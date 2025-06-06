# sendAction(_:to:forAllCells:)

**Framework**: AppKit  
**Kind**: method

Iterates through the cells in the receiver, sending the specified selector to an object for each cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction(_ selector: Selector, to object: Any, forAllCells flag: Bool)
```

#### Discussion

Iteration begins with the cell in the upper-left corner of the receiver, proceeding through the appropriate entries in the first row, then on to the next.

This method is not invoked to send action messages to target objects in response to mouse-down events in the receiver. Instead, you can invoke it if you want to have multiple cells in an [`NSMatrix`](nsmatrix.md) interact with an object. For example, you could use it to verify the titles in a list of items or to enable a series of radio buttons based on their purpose in relation to `anObject`.

## Parameters

- `selector`: The selector to send to the object for each cell. This must represent a method that takes a single argument: the id of the current cell in the iteration.  ’s return value must be a BOOL. If   returns   for any cell,   terminates immediately, without sending the message for the remaining cells. If it returns  ,   proceeds to the next cell.
- `object`: The object that is sent the selector for each cell in the matrix.
- `flag`:   if the method should iterate through all cells in the matrix;   if it should iterate through just the selected cells in the matrix.

## See Also

- [func sendAction() -> Bool](nsmatrix/sendaction.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [var doubleAction: Selector?](nsmatrix/doubleaction.md)
  The action sent to the target of the receiver when the user double-clicks a cell.
- [func sendDoubleAction()](nsmatrix/senddoubleaction.md)
  Sends the double-click action message to the target of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sendaction(_:to:forallcells:))*