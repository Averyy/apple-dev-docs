# trackMouse(with:in:of:atCharacterIndex:untilMouseUp:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Handles a mouse-down event on the image at the specified character position.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func trackMouse(with theEvent: NSEvent, in cellFrame: NSRect, of controlView: NSView?, atCharacterIndex charIndex: Int, untilMouseUp flag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the cell successfully finished tracking the mouse, or [`false`](https://developer.apple.com/documentation/swift/false) if tracking was unsuccessful.

#### Discussion

The [`NSTextAttachmentCell`](nstextattachmentcell-swift.class.md) implementation of this method calls upon `aTextView`’s delegate to handle the event. If `theEvent` is a mouse-up event for a double click, the text attachment cell calls the [`textView(_:doubleClickedOn:in:at:)`](nstextviewdelegate/textview(_:doubleclickedon:in:at:).md) method of its delegate and returns [`true`](https://developer.apple.com/documentation/swift/true). Otherwise, depending on whether the user clicks or drags the cell, it sends the delegate a [`textView(_:clickedOn:in:at:)`](nstextviewdelegate/textview(_:clickedon:in:at:).md): or a [`textView(_:draggedCell:in:event:at:)`](nstextviewdelegate/textview(_:draggedcell:in:event:at:).md) message and returns [`true`](https://developer.apple.com/documentation/swift/true). The [`NSTextAttachmentCell`](nstextattachmentcell-swift.class.md) implementation returns [`false`](https://developer.apple.com/documentation/swift/false) only if `flag` is [`false`](https://developer.apple.com/documentation/swift/false) and the mouse is dragged outside of `cellFrame`. The delegate methods are invoked only if the delegate responds.

## Parameters

- `theEvent`: The mouse-down event.
- `cellFrame`: The region of an   in which to track further mouse events.
- `controlView`: The view that received the event. Typically, this view is an   object and is focused.
- `charIndex`: The position in the text at which the attachment appears.
- `flag`: A Boolean value that indicates whether to track the mouse until a mouse-up event occurs. If this parameter is  , stop tracking when a mouse-dragged event occurs outside of  .

## See Also

- [func wantsToTrackMouse() -> Bool](nstextattachmentcellprotocol/wantstotrackmouse.md)
  Returns a Boolean value that indicates whether the attachment handles mouse events occurring over its image.
- [func wantsToTrackMouse(for: NSEvent, in: NSRect, of: NSView?, atCharacterIndex: Int) -> Bool](nstextattachmentcellprotocol/wantstotrackmouse(for:in:of:atcharacterindex:).md)
  Allows an attachment to specify the events for which it tracks the mouse.
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView?, untilMouseUp: Bool) -> Bool](nstextattachmentcellprotocol/trackmouse(with:in:of:untilmouseup:).md)
  Handles a mouse-down event on the cell’s image, and optionally waits until a mouse-up event


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcellprotocol/trackmouse(with:in:of:atcharacterindex:untilmouseup:))*