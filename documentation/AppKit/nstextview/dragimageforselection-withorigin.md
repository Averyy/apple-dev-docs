# dragImageForSelection(with:origin:)

**Framework**: AppKit  
**Kind**: method

Returns an appropriate drag image for the drag initiated by the specified event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dragImageForSelection(with event: NSEvent, origin: NSPointPointer?) -> NSImage?
```

#### Return Value

An appropriate drag image for the drag initiated by `event`. May be `nil`, in which case a default icon will be used.

#### Discussion

This method is used by [`dragSelection(with:offset:slideBack:)`](nstextview/dragselection(with:offset:slideback:).md). It can be called by others who need such an image, or can be overridden by subclasses to return a different image.

## Parameters

- `event`: The event that initiated the drag session.
- `origin`: On return, the lower-left point of the image in view coordinates.

## See Also

- [func dragOperation(for: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation](nstextview/dragoperation(for:type:).md)
  Returns the type of drag operation that should be performed if the image were released now.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](nstextview/dragselection(with:offset:slideback:).md)
  Begins dragging the current selected text range.
- [var acceptsGlyphInfo: Bool](nstextview/acceptsglyphinfo.md)
  A Boolean value that indicates whether the receiver accepts the glyph info attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/dragimageforselection(with:origin:))*