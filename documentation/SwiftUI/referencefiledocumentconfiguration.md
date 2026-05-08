# ReferenceFileDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of an open reference file document.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument
```

#### Overview

You receive an instance of this structure when you create a [`DocumentGroup`](documentgroup.md) with a reference file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document
- [var document: Document](referencefiledocumentconfiguration/document.md)
  The current document model.
- [var $document: ObservedObject<Document>.Wrapper](referencefiledocumentconfiguration/$document.md)
### Getting document properties
- [var fileURL: URL?](referencefiledocumentconfiguration/fileurl.md)
  The URL of the open file document.
- [var isEditable: Bool](referencefiledocumentconfiguration/iseditable.md)
  A Boolean that indicates whether you can edit the document.

## See Also

- [protocol ReferenceFileDocument](referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration)*