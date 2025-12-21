# sendAction(_:to:)

**Framework**: AppKit  
**Kind**: method

Causes the specified action to be sent to the target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction(_ action: Selector?, to target: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the message was successfully sent; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method uses the [`sendAction(_:to:from:)`](nsapplication/sendaction(_:to:from:).md) method of `NSApplication` to invoke the specified method on an object. The receiver is passed as the parameter to the action message. This method is invoked primarily by the  [`trackMouse(with:in:of:untilMouseUp:)`](nscell/trackmouse(with:in:of:untilmouseup:).md) method of `NSCell`.

## Parameters

- `action`: The selector to invoke on the target. If the selector is  , no message is sent.
- `target`: The target object to receive the message. If the object is  , the application searches the responder chain for an object capable of handling the message. For more information on dispatching actions, see the class description for  .

## See Also

- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sendaction(_:to:))*