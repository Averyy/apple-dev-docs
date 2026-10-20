# performClickOnCell(atColumn:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a click action on the cell at the specified row and column.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use a view-based table view and use the view to handle user interactions.

## Declaration

```swift
func performClickOnCell(atColumn column: Int, row: Int)
```

```objc
- (void) performClickOnCellAtColumn:(NSInteger) column row:(NSInteger) row;
```

#### Discussion

Acquires the [`NSTableView`](../nstableview.md), copies it, invokes [`performClick(_:)`](../nscell/performclick%28_%29.md) or [`performClick(withFrame:in:)`](../nspopupbuttoncell/performclick%28withframe,in%29.md) (if the cell is an [`NSPopUpButtonCell`](../nspopupbuttoncell.md)), and then updates the data source, if required. This method does not do any checks to see if the cell is enabled.

> **Note**:  This method is only available to [`NSCell`](../nscell.md)-based table views.

## Parameters

- `column`: The column of the cell.
- `row`: The row of the cell.

## See Also

### Deprecated methods
- [func focusedColumn() -> Int](./focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](./setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](./preparedcell%28atcolumn,row%29.md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/performclickoncell(atcolumn:row:))*