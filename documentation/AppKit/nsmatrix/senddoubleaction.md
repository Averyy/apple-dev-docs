# sendDoubleAction()

**Framework**: AppKit  
**Kind**: method

Sends the double-click action message to the target of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendDoubleAction()
```

#### Discussion

If the receiver doesn’t have a double-click action, the double-click action message of the selected cell (as returned by [`selectedCell`](nsmatrix/selectedcell.md)) is sent to the selected cell’s target. Finally, if the selected cell also has no action, then the single-click action of the receiver is sent to the target of the receiver.

If the selected cell is disabled, this method does nothing.

Your code shouldn’t invoke this method; it’s sent in response to a double-click event in the [`NSMatrix`](nsmatrix.md). Override it if you need to change the search order for an action to send.

## See Also

- [var ignoresMultiClick: Bool](nscontrol/ignoresmulticlick.md)
  A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.
- [func sendAction() -> Bool](nsmatrix/sendaction.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [func sendAction(Selector, to: Any, forAllCells: Bool)](nsmatrix/sendaction(_:to:forallcells:).md)
  Iterates through the cells in the receiver, sending the specified selector to an object for each cell.
- [var doubleAction: Selector?](nsmatrix/doubleaction.md)
  The action sent to the target of the receiver when the user double-clicks a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/senddoubleaction())*