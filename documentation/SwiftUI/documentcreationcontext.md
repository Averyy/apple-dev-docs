# DocumentCreationContext

**Framework**: SwiftUI  
**Kind**: struct

Provides context about how a document was created or opened.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DocumentCreationContext
```

## Topics

### Accessing creation properties
- [var creationSource: DocumentCreationSource?](documentcreationcontext/creationsource.md)
  The source associated with the button that created this document.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol Document](document.md)
- [protocol ReadableDocument](readabledocument.md)
  A type that you use to read documents from file.
- [protocol WritableDocument](writabledocument.md)
  A type that you use to write documents to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  A set of settings and properties of an open document.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentcreationcontext)*