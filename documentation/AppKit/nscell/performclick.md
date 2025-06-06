# performClick(_:)

**Framework**: AppKit  
**Kind**: method

Simulates a single mouse click on the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performClick(_ sender: Any?)
```

#### Discussion

This method performs the receiver’s action on its target. The receiver must be enabled to perform the action. If the receiver’s control view is valid, that view is used as the sender; otherwise, the value in `sender` is used.

The receiver of this message must be a cell of type `NSActionCell`. This method raises an exception if the action message cannot be successfully sent.

## Parameters

- `sender`: The object to use as the sender of the event (if the receiver’s control view is not valid). This object must be a subclass of  .

## See Also

- [var controlView: NSView?](nscell/controlview.md)
  The view associated with the cell.
- [var acceptsFirstResponder: Bool](nscell/acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var showsFirstResponder: Bool](nscell/showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [var refusesFirstResponder: Bool](nscell/refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/performclick(_:))*