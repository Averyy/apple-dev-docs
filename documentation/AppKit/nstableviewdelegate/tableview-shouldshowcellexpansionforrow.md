# tableView(_:shouldShowCellExpansionFor:row:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if an expansion tooltip should be displayed for a specific row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldShowCellExpansionFor tableColumn: NSTableColumn?, row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an expansion tooltip should be displayed, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

An expansion tooltip can be displayed when the pointer hovers over a cell that contains truncated text. When this method returns [`true`](https://developer.apple.com/documentation/swift/true), the cell’s full contents is shown in an expansion tooltip, which looks similar to a help tag.

> **Note**:  This method is only valid for [`NSCell`](nscell.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.
- `row`: The row index.

## See Also

- [func tableView(NSTableView, willDisplayCell: Any, for: NSTableColumn?, row: Int)](nstableviewdelegate/tableview(_:willdisplaycell:for:row:).md)
  Tells the delegate that the table view will display the specified cell at the specified row and column.
- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](nstableviewdelegate/tableview(_:datacellfor:row:).md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, toolTipFor: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String](nstableviewdelegate/tableview(_:tooltipfor:rect:tablecolumn:row:mouselocation:).md)
  Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldshowcellexpansionfor:row:))*