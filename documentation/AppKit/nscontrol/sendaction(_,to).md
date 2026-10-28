# sendAction(_:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the specified action to be sent to the target.

**Availability**:
- macOS

## Declaration

```swift
func sendAction(_ action: Selector?, to target: Any?) -> Bool
```

```objc
- (BOOL) sendAction:(SEL) action to:(id) target;
```

## Return Value

[`true`](../../Swift/true.md) if the message was successfully sent; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method uses the [`sendAction(_:to:from:)`](../nsapplication/sendaction%28_,to,from%29.md) method of `NSApplication` to invoke the specified method on an object. The receiver is passed as the parameter to the action message. This method is invoked primarily by the  [`trackMouse(with:in:of:untilMouseUp:)`](../nscell/trackmouse%28with,in,of,untilmouseup%29.md) method of `NSCell`.

## Parameters

- `action`: The selector to invoke on the target. If the selector is `NULL`, no message is sent.
- `target`: The target object to receive the message. If the object is `nil`, the application searches the responder chain for an object capable of handling the message. For more information on dispatching actions, see the class description for [`NSActionCell`](../nsactioncell.md).

## See Also

### Implementing the Target-Action Mechanism
- [var action: Selector?](./action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](./target.md)
  The target object that receives action messages from the cell.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sendaction(_:to:))*