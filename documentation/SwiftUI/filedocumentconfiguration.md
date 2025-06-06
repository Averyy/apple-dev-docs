# FileDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of an open file document.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct FileDocumentConfiguration<Document> where Document : FileDocument
```

#### Overview

You receive an instance of this structure when you create a [`DocumentGroup`](documentgroup.md) with a value file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document
- [var document: Document](filedocumentconfiguration/document.md)
  The current document model.
- [var $document: Binding<Document>](filedocumentconfiguration/$document.md)
### Getting document properties
- [var fileURL: URL?](filedocumentconfiguration/fileurl.md)
  The URL of the open file document.
- [var isEditable: Bool](filedocumentconfiguration/iseditable.md)
  A Boolean that indicates whether you can edit the document.

## See Also

- [protocol FileDocument](filedocument.md)
  A type that you use to serialize documents to and from file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentconfiguration)*