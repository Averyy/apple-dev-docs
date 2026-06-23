# Document

**Framework**: SwiftUI  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Document : ReadableDocument, WritableDocument
```

## Relationships

### Inherits From
- [ReadableDocument](readabledocument.md)
- [WritableDocument](writabledocument.md)

## See Also

- [protocol ReadableDocument](readabledocument.md)
  A type that you use to read documents from file.
- [protocol WritableDocument](writabledocument.md)
  A type that you use to write documents to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  A set of settings and properties of an open document.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Provides context about how a document was created or opened.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/document)*