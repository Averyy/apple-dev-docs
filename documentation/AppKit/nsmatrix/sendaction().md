# sendAction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

If the selected cell has both an action and a target, sends its action to its target.

**Availability**:
- macOS

## Declaration

```swift
func sendAction() -> Bool
```

```objc
- (BOOL) sendAction;
```

#### Return Value

[`true`](../../Swift/true.md) if an action was successfully sent to a target. If the selected cell is disabled, this method does nothing and returns [`false`](../../Swift/false.md).

#### Discussion

If the cell has an action but no target, its action is sent to the target of the receiver. If the cell doesn’t have an action, or if there is no selected cell, the receiver sends its own action to its target.

## See Also

### Related Documentation
- [var action: Selector?](../nscell/action.md)
  The action performed by the cell.
- [var target: AnyObject?](../nscell/target.md)
  The object that receives the cell’s action messages.
### Managing and Sending Action Messages
- [func sendAction(Selector, to: Any, forAllCells: Bool)](./sendaction%28_,to,forallcells%29.md)
  Iterates through the cells in the receiver, sending the specified selector to an object for each cell.
- [var doubleAction: Selector?](./doubleaction.md)
  The action sent to the target of the receiver when the user double-clicks a cell.
- [func sendDoubleAction()](./senddoubleaction%28%29.md)
  Sends the double-click action message to the target of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sendaction())*