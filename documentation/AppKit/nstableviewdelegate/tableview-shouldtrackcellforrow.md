# tableView(_:shouldTrackCell:for:row:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether the specified cell should be tracked.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldTrackCell cell: NSCell, for tableColumn: NSTableColumn?, row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the cell should be tracked, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

In general, only selectable or selected cells can be tracked. If you implement this method, cells that aren’t selectable or selected can be tracked; similarly, cells that are selectable or selected can be set as untracked.

For example, this allows you to have an [`NSButtonCell`](nsbuttoncell.md) object in a table that doesn’t change the selection, but can still be clicked on and tracked.

> **Note**:  This method is only valid for [`NSCell`](nscell.md)-based table views.

 This method is only valid for [`NSCell`](nscell.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `cell`: The cell to track.
- `tableColumn`: The table column.
- `row`: A row in  .

## See Also

- [func tableView(NSTableView, didClick: NSTableColumn)](nstableviewdelegate/tableview(_:didclick:).md)
  Tells the delegate that the mouse button was clicked in the specified table column, but the column was not dragged.
- [func tableView(NSTableView, mouseDownInHeaderOf: NSTableColumn)](nstableviewdelegate/tableview(_:mousedowninheaderof:).md)
  Tells the delegate that the mouse button was clicked in the specified table column’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldtrackcell:for:row:))*