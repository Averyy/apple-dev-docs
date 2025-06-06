# dragOperation(for:type:)

**Framework**: AppKit  
**Kind**: method

Returns the type of drag operation that should be performed if the image were released now.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dragOperation(for dragInfo: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation
```

#### Return Value

The drag operation that should be performed if the image were released now.

#### Discussion

The returned value should be one of the following:

| Option | Meaning |
| --- | --- |
| `NSDragOperationCopy` | The data represented by the image will be copied. |
| `NSDragOperationLink` | The data will be shared. |
| `NSDragOperationGeneric` | The operation will be defined by the destination. |
| `NSDragOperationPrivate` | The operation is negotiated privately between the source and the destination. |

If none of the operations is appropriate, this method should return `NSDragOperationNone`.

This method is called repeatedly from [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) and [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) as the user drags the image.

## Parameters

- `dragInfo`: The drag information.
- `type`: The pasteboard type that will be read from the dragging pasteboard.

## See Also

- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingupdated(_:).md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingentered(_:).md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](nstextview/dragimageforselection(with:origin:).md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](nstextview/dragselection(with:offset:slideback:).md)
  Begins dragging the current selected text range.
- [var acceptsGlyphInfo: Bool](nstextview/acceptsglyphinfo.md)
  A Boolean value that indicates whether the receiver accepts the glyph info attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/dragoperation(for:type:))*