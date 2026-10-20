# NSDraggingItem.ImageComponentKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys that identify components of a dragging image.

**Availability**:
- macOS

## Declaration

```swift
struct ImageComponentKey
```

```c
typedef NSString * NSDraggingImageComponentKey;
```

## Topics

### Initializing a component key
- [init(String)](./imagecomponentkey/init%28_%29.md)
  Creates an image component key using the string you provide.
- [init(rawValue: String)](./imagecomponentkey/init%28rawvalue%29.md)
  Creates an image component key using the string you provide.
### Image component keys
- [static let icon: NSDraggingItem.ImageComponentKey](./imagecomponentkey/icon.md)
  A key for a corresponding value that is a dragging item’s image.
- [static let label: NSDraggingItem.ImageComponentKey](./imagecomponentkey/label.md)
  A key for a corresponding value that represents a textual label for a dragging item, for example, a file name.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Drag image components
- [var imageComponents: [NSDraggingImageComponent]?](./imagecomponents.md)
  An array of dragging image components to use to create the drag image.
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](./imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [var item: Any](./item.md)
  The pasteboard reader or writer object dependent on the context where you use the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/imagecomponentkey)*