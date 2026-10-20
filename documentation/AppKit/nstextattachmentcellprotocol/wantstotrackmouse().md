# wantsToTrackMouse()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func wantsToTrackMouse() -> Bool
```

```objc
- (BOOL) wantsToTrackMouse;
```

#### Discussion

The default implementation of this method returns [`true`](../../Swift/true.md). The [`NSView`](../nsview.md) containing the cell should invoke this method before sending a [`trackMouse(with:in:of:untilMouseUp:)`](./trackmouse%28with,in,of,untilmouseup%29.md) message.

For an attachment in an attributed string, if the attachment cell returns [`false`](../../Swift/false.md), its attachment character should be selected rather than the cell being asked to track the mouse. This results in the attachment icon behaving as any regular glyph in text.

## See Also

### Responding to mouse events
- [func wantsToTrackMouse(for: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int) -> Bool](./wantstotrackmouse%28for,in,of,atcharacterindex%29.md)
  Allows an attachment to specify the events for which it tracks the mouse.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,atcharacterindex,untilmouseup%29.md)
  Handles a mouse-down event on the image at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/wantstotrackmouse())*