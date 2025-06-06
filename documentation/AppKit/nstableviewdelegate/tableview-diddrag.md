# tableView(_:didDrag:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the specified table column was dragged.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didDrag tableColumn: NSTableColumn)
```

#### Discussion

Specifically, this method is sent when the mouse button goes up in `tableView` and `tableColumn` has been dragged during the time the mouse button was down. In macOS 10.5 and later the dragged column is sent to the delegate. (In earlier versions of macOS the table column that’s currently located at the dragged column’s original index is sent.)

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.

## See Also

- [func tableView(NSTableView, shouldReorderColumn: Int, toColumn: Int) -> Bool](nstableviewdelegate/tableview(_:shouldreordercolumn:tocolumn:).md)
  Asks the delegate to allow or prohibit the specified column to be dragged to a new location.
- [func tableViewColumnDidMove(Notification)](nstableviewdelegate/tableviewcolumndidmove(_:).md)
  Tells the delegate that a table column was moved by user action.
- [func tableViewColumnDidResize(Notification)](nstableviewdelegate/tableviewcolumndidresize(_:).md)
  Tells the delegate that a table column was resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:diddrag:))*