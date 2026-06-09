# fileURL

**Framework**: SwiftUI  
**Kind**: property

A URL of the open document if it is saved to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(unsafe) final var fileURL: URL? { get set }
```

#### Discussion

Returns `nil` if the document has never been saved.

## See Also

- [var lastContentModificationDate: Date?](urldocumentconfiguration/lastcontentmodificationdate.md)
  The date on which the contents of the document were last modified, if available.
- [var creationSource: DocumentCreationSource?](urldocumentconfiguration/creationsource.md)
  The source associated with the button that created this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/fileurl)*