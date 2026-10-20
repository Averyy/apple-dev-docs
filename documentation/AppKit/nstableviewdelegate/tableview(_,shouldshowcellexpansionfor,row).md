# tableView(_:shouldShowCellExpansionFor:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if an expansion tooltip should be displayed for a specific row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldShowCellExpansionFor tableColumn: NSTableColumn?, row: Int) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView shouldShowCellExpansionForTableColumn:(NSTableColumn *) tableColumn row:(NSInteger) row;
```

#### Return Value

[`true`](../../Swift/true.md) if an expansion tooltip should be displayed, [`false`](../../Swift/false.md) otherwise.

#### Discussion

An expansion tooltip can be displayed when the pointer hovers over a cell that contains truncated text. When this method returns [`true`](../../Swift/true.md), the cell’s full contents is shown in an expansion tooltip, which looks similar to a help tag.

> **Note**:  This method is only valid for [`NSCell`](../nscell.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.
- `row`: The row index.

## See Also

### Providing cells for rows and columns
- [func tableView(NSTableView, willDisplayCell: Any, for: NSTableColumn?, row: Int)](./tableview%28_,willdisplaycell,for,row%29.md)
  Tells the delegate that the table view will display the specified cell at the specified row and column.
- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](./tableview%28_,datacellfor,row%29.md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, toolTipFor: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String](./tableview%28_,tooltipfor,rect,tablecolumn,row,mouselocation%29.md)
  Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldshowcellexpansionfor:row:))*