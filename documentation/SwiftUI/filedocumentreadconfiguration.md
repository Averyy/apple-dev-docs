# FileDocumentReadConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The configuration for reading file contents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct FileDocumentReadConfiguration
```

## Topics

### Reading the content
- [let contentType: UTType](filedocumentreadconfiguration/contenttype.md)
  The expected uniform type of the file contents.
- [let file: FileWrapper](filedocumentreadconfiguration/file.md)
  The file wrapper containing the document content.

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  Provides the information required to read a document from disk.
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  Provides the information required to write a document to disk.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [protocol DocumentReader](documentreader.md)
  Implements logic of reading documents from disk.
- [protocol DocumentWriter](documentwriter.md)
  Implements logic of writing documents to disk.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that uses `FileWrapper` for reading.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that uses `FileWrapper` for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentreadconfiguration)*