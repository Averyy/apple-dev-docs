# dragOperation(for:type:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the type of drag operation that should be performed if the image were released now.

**Availability**:
- macOS

## Declaration

```swift
func dragOperation(for dragInfo: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation
```

```objc
- (NSDragOperation) dragOperationForDraggingInfo:(id<NSDraggingInfo>) dragInfo type:(NSPasteboardType) type;
```

## Return Value

The drag operation that should be performed if the image were released now.

## Discussion

The returned value should be one of the following:

| Option | Meaning |
| --- | --- |
| `NSDragOperationCopy` | The data represented by the image will be copied. |
| `NSDragOperationLink` | The data will be shared. |
| `NSDragOperationGeneric` | The operation will be defined by the destination. |
| `NSDragOperationPrivate` | The operation is negotiated privately between the source and the destination. |

If none of the operations is appropriate, this method should return `NSDragOperationNone`.

This method is called repeatedly from [`draggingEntered(_:)`](../nsdraggingdestination/draggingentered%28_%29.md) and [`draggingUpdated(_:)`](../nsdraggingdestination/draggingupdated%28_%29.md) as the user drags the image.

## Parameters

- `dragInfo`: The drag information.
- `type`: The pasteboard type that will be read from the dragging pasteboard.

## See Also

### Related Documentation
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](../nsdraggingdestination/draggingupdated%28_%29.md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](../nsdraggingdestination/draggingentered%28_%29.md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
### Dragging
- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](./dragimageforselection%28with,origin%29.md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](./dragselection%28with,offset,slideback%29.md)
  Begins dragging the current selected text range.
- [var acceptsGlyphInfo: Bool](./acceptsglyphinfo.md)
  A Boolean value that indicates whether the receiver accepts the glyph info attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/dragoperation(for:type:))*