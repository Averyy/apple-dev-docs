# doubleAction

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The action sent to the target of the receiver when the user double-clicks a cell.

**Availability**:
- macOS

## Declaration

```swift
var doubleAction: Selector? { get set }
```

```objc
@property (nullable) SEL doubleAction;
```

#### Discussion

The double-click action of an [`NSMatrix`](../nsmatrix.md) is sent after the appropriate single-click action (for the [`NSCell`](../nscell.md) clicked, or for the [`NSMatrix`](../nsmatrix.md) if the [`NSCell`](../nscell.md) doesn’t have its own action). If there is no double-click action and the [`NSMatrix`](../nsmatrix.md) doesn’t ignore multiple clicks, the single-click action is sent twice. If the value of this property is a non-`nil` selector, this property also sets `ignoresMultiClick` to [`false`](../../Swift/false.md); otherwise, it leaves `ignoresMultiClick` unchanged.

## See Also

### Related Documentation
- [var action: Selector?](../nscontrol/action.md)
  The default action-message selector associated with the control.
- [var ignoresMultiClick: Bool](../nscontrol/ignoresmulticlick.md)
  A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.
- [var target: AnyObject?](../nscontrol/target.md)
  The target object that receives action messages from the cell.
### Managing and Sending Action Messages
- [func sendAction() -> Bool](./sendaction%28%29.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [func sendAction(Selector, to: Any, forAllCells: Bool)](./sendaction%28_,to,forallcells%29.md)
  Iterates through the cells in the receiver, sending the specified selector to an object for each cell.
- [func sendDoubleAction()](./senddoubleaction%28%29.md)
  Sends the double-click action message to the target of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/doubleaction)*