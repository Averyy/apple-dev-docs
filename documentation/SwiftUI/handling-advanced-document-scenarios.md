# Handling advanced document scenarios

**Framework**: SwiftUI

Extend your document-based app to support custom file formats, on-demand file access, and progress reporting.

#### Overview

After you’ve created a working document-based app, you can extend it to handle scenarios that go beyond basic reading and writing. Support file formats that the system doesn’t know about by default by using a custom [`UTType`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype). Access files outside the normal read and write lifecycle using [`makeFileCoordinator()`](URLDocumentConfiguration/makeFileCoordinator().md), for example, to open a specific subfile in a package on demand. Add progress reporting to give people feedback during long operations.

> **Note**: If you’re new to document-based apps in SwiftUI, start with [`Creating a document-based app`](creating-a-document-based-app.md).

#### Declare a Custom File Format

The system knows about popular built-in formats and their identifiers, like [`utf8PlainText`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf8plaintext), [`jpeg`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/jpeg), and [`markdown`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/markdown). For your own file formats, declare a custom [`UTType`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype) so the Finder, the document browser, and Spotlight understand them.

Every custom type needs a base type that tells the system what kind of file it is. Use `public.data` or conforming types as a base type for single-file documents, or `com.apple.package` for documents the system stores as a directory but presents as a single file.

Declare the content type in your app target’s information property list under `UTExportedTypeDeclarations` so the Finder, the document browser, and Spotlight all recognize it. Set `UTTypeConformsTo` to the matching base type and add a `UTTypeTagSpecification` that maps the type to your filename extension. The example below declares a notebook package; for a flat-file format, swap `com.apple.package` for `public.data`, like this:

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.example.notebook</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>com.apple.package</string>
        </array>
        <key>UTTypeTagSpecification</key>
        <dict>
            <key>public.filename-extension</key>
            <array>
                <string>examplenotebook</string>
            </array>
        </dict>
    </dict>
</array>
```

For convenience, mirror the declaration in code, as shown here:

```swift
extension UTType {
    static let notebook = UTType(exportedAs: "com.example.notebook")
}
```

Then reference your type from the document’s [`readableContentTypes`](ReadableDocument/readableContentTypes.md) and [`writableContentTypes`](WritableDocument/writableContentTypes.md), like this:

```swift
static let readableContentTypes: [UTType] = [.notebook]
static let writableContentTypes: [UTType] = [.notebook, .utf8PlainText]
```

For more about declaring uniform type identifiers for proprietary formats, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app).

> **Note**: Every Mac registers the standard content types that the system provides, but the set of less common types each computer recognizes depends on the software installed on it. A computer might not recognize certain media types, for example, if no installed app declares them. Similarly, a computer that doesn’t have Xcode installed doesn’t recognize `com.apple.xcode.resultbundle`, the type identifier for Xcode result bundles.

#### Access Files Outside Read and Write

SwiftUI coordinates file access for `read` and `write` calls automatically. To access the file URL at other times — for example, when reading a specific subfile in a package — use the configuration’s file coordinator, as shown here:

```swift
let coordinator = document.configuration.makeFileCoordinator()
coordinator.coordinate(
    readingItemAt: packageURL.appending(path: "metadata.json"),
                       options: []) { url in
    do {
        let data = try Data(contentsOf: url)
        let metadata = try JSONDecoder().decode(NotebookMetadata.self, from: data)
        // Process the metadata.
    } catch {
        // Handle errors.
    }
}
```

> ❗ **Important**: Always use [`makeFileCoordinator()`](URLDocumentConfiguration/makeFileCoordinator().md) for disk access outside of `read` and `write`. Accessing the file URL directly risks corruption because other processes, including iCloud, can change it any time.

#### Report Progress

Packages let you read and write incrementally; instead of loading or saving the whole document on every change, you can read only the files you need and write only the ones that changed. For notebook documents that consist of multiple files, custom image formats that store data in separate files, or projects with embedded media, this can mean the difference between a fast autosave and a slow one.

Both [`DocumentReader`](DocumentReader.md) and [`DocumentWriter`](DocumentWriter.md) receive a [`Subprogress`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/subprogress) parameter via their `read` and `write` methods, respectively. Report progress through the parameter so SwiftUI can display the appropriate UI during long operations.

Create a [`ProgressReporter`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/progressreporter) from the [`Subprogress`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/subprogress) by specifying a total unit count. Then call [`complete(count:)`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/progressreporter/complete(count:)) as the work finishes, like this:

```swift
@concurrent 
func read(from source: URL, progress: consuming Subprogress) async throws -> sending ImageSnapshot {
    let progressManager = progress.start(totalCount: 2)
    let data = try Data(contentsOf: source)
    progressManager.complete(count: 1)
    let image = try decodeImage(from: data)
    progressManager.complete(count: 1)
    return ImageSnapshot(image: image)
}
```

For package documents, you can treat each file as an equal chunk of work, as shown below. This approach gives granular feedback as the writer processes files one by one.

```swift
@concurrent
func write(
    snapshot: sending NotebookSnapshot, to destination: URL,
    previous: sending NotebookSnapshot?, progress: consuming Subprogress
) async throws {
    let changedPages = snapshot.pages.filter { (identifier, content) in
        previous?.pages[identifier] != content
    }

    // One unit for metadata, and one unit per changed page.
    let totalUnits = 1 + changedPages.count
    let progressManager = progress.start(totalCount: totalUnits)

    // Write the metadata.
    let metadataURL = destination.appending(path: "metadata.json")
    let metadataData = try JSONEncoder().encode(snapshot.metadata)
    try metadataData.write(to: metadataURL, options: .atomic)
    progressManager.complete(count: 1)

    // Write each changed page individually.
    let fileManager = FileManager.default
    let pagesDirectory = destination.appending(path: "pages")

    // Create the pages subdirectory if it doesn't already exist.
    try? fileManager.createDirectory(
        at: pagesDirectory, withIntermediateDirectories: true
    )

    for (identifier, content) in changedPages {
        let pageURL = pagesDirectory.appending(
            path: "\(identifier.uuidString).txt"
        )
        let data = Data(content.utf8)
        try data.write(to: pageURL, options: .atomic)
        progressManager.complete(count: 1)
    }
}
```

If you use [`FileHandle`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filehandle) or [`OutputStream`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/outputstream) to write files in chunks — for example, a large media file — report progress after each chunk rather than only once at the end. Each call to [`complete(count:)`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/progressreporter/complete(count:)) moves the progress bar forward, so spread the calls throughout the write.

The example below writes a large media file to disk in chunks. Set the total unit count to the file size in bytes, and call the reporter after each chunk so the progress bar updates smoothly.

```swift
@concurrent
func write(
    snapshot: sending MediaSnapshot, to destination: URL,
    previous: sending MediaSnapshot?, progress: consuming Subprogress
) async throws {
    let payload = snapshot.payload
    let totalBytes = payload.count
    let progressManager = progress.start(totalCount: totalBytes)

    try Data().write(to: destination)
    let fileHandle = try FileHandle(forWritingTo: destination)
    defer { try? fileHandle.close() }

    // Aim for ~100 progress updates across the write, clamped so chunks
    // stay large enough to amortize system call overhead and small enough
    // to keep the progress bar moving on tiny payloads.
    let targetUpdateCount = 100
    let minimumChunkSize = 64 * 1024        //  64 KB
    let maximumChunkSize = 4 * 1024 * 1024  //   4 MB
    let chunkSize = min(
        maximumChunkSize,
        max(minimumChunkSize, totalBytes / targetUpdateCount)
    )

    var offset = 0
    while offset < totalBytes {
        let end = min(offset + chunkSize, totalBytes)
        let chunk = payload[offset..<end]
        try fileHandle.write(contentsOf: chunk)
        progressManager.complete(count: end - offset)
        offset = end
    }
}
```

The chunk size adapts to the file size, so large files don’t generate unnecessary system overhead. If you stream to an [`OutputStream`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/outputstream) instead, the same pattern applies: Open the stream, write chunks of the computed size, call [`complete(count:)`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/progressreporter/complete(count:)) with the bytes written, and call `ProgresManager.complete(count:)` when finished.

> **Note**: Even when you report progress, SwiftUI decides whether to show a progress view.

## See Also

- [Creating a document-based app](creating-a-document-based-app.md)
  Build apps that people can use to open, edit, and save files using coordinated file access.
- [Updating your document-based app](updating-your-document-based-app.md)
  Migrate an existing app to adopt URL-based document reading and writing with Swift concurrency.
- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md)
  Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct DocumentGroup](documentgroup.md)
  A scene that enables support for opening, creating, and saving documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/handling-advanced-document-scenarios)*