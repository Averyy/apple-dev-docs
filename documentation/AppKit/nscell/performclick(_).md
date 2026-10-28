# performClick(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Simulates a single mouse click on the receiver.

**Availability**:
- macOS

## Declaration

```swift
func performClick(_ sender: Any?)
```

```objc
- (void) performClick:(id) sender;
```

## Discussion

This method performs the receiver’s action on its target. The receiver must be enabled to perform the action. If the receiver’s control view is valid, that view is used as the sender; otherwise, the value in `sender` is used.

The receiver of this message must be a cell of type `NSActionCell`. This method raises an exception if the action message cannot be successfully sent.

## Parameters

- `sender`: The object to use as the sender of the event (if the receiver’s control view is not valid). This object must be a subclass of `NSView`.

## See Also

### Related Documentation
- [var controlView: NSView?](./controlview.md)
  The view associated with the cell.
### Respond to Keyboard Events
- [var acceptsFirstResponder: Bool](./acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var showsFirstResponder: Bool](./showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [var refusesFirstResponder: Bool](./refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/performclick(_:))*