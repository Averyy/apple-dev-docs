# tableView(_:toolTipFor:rect:tableColumn:row:mouseLocation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, toolTipFor cell: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String
```

```objc
- (NSString *) tableView:(NSTableView *) tableView toolTipForCell:(NSCell *) cell rect:(NSRectPointer) rect tableColumn:(NSTableColumn *) tableColumn row:(NSInteger) row mouseLocation:(NSPoint) mouseLocation;
```

#### Return Value

A string that should be displayed in the tooltip. Return `nil` or the empty string if no tooltip is desired.

#### Discussion

By default, `rect` is computed as

`[cell drawingRectForBounds:cellFrame]`. Note that tooltips are also known as help tags.

## Parameters

- `tableView`: The table view that sent the message.
- `cell`: The cell.
- `rect`: The proposed active area of the tooltip. You can modify `rect` to provide an alternative active area.
- `tableColumn`: The table column.
- `row`: The row index.
- `mouseLocation`: The mouse location.

## See Also

### Providing cells for rows and columns
- [func tableView(NSTableView, willDisplayCell: Any, for: NSTableColumn?, row: Int)](./tableview%28_,willdisplaycell,for,row%29.md)
  Tells the delegate that the table view will display the specified cell at the specified row and column.
- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](./tableview%28_,datacellfor,row%29.md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, shouldShowCellExpansionFor: NSTableColumn?, row: Int) -> Bool](./tableview%28_,shouldshowcellexpansionfor,row%29.md)
  Asks the delegate if an expansion tooltip should be displayed for a specific row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:tooltipfor:rect:tablecolumn:row:mouselocation:))*