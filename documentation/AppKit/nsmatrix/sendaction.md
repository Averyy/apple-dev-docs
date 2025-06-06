# sendAction()

**Framework**: AppKit  
**Kind**: method

If the selected cell has both an action and a target, sends its action to its target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an action was successfully sent to a target. If the selected cell is disabled, this method does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the cell has an action but no target, its action is sent to the target of the receiver. If the cell doesn’t have an action, or if there is no selected cell, the receiver sends its own action to its target.

## See Also

- [var action: Selector?](nscell/action.md)
  The action performed by the cell.
- [var target: AnyObject?](nscell/target.md)
  The object that receives the cell’s action messages.
- [func sendAction(Selector, to: Any, forAllCells: Bool)](nsmatrix/sendaction(_:to:forallcells:).md)
  Iterates through the cells in the receiver, sending the specified selector to an object for each cell.
- [var doubleAction: Selector?](nsmatrix/doubleaction.md)
  The action sent to the target of the receiver when the user double-clicks a cell.
- [func sendDoubleAction()](nsmatrix/senddoubleaction.md)
  Sends the double-click action message to the target of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sendaction())*