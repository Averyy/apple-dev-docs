# acceptsGlyphInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver accepts the glyph info attribute.

**Availability**:
- macOS

## Declaration

```swift
var acceptsGlyphInfo: Bool { get set }
```

```objc
@property BOOL acceptsGlyphInfo;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver accepts the `NSGlyphInfoAttributeName` attribute from text input sources such as input methods and the pasteboard, [`false`](../../Swift/false.md) otherwise.

## See Also

### Dragging
- [func dragImageForSelection(with: NSEvent, origin: NSPointPointer?) -> NSImage?](./dragimageforselection%28with,origin%29.md)
  Returns an appropriate drag image for the drag initiated by the specified event.
- [func dragOperation(for: any NSDraggingInfo, type: NSPasteboard.PasteboardType) -> NSDragOperation](./dragoperation%28for,type%29.md)
  Returns the type of drag operation that should be performed if the image were released now.
- [func dragSelection(with: NSEvent, offset: NSSize, slideBack: Bool) -> Bool](./dragselection%28with,offset,slideback%29.md)
  Begins dragging the current selected text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/acceptsglyphinfo)*