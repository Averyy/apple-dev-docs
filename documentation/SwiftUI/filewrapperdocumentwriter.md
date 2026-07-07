# FileWrapperDocumentWriter

**Framework**: SwiftUI  
**Kind**: struct

A document writer that uses `FileWrapper` for writing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FileWrapperDocumentWriter<Snapshot>
```

#### Overview

The `makeFileWrapper` closure in [`init(_:makeFileWrapper:)`](filewrapperdocumentwriter/init(_:makefilewrapper:).md) turns the document’s snapshot into a `FileWrapper` that SwiftUI writes to disk. It receives the current snapshot and, when available, the `FileWrapper` from the document’s last read or write. For documents written as a single file, ignore `previous` and return a freshly built wrapper:

```swift
extension TextDocument {
    func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(regularFileWithContents: Data(snapshot.utf8))
        }
    }
}
```

For package documents, also prefer building a fresh `FileWrapper` by default — it’s straightforward and correct.

Alternatively, when needed, you can implement incremental write: mutate `previous` in place and return it. `FileWrapper` only writes children that actually changed, so unchanged entries stay untouched on disk — letting you avoid rewriting an entire package on every save.

Reach for incremental writes only when profiling or user reports show that rewriting the whole package is too expensive: keeping `previous` consistent with the latest snapshot adds nontrivial bookkeeping, since you have to add new entries, replace changed ones, and explicitly remove anything that disappeared from the snapshot, as the example below demonstrates:

```swift
struct NotebookSnapshot {
    var pages: [UUID: PageContent]
}

struct PageContent {
    var text: String
    var hasChanges: Bool
}

extension NotebookDocument {
    func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<NotebookSnapshot> {
        FileWrapperDocumentWriter(configuration) { snapshot, previous in
            let directoryWrapper = previous
                ?? FileWrapper(directoryWithFileWrappers: [:])
            // Find or create the "pages" subdirectory in place.
            let pagesWrapper: FileWrapper
            if let existing = directoryWrapper
                .fileWrappers?["pages"] {
                pagesWrapper = existing
            } else {
                pagesWrapper = FileWrapper(
                    directoryWithFileWrappers: [:]
                )
                pagesWrapper.preferredFilename = "pages"
                directoryWrapper.addFileWrapper(pagesWrapper)
            }
            // Replace each changed page in place. Unchanged
            // pages are left alone, so FileWrapper skips their
            // disk writes.
            for (pageIdentifier, pageContent) in snapshot.pages
            where pageContent.hasChanges {
                let filename = "\(pageIdentifier.uuidString).txt"
                if let stale = pagesWrapper
                    .fileWrappers?[filename] {
                    pagesWrapper.removeFileWrapper(stale)
                }
                let pageWrapper = FileWrapper(
                    regularFileWithContents:
                        Data(pageContent.text.utf8)
                )
                pageWrapper.preferredFilename = filename
                pagesWrapper.addFileWrapper(pageWrapper)
            }
            // Drop any pages that no longer exist in the
            // snapshot — with in-place mutation, deletion has
            // to be explicit.
            let liveFilenames = Set(
                snapshot.pages.keys.map {
                    "\($0.uuidString).txt"
                }
            )
            for (filename, wrapper) in
                pagesWrapper.fileWrappers ?? [:]
            where !liveFilenames.contains(filename) {
                pagesWrapper.removeFileWrapper(wrapper)
            }
            return directoryWrapper
        }
    }
}
```

## Topics

### Creating a writer
- [init(sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: (Snapshot, FileWrapper?) async throws -> FileWrapper)](filewrapperdocumentwriter/init(_:makefilewrapper:).md)
  Creates a writer that uses `FileWrapper` to write documents to disk.
- [FileWrapperDocumentWriter.WriteConfiguration](filewrapperdocumentwriter/writeconfiguration.md)

## Relationships

### Conforms To
- [DocumentWriter](documentwriter.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  Provides the information required to read a document from disk.
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  Provides the information required to write a document to disk.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [protocol DocumentReader](documentreader.md)
  Implements logic of reading documents from disk.
- [protocol DocumentWriter](documentwriter.md)
  Implements logic of writing documents to disk.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that uses `FileWrapper` for reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter)*