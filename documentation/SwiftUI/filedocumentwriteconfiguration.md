# FileDocumentWriteConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The configuration for serializing file contents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use the Document protocol and URLDocumentConfiguration.

## Declaration

```swift
struct FileDocumentWriteConfiguration
```

## Topics

### Writing the content
- [let contentType: UTType](./filedocumentwriteconfiguration/contenttype.md)
  The expected uniform type of the file contents.
- [let existingFile: FileWrapper?](./filedocumentwriteconfiguration/existingfile.md)
  The file wrapper containing the current document content. `nil` if the document is unsaved.

## See Also

### Deprecated structures
- [struct FileDocumentConfiguration](./filedocumentconfiguration.md)
  The properties of an open file document.
- [struct FileDocumentReadConfiguration](./filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct ReferenceFileDocumentConfiguration](./referencefiledocumentconfiguration.md)
  The properties of an open reference file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration)*