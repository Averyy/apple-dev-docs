# isContinuous

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isContinuous: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the action message is sent continuously; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [func sendAction(Selector?, to: Any?) -> Bool](nscontrol/sendaction(_:to:).md)
  Causes the specified action to be sent to the target.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/iscontinuous)*