# imageComponents

**Framework**: AppKit  
**Kind**: property

An array of dragging image components to use to create the drag image.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var imageComponents: [NSDraggingImageComponent]? { get }
```

#### Discussion

The array contains copies of the components. The drag does not reflect changes you make to these copies. If needed, the system calls the [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md) block to generate the image components.

## See Also

- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](nsdraggingitem/imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [NSDraggingItem.ImageComponentKey](nsdraggingitem/imagecomponentkey.md)
  Keys that identify components of a dragging image.
- [var item: Any](nsdraggingitem/item.md)
  The pasteboard reader or writer object dependent on the context where you use the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/imagecomponents)*