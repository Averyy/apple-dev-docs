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

Use `FileWrapperDocumentWriter` for simple cases where the application does not need custom writing logic. It is efficient for documents of small and medium size.

> **Note**: For large files or packages, provide a custom [`DocumentWriter`](documentwriter.md) that writes only what changed.

## Topics

### Creating a writer
- [init(sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: (Snapshot) async throws -> FileWrapper)](filewrapperdocumentwriter/init(_:makefilewrapper:).md)
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