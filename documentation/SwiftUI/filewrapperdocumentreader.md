# FileWrapperDocumentReader

**Framework**: SwiftUI  
**Kind**: struct

A document reader that uses `FileWrapper` for reading.

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

Use `FileWrapperDocumentReader` for simple cases where the application does not need custom reading logic. It is efficient for documents of small and medium size.

> **Note**: For large files or packages, provide a custom [`DocumentReader`](documentreader.md) that reads only what changed.

## Topics

### Creating a reader
- [init(sending FileWrapperDocumentReader<Snapshot>.ReadConfiguration, makeSnapshot: (FileWrapper) async throws -> sending Snapshot)](filewrapperdocumentreader/init(_:makesnapshot:).md)
  Creates a reader that uses `FileWrapper` to read documents from disk.
- [FileWrapperDocumentReader.ReadConfiguration](filewrapperdocumentreader/readconfiguration.md)

## Relationships

### Conforms To
- [DocumentReader](documentreader.md)

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
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that uses `FileWrapper` for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader)*