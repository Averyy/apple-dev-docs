# tableView(_:rowActionsForRow:edge:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to provide an array of row actions to be attached to the specified edge of a table row and displayed when the user swipes horizontally across the row.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, rowActionsForRow row: Int, edge: NSTableView.RowActionEdge) -> [NSTableViewRowAction]
```

#### Return Value

An array of row actions (of class [`NSTableViewRowAction`](nstableviewrowaction.md)) to be enabled on the specified edge of the table row.

#### Discussion

Implement this method if your table row supports actions that are displayed when the user swipes horizontally across the row. For example, your table view could use this method to implement a swipe left to delete function in your table rows. When called, this method receives the table view, the index of the row the user swiped, and an edge of type `NSTableRowActionEdge`. The method should return an array of any row actions of class [`NSTableViewRowAction`](nstableviewrowaction.md) that are supported for the specified edge. If no row actions are available, an empty array should be returned.

If this method isn’t implemented, then the table row displays no actions when the user swipes horizontally away from the specified edge.

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The index of the target row.
- `edge`: The edge (of class  ) for which row actions are requested. This is based on the direction in which the user swiped on the row. Swiping to the right results in an edge value of  . Swiping to the left results in an edge value of  .

## See Also

- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:rowactionsforrow:edge:))*