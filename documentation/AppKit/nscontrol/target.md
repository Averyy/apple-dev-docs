# target

**Framework**: AppKit  
**Kind**: property

The target object that receives action messages from the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

#### Discussion

When the value of this property is `nil`, the application follows the responder chain looking for an object that can respond to the message. See the description of the [`NSActionCell`](nsactioncell.md) class for details.

## See Also

- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(Selector?, to: Any?) -> Bool](nscontrol/sendaction(_:to:).md)
  Causes the specified action to be sent to the target.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/target)*