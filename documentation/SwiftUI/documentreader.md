# DocumentReader

**Framework**: SwiftUI  
**Kind**: protocol

Implements logic of reading documents from disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DocumentReader<Snapshot>
```

## Topics

### Reading a document
- [func read(from: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot](documentreader/read(from:progress:).md)
  Reads the document from disk.
- [associatedtype Snapshot](documentreader/snapshot.md)
  A type that represents the document’s stored content.
- [associatedtype Source](documentreader/source.md)

## Relationships

### Conforming Types
- [FileWrapperDocumentReader](filewrapperdocumentreader.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  Provides the information required to read a document from disk.
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  Provides the information required to write a document to disk.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [protocol DocumentWriter](documentwriter.md)
  Implements logic of writing documents to disk.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that uses `FileWrapper` for reading.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that uses `FileWrapper` for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader)*