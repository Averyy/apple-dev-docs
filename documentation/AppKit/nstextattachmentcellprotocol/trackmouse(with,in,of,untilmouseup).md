# trackMouse(with:in:of:untilMouseUp:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func trackMouse(with theEvent: NSEvent, in cellFrame: NSRect, of controlView: NSView?, untilMouseUp flag: Bool) -> Bool
```

```objc
- (BOOL) trackMouse:(NSEvent *) theEvent inRect:(NSRect) cellFrame ofView:(NSView *) controlView untilMouseUp:(BOOL) flag;
```

#### Return Value

[`true`](../../Swift/true.md) if the cell successfully finished tracking the mouse, or [`false`](../../Swift/false.md) if tracking was unsuccessful.

#### Discussion

The [`NSTextAttachmentCell`](../nstextattachmentcell-swift.class.md) implementation of this method calls upon `aTextView`’s delegate to handle the event. If `theEvent` is a mouse-up event for a double click, the text attachment cell calls the [`textView(_:doubleClickedOn:in:at:)`](../nstextviewdelegate/textview%28_,doubleclickedon,in,at%29.md) method of its delegate and returns [`true`](../../Swift/true.md). Otherwise, depending on whether the user clicks or drags the cell, it sends the delegate a [`textView(_:clickedOn:in:at:)`](../nstextviewdelegate/textview%28_,clickedon,in,at%29.md): or a [`textView(_:draggedCell:in:event:at:)`](../nstextviewdelegate/textview%28_,draggedcell,in,event,at%29.md) message and returns [`true`](../../Swift/true.md). The [`NSTextAttachmentCell`](../nstextattachmentcell-swift.class.md) implementation returns [`false`](../../Swift/false.md) only if `flag` is [`false`](../../Swift/false.md) and the mouse is dragged outside of `cellFrame`. The delegate methods are invoked only if the delegate responds.

## Parameters

- `theEvent`: The mouse-down event.
- `cellFrame`: The region of an [`NSTextView`](../nstextview.md) in which to track further mouse events.
- `controlView`: The view that received the event. Typically, this view is an [`NSTextView`](../nstextview.md) object and is focused.
- `flag`: A Boolean value that indicates whether to track the mouse until a mouse-up event occurs. If this parameter is [`false`](../../Swift/false.md), stop tracking when a mouse-dragged event occurs outside of `cellFrame`.

## See Also

### Related Documentation
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](../nscell/trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func lockFocus()](../nsview/lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
### Responding to mouse events
- [func wantsToTrackMouse() -> Bool](./wantstotrackmouse%28%29.md)
  Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.
- [func wantsToTrackMouse(for: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int) -> Bool](./wantstotrackmouse%28for,in,of,atcharacterindex%29.md)
  Allows an attachment to specify the events for which it tracks the mouse.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int, untilMouseUp: Bool) -> Bool](./trackmouse%28with,in,of,atcharacterindex,untilmouseup%29.md)
  Handles a mouse-down event on the image at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/trackmouse(with:in:of:untilmouseup:))*