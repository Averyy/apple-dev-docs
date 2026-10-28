# isContinuous

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.

**Availability**:
- macOS

## Declaration

```swift
var isContinuous: Bool { get set }
```

```objc
@property (getter=isContinuous) BOOL continuous;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the action message is sent continuously; otherwise, [`false`](../../Swift/false.md).

## See Also

### Implementing the Target-Action Mechanism
- [var action: Selector?](./action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](./target.md)
  The target object that receives action messages from the cell.
- [func sendAction(Selector?, to: Any?) -> Bool](./sendaction%28_,to%29.md)
  Causes the specified action to be sent to the target.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/iscontinuous)*