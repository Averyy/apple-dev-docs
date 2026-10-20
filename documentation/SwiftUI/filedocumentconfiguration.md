# FileDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The properties of an open file document.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to Document and use URLDocumentConfiguration instead.

## Declaration

```swift
struct FileDocumentConfiguration<Document> where Document : FileDocument
```

#### Overview

You receive an instance of this structure when you create a [`DocumentGroup`](./documentgroup.md) with a value file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document
- [var document: Document](./filedocumentconfiguration/document.md)
  The current document model.
- [var $document: Binding<Document>](./filedocumentconfiguration/dollardocument.md)
### Getting document properties
- [var fileURL: URL?](./filedocumentconfiguration/fileurl.md)
  The URL of the open file document.
- [var isEditable: Bool](./filedocumentconfiguration/iseditable.md)
  A Boolean that indicates whether you can edit the document.
### Instance Properties
- [var creationSource: DocumentCreationSource?](./filedocumentconfiguration/creationsource.md)
  The source associated with the button that created this document.

## See Also

### Deprecated structures
- [struct FileDocumentReadConfiguration](./filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](./filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [struct ReferenceFileDocumentConfiguration](./referencefiledocumentconfiguration.md)
  The properties of an open reference file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentconfiguration)*