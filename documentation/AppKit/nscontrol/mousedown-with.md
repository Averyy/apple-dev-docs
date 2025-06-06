# mouseDown(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has pressed the left mouse button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func mouseDown(with event: NSEvent)
```

#### Discussion

Invoked when the mouse button is pressed while the cursor is within the bounds of the receiver, generating `theEvent`. This method highlights the receiver’s cell and sends it a [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) message. Whenever the cell finishes tracking the mouse (for example, because the cursor has left the cell’s bounds), the cell is unhighlighted. If the mouse button is still down and the cursor reenters the bounds, the cell is again highlighted and a new [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) message is sent. This behavior repeats until the mouse button goes up. If it goes up with the cursor in the control, the state of the control is changed, and the action message is sent to the target. If the mouse button goes up when the cursor is outside the control, no action message is sent.

## Parameters

- `event`: The event resulting from the user action.

## See Also

- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](nscell/trackmouse(with:in:of:untilmouseup:).md)
  Initiates the mouse tracking behavior in a cell.
- [var ignoresMultiClick: Bool](nscontrol/ignoresmulticlick.md)
  A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/mousedown(with:))*