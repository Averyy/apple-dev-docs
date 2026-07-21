# DocumentBaseBox

**Framework**: SwiftUI  
**Kind**: protocol

A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol DocumentBaseBox<Document> : AnyObject
```

## Topics

### Specifying the document type
- [associatedtype Document](documentbasebox/document.md)
  The underlying document type.
### Accessing the document
- [var base: Self.Document?](documentbasebox/base.md)
  Updates the underlying document to a new value.

## See Also

- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentbasebox)*