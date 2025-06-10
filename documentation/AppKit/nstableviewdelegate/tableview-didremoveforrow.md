# tableView(_:didRemove:forRow:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that a row view was removed from the table at the specified row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didRemove rowView: NSTableRowView, forRow row: Int)
```

#### Discussion

If `row` equals `-1`, the row is being deleted from the table and is no longer a valid row; otherwise `row` is a valid row that is being removed by being moved off screen.

> **Note**:  This method is only valid for [`NSView`](nsview.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `rowView`: The row view.
- `row`: The index of the row.

## See Also

- [func tableView(NSTableView, didAdd: NSTableRowView, forRow: Int)](nstableviewdelegate/tableview(_:didadd:forrow:).md)
  Tells the delegate that a row view was added at the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:didremove:forrow:))*