# imageComponents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of dragging image components to use to create the drag image.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var imageComponents: [NSDraggingImageComponent]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSDraggingImageComponent *> * imageComponents;
```

#### Discussion

The array contains copies of the components. The drag does not reflect changes you make to these copies. If needed, the system calls the [`imageComponentsProvider`](./imagecomponentsprovider.md) block to generate the image components.

## See Also

### Drag image components
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](./imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [NSDraggingItem.ImageComponentKey](./imagecomponentkey.md)
  Keys that identify components of a dragging image.
- [var item: Any](./item.md)
  The pasteboard reader or writer object dependent on the context where you use the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/imagecomponents)*