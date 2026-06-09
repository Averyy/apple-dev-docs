# FileDocumentWriteConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The configuration for serializing file contents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct FileDocumentWriteConfiguration
```

## Topics

### Writing the content
- [let contentType: UTType](filedocumentwriteconfiguration/contenttype.md)
  The expected uniform type of the file contents.
- [let existingFile: FileWrapper?](filedocumentwriteconfiguration/existingfile.md)
  The file wrapper containing the current document content. `nil` if the document is unsaved.

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  Provides the information required to read a document from disk.
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  Provides the information required to write a document to disk.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [protocol DocumentReader](documentreader.md)
  Implements logic of reading documents from disk.
- [protocol DocumentWriter](documentwriter.md)
  Implements logic of writing documents to disk.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that uses `FileWrapper` for reading.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that uses `FileWrapper` for writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration)*