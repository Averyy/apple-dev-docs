# sendAction(on:)

**Framework**: AppKit  
**Kind**: method

Sets the conditions on which the receiver sends action messages to its target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction(on mask: NSEvent.EventTypeMask) -> Int
```

#### Return Value

A bit mask containing the previous settings. This bit mask uses the same values as specified in the `mask` parameter.

#### Discussion

You use this method during mouse tracking when the mouse button changes state, the mouse moves, or if the cell is marked to send its action continuously while tracking. Because of this, the only bits checked in `mask` are `NSLeftMouseDownMask`, `NSLeftMouseUpMask`, `NSLeftMouseDraggedMask`, and `NSPeriodicMask`, which are declared in the [`NSEvent`](nsevent.md) class reference.

The default implementation of this method simply invokes the [`sendAction(on:)`](nscell/sendaction(on:).md) method of its associated cell.

## Parameters

- `mask`: A bit mask containing the conditions for sending the action. The only conditions that are actually checked are associated with the  ,   ,  , and   bits.

## See Also

- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscell/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.
- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(Selector?, to: Any?) -> Bool](nscontrol/sendaction(_:to:).md)
  Causes the specified action to be sent to the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sendaction(on:))*