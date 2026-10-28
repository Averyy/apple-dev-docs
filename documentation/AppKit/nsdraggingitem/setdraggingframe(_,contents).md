# setDraggingFrame(_:contents:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the item’s dragging frame and contents.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setDraggingFrame(_ frame: NSRect, contents: Any?)
```

```objc
- (void) setDraggingFrame:(NSRect) frame contents:(id) contents;
```

## Discussion

Alternate single image component setter.

This convenience method simplifies modifying the components of an `NSDraggingItem` when there is only one component. It sets the [`draggingFrame`](./draggingframe.md) and creates a single [`NSDraggingImageComponent`](../nsdraggingimagecomponent.md) instance with one image corresponding to the [`icon`](./imagecomponentkey/icon.md) key. You should use this method only under the following conditions: the drag image for this item is composed of a single image, or there are a reasonable number of dragging item instances being created or enumerated.

If your application requires the dragging of hundreds of items this method would create a instance for each item when it is called. Compare this to the [`imageComponentsProvider`](./imagecomponentsprovider.md) block which is much faster to define and allows AppKit to create only a subset of the items using [`imageComponentsProvider`](./imagecomponentsprovider.md).

This method sets the [`draggingFrame`](./draggingframe.md) and [`imageComponents`](./imagecomponents.md) properties.

## Parameters

- `frame`: The item content frame, which is in the same coordinate space as the value of [`draggingFrame`](./draggingframe.md).
- `contents`: The item contents to display when dragging. Typically this is an `NSImage`, but a `CGImageRef` will also work.

## See Also

### Related Documentation
- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](./imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
### Dragging frame
- [var draggingFrame: NSRect](./draggingframe.md)
  The frame of the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/setdraggingframe(_:contents:))*