# PreviewItem

**Framework**: Quick Look  
**Kind**: struct

An item to preview in the preview application.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct PreviewItem
```

## Topics

### Operators
- [static func == (PreviewItem, PreviewItem) -> Bool](previewitem/==(_:_:).md)
  Returns a Boolean value that indicates whether two preview items are equal.
### Initializers
- [init(url: URL, displayName: String?, editingMode: EditingMode)](previewitem/init(url:displayname:editingmode:).md)
  Create a preview item from a URL and, optionally, a displayName and editingMode.
### Instance Properties
- [let displayName: String?](previewitem/displayname.md)
  An optional display name to present for the preview item.
- [let editingMode: EditingMode](previewitem/editingmode.md)
  The editingMode for the preview item.
- [let id: UUID](previewitem/id.md)
  The stable identity of the preview item.
### Instance Methods
- [func hash(into: inout Hasher)](previewitem/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewitem)*