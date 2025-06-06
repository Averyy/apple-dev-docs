# isContinuous

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isContinuous: Bool { get set }
```

#### Discussion

When the value of this property is YES, the cell’s action message is sent continuously during mouse tracking. In practice, the continuous delivery of action messages has meaning only for [`NSActionCell`](nsactioncell.md) and its subclasses, which implement the target/action mechanism. Some [`NSControl`](nscontrol.md) subclasses, notably [`NSMatrix`](nsmatrix.md), send a default action to a default target when a cell doesn’t provide a target or action.

## See Also

- [var action: Selector?](nscell/action.md)
  The action performed by the cell.
- [var target: AnyObject?](nscell/target.md)
  The object that receives the cell’s action messages.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscell/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/iscontinuous)*