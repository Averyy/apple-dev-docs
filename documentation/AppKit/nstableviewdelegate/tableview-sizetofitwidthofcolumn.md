# tableView(_:sizeToFitWidthOfColumn:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, sizeToFitWidthOfColumn column: Int) -> CGFloat
```

#### Return Value

The width of the specified column.

#### Discussion

By default, [`NSTableView`](nstableview.md) iterates every row in the table, accesses a cell via [`preparedCell(atColumn:row:)`](nstableview/preparedcell(atcolumn:row:).md), and requests the [`cellSize`](nscell/cellsize.md) to find the appropriate largest width to use.

For accurate results and performance, it’s recommended that this method is implemented when using large tables. By default, large tables use a Monte Carlo simulation instead of iterating every row.

## Parameters

- `tableView`: The table view that sent the message.
- `column`: The index of the column.

## See Also

- [func tableView(NSTableView, heightOfRow: Int) -> CGFloat](nstableviewdelegate/tableview(_:heightofrow:).md)
  Asks the delegate for the height of the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:sizetofitwidthofcolumn:))*