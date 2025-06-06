# tableView(_:willDisplayCell:for:row:)

**Framework**: Appkit  
**Kind**: method

Tells the delegate that the table view will display the specified cell at the specified row and column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, willDisplayCell cell: Any, for tableColumn: NSTableColumn?, row: Int)
```

#### Discussion

The delegate can modify the display attributes of `aCell` to alter the appearance of the cell.

Because `aCell` is reused for every row in `aTableColumn`, the delegate must set the display attributes both when drawing special cells and when drawing standard cells.

> **Note**:  The implementation of this method must not draw portions of the cell. It should only alter the state of the passed-in cell.

## Parameters

- `tableView`: The table view that sent the message.
- `cell`: The cell to be displayed.
- `tableColumn`: The table column.
- `row`: The row index.

## See Also

- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](nstableviewdelegate/tableview(_:datacellfor:row:).md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, shouldShowCellExpansionFor: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldshowcellexpansionfor:row:).md)
  Asks the delegate if an expansion tooltip should be displayed for a specific row and column.
- [func tableView(NSTableView, toolTipFor: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String](nstableviewdelegate/tableview(_:tooltipfor:rect:tablecolumn:row:mouselocation:).md)
  Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:willdisplaycell:for:row:))*