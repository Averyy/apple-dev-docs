# acceptsGlyphInfo

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver accepts the glyph info attribute.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var acceptsGlyphInfo: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver accepts the `NSGlyphInfoAttributeName` attribute from text input sources such as input methods and the pasteboard, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](nstextview/dragimageforselection(with:origin:).md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragOperation(for: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation](nstextview/dragoperation(for:type:).md)
  Returns the type of drag operation that should be performed if the image were released now.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](nstextview/dragselection(with:offset:slideback:).md)
  Begins dragging the current selected text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/acceptsglyphinfo)*