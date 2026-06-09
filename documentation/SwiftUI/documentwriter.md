# DocumentWriter

**Framework**: SwiftUI  
**Kind**: protocol

Implements logic of writing documents to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DocumentWriter<Snapshot>
```

## Topics

### Writing a document
- [func write(content: sending Self.Snapshot, to: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws](documentwriter/write(content:to:previous:progress:).md)
  Writes the document content to disk.
- [associatedtype Snapshot](documentwriter/snapshot.md)
  A type that represents the document’s stored content.
- [associatedtype Destination](documentwriter/destination.md)

## Relationships

### Conforming Types
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md)

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
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that uses `FileWrapper` for reading.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that uses `FileWrapper` for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter)*