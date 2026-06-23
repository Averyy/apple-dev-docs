# URLDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: class

A set of settings and properties of an open document.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class URLDocumentConfiguration
```

## Topics

### Accessing document properties
- [var fileURL: URL?](urldocumentconfiguration/fileurl.md)
  A URL of the open document if it is saved to disk.
- [var lastContentModificationDate: Date?](urldocumentconfiguration/lastcontentmodificationdate.md)
  The date on which the contents of the document were last modified, if available.
- [var creationSource: DocumentCreationSource?](urldocumentconfiguration/creationsource.md)
  The source associated with the button that created this document.
### Coordinating file access
- [func makeFileCoordinator() -> sending NSFileCoordinator](urldocumentconfiguration/makefilecoordinator.md)
  A coordinator that can be used to coordinate additional read and write operations to prevent document corruption.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Document](document.md)
- [protocol ReadableDocument](readabledocument.md)
  A type that you use to read documents from file.
- [protocol WritableDocument](writabledocument.md)
  A type that you use to write documents to file.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Provides context about how a document was created or opened.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration)*