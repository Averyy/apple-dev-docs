# tableView(_:didClick:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the mouse button was clicked in the specified table column, but the column was not dragged.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didClick tableColumn: NSTableColumn)
```

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.

## See Also

- [func tableView(NSTableView, mouseDownInHeaderOf: NSTableColumn)](nstableviewdelegate/tableview(_:mousedowninheaderof:).md)
  Tells the delegate that the mouse button was clicked in the specified table column’s header.
- [func tableView(NSTableView, shouldTrackCell: NSCell, for: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldtrackcell:for:row:).md)
  Asks the delegate whether the specified cell should be tracked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:didclick:))*