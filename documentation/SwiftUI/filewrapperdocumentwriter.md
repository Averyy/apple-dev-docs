# FileWrapperDocumentWriter

**Framework**: SwiftUI  
**Kind**: struct

A document writer that serializes a snapshot into a `FileWrapper`.

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
extension TextDocument: WritableDocument {
    func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(regularFileWithContents: Data(snapshot.utf8))
        }
    }

    // ...
}
```

## Topics

### Creating a writer
- [init(sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: (Snapshot, FileWrapper?) async throws -> FileWrapper)](filewrapperdocumentwriter/init(_:makefilewrapper:).md)
  Creates a writer that converts a snapshot into a `FileWrapper`.
- [FileWrapperDocumentWriter.WriteConfiguration](filewrapperdocumentwriter/writeconfiguration.md)

## Relationships

### Conforms To
- [DocumentWriter](documentwriter.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter)*