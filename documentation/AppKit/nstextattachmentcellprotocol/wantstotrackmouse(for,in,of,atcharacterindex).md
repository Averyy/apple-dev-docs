# wantsToTrackMouse(for:in:of:atCharacterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allows an attachment to specify the events for which it tracks the mouse.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func wantsToTrackMouse(for theEvent: NSEvent, in cellFrame: NSRect, of controlView: NSView?, atCharacterIndex charIndex: Int) -> Bool
```

```objc
- (BOOL) wantsToTrackMouseForEvent:(NSEvent *) theEvent inRect:(NSRect) cellFrame ofView:(NSView *) controlView atCharacterIndex:(NSUInteger) charIndex;
```

## Discussion

`theEvent` is the event in question that occurred in `cellFrame` inside `controlView`. `charIndex` is the index of the attachment character within the text. If [`wantsToTrackMouse()`](./wantstotrackmouse%28%29.md) returns [`true`](../../Swift/true.md), this method allows the attachment to decide whether it wishes to do so for particular events.

## See Also

### Responding to mouse events
- [func wantsToTrackMouse() -> Bool](./wantstotrackmouse%28%29.md)
  Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,untilmouseup%29.md)
  Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,atcharacterindex,untilmouseup%29.md)
  Handles a mouse-down event on the image at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/wantstotrackmouse(for:in:of:atcharacterindex:))*