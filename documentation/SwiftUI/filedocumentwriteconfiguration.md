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

- [protocol FileDocument](filedocument.md)
  A type that you use to serialize documents to and from file.
- [struct FileDocumentConfiguration](filedocumentconfiguration.md)
  The properties of an open file document.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct NewDocumentAction](newdocumentaction.md)
  An action that presents a new document.
- [protocol ReferenceFileDocument](referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.
- [struct ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md)
  The properties of an open reference file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration)*