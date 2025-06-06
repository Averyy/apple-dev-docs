# tableView(_:toolTipFor:rect:tableColumn:row:mouseLocation:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, toolTipFor cell: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String
```

#### Return Value

A string that should be displayed in the tooltip. Return `nil` or the empty string if no tooltip is desired.

#### Discussion

By default, `rect` is computed as

`[cell drawingRectForBounds:cellFrame]`. Note that tooltips are also known as help tags.

## Parameters

- `tableView`: The table view that sent the message.
- `cell`: The cell.
- `rect`: The proposed active area of the tooltip. You can modify   to provide an alternative active area.
- `tableColumn`: The table column.
- `row`: The row index.
- `mouseLocation`: The mouse location.

## See Also

- [func tableView(NSTableView, willDisplayCell: Any, for: NSTableColumn?, row: Int)](nstableviewdelegate/tableview(_:willdisplaycell:for:row:).md)
  Tells the delegate that the table view will display the specified cell at the specified row and column.
- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](nstableviewdelegate/tableview(_:datacellfor:row:).md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, shouldShowCellExpansionFor: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldshowcellexpansionfor:row:).md)
  Asks the delegate if an expansion tooltip should be displayed for a specific row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:tooltipfor:rect:tablecolumn:row:mouselocation:))*