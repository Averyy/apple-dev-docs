# NSDraggingItem.ImageComponentKey

**Framework**: AppKit  
**Kind**: struct

Keys that identify components of a dragging image.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ImageComponentKey
```

## Topics

### Initializing a component key
- [init(String)](nsdraggingitem/imagecomponentkey/init(_:).md)
  Creates an image component key using the string you provide.
- [init(rawValue: String)](nsdraggingitem/imagecomponentkey/init(rawvalue:).md)
  Creates an image component key using the string you provide.
### Image component keys
- [static let icon: NSDraggingItem.ImageComponentKey](nsdraggingitem/imagecomponentkey/icon.md)
  A key for a corresponding value that is a dragging item’s image.
- [static let label: NSDraggingItem.ImageComponentKey](nsdraggingitem/imagecomponentkey/label.md)
  A key for a corresponding value that represents a textual label for a dragging item, for example, a file name.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var imageComponents: [NSDraggingImageComponent]?](nsdraggingitem/imagecomponents.md)
  An array of dragging image components to use to create the drag image.
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](nsdraggingitem/imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [var item: Any](nsdraggingitem/item.md)
  The pasteboard reader or writer object dependent on the context where you use the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/imagecomponentkey)*