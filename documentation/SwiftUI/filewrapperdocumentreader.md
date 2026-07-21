# FileWrapperDocumentReader

**Framework**: SwiftUI  
**Kind**: struct

A document reader that deserializes a `FileWrapper` into a snapshot.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FileWrapperDocumentReader<Snapshot>
```

#### Overview

This is the recommended reader for most documents. Provide a closure that converts a `FileWrapper` into your snapshot type, and `FileWrapperDocumentReader` handles file coordination and loading.

```swift
func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
    FileWrapperDocumentReader(configuration) { fileWrapper in
        guard let data =
            fileWrapper.regularFileContents else {
            throw CocoaError(.fileReadCorruptFile)
        }
        return String(decoding: data, as: UTF8.self)
    }
}
```

For package documents, navigate the `FileWrapper` hierarchy:

```swift
FileWrapperDocumentReader(configuration) { directory in
    let children = directory.fileWrappers ?? [:]
    guard let metadataData = children["metadata.json"]?
        .regularFileContents else {
        throw CocoaError(.fileReadCorruptFile)
    }
    return try JSONDecoder().decode(
        Metadata.self, from: metadataData
    )
}
```

> ❗ **Important**: `FileWrapper` loads file contents on demand. A child file may be gone by the time you call `regularFileContents`. Always handle errors when reading children of a package.

The closure does not receive a `Subprogress`. To report progress during reads, use a custom [`DocumentReader`](documentreader.md) instead.

## Topics

### Creating a reader
- [init(sending FileWrapperDocumentReader<Snapshot>.ReadConfiguration, makeSnapshot: (FileWrapper) async throws -> sending Snapshot)](filewrapperdocumentreader/init(_:makesnapshot:).md)
  Creates a reader that converts a `FileWrapper` into a snapshot.
- [FileWrapperDocumentReader.ReadConfiguration](filewrapperdocumentreader/readconfiguration.md)

## Relationships

### Conforms To
- [DocumentReader](documentreader.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader)*