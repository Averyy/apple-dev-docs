# dragSelection(with:offset:slideBack:)

**Framework**: AppKit  
**Kind**: method

Begins dragging the current selected text range.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dragSelection(with event: NSEvent, offset mouseOffset: NSSize, slideBack: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the drag can be successfully initiated, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Primarily for subclasses, who can override it to intervene at the beginning of a drag.

## Parameters

- `event`: The event that initiated dragging the selection.
- `mouseOffset`: The cursor’s current location relative to the mouse-down  .
- `slideBack`:   if the image being dragged should slide back to its original position if the drag does not succeed,   otherwise.

## See Also

- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](nstextview/dragimageforselection(with:origin:).md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragOperation(for: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation](nstextview/dragoperation(for:type:).md)
  Returns the type of drag operation that should be performed if the image were released now.
- [var acceptsGlyphInfo: Bool](nstextview/acceptsglyphinfo.md)
  A Boolean value that indicates whether the receiver accepts the glyph info attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/dragselection(with:offset:slideback:))*