# outlineView(_:dataCellFor:item:)

**Framework**: AppKit  
**Kind**: method

Returns the cell to use in a given column for a given item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, dataCellFor tableColumn: NSTableColumn?, item: Any) -> NSCell?
```

#### Return Value

The cell to use in column `tableColumn` for item `item`, or `nil`. Because the outline view might copy the cell, the cell must properly implement [`copyWithZone:`](https://developer.apple.com/documentation/objectivec/nsobject/1571953-copywithzone).

#### Discussion

You can return a different data cell for any table column and item combination. Alternatively, you can return a full-width cell for the entire row.

If `tableColumn` is non-`nil`, you can return a cell. In most cases, however, you default to returning the result from [`tableView(_:dataCellFor:row:)`](nstableviewdelegate/tableview(_:datacellfor:row:).md).

At the time of drawing, the outline view calls each row identified by `item` with a `nil` value for `tableColumn`. At this point, you can return a cell that the system can use to draw the entire row, acting as a group.

If you return a cell for the `nil` table column, prepare the other corresponding data source implementations and delegate methods to accept a `nil` value for `tableColumn`. If you don’t return a cell for the `nil` table column, the outline view calls this method once for each column, as usual.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column that requires the cell. This value can be  .
- `item`: The item that requires the cell.

## See Also

- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplaycell:for:item:).md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, willDisplayOutlineCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplayoutlinecell:for:item:).md)
  Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.
- [func outlineView(NSOutlineView, shouldShowOutlineCellForItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowoutlinecellforitem:).md)
  Returns whether the specified item should display the outline cell (the disclosure triangle).
- [func outlineView(NSOutlineView, shouldShowCellExpansionFor: NSTableColumn?, item: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowcellexpansionfor:item:).md)
  Invoked to allow the delegate to control cell expansion for a specific column and item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:datacellfor:item:))*