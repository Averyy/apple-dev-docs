# setDraggingFrame(_:contents:)

**Framework**: AppKit  
**Kind**: method

Sets the item’s dragging frame and contents.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setDraggingFrame(_ frame: NSRect, contents: Any?)
```

#### Discussion

Alternate single image component setter.

This convenience method simplifies modifying the components of an `NSDraggingItem` when there is only one component. It sets the [`draggingFrame`](nsdraggingitem/draggingframe.md) and creates a single [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) instance with one image corresponding to the [`icon`](nsdraggingitem/imagecomponentkey/icon.md) key. You should use this method only under the following conditions: the drag image for this item is composed of a single image, or there are a reasonable number of dragging item instances being created or enumerated.

If your application requires the dragging of hundreds of items this method would create a instance for each item when it is called. Compare this to the [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md) block which is much faster to define and allows AppKit to create only a subset of the items using [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md).

This method sets the [`draggingFrame`](nsdraggingitem/draggingframe.md) and [`imageComponents`](nsdraggingitem/imagecomponents.md) properties.

## Parameters

- `frame`: The item content frame, which is in the same coordinate space as the value of  .
- `contents`: The item contents to display when dragging. Typically this is an  , but a   will also work.

## See Also

- [var imageComponentsProvider: (() -> [NSDraggingImageComponent])?](nsdraggingitem/imagecomponentsprovider.md)
  An array of blocks that provide the dragging image components.
- [var draggingFrame: NSRect](nsdraggingitem/draggingframe.md)
  The frame of the dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/setdraggingframe(_:contents:))*