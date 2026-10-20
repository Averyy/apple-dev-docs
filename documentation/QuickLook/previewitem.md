# PreviewItem

**Framework**: Quick Look  
**Kind**: struct  
**Role**: Structure

An item to preview in the preview application.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct PreviewItem
```

## Topics

### Operators
- [static func == (PreviewItem, PreviewItem) -> Bool](./previewitem/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two preview items are equal.
### Initializers
- [init(url: URL, displayName: String?, editingMode: EditingMode)](./previewitem/init%28url,displayname,editingmode%29.md)
  Create a preview item from a URL and, optionally, a displayName and editingMode.
### Instance Properties
- [let displayName: String?](./previewitem/displayname.md)
  An optional display name to present for the preview item.
- [let editingMode: EditingMode](./previewitem/editingmode.md)
  The editingMode for the preview item.
- [let id: UUID](./previewitem/id.md)
  The stable identity of the preview item.
### Instance Methods
- [func hash(into: inout Hasher)](./previewitem/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewitem)*