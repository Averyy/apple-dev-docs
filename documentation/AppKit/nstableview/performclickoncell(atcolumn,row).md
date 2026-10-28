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

## Discussion

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
- [- dragImageForRows:event:dragImageOffset:](./dragimageforrows_event_dragimageoffset_.md)
  Computes and returns an image to use for dragging.
- [- setAutoresizesAllColumnsToFit:](./setautoresizesallcolumnstofit_.md)
  Controls whether the table view proportionally resizes its columns to fit when its superview’s frame changes.
- [- autoresizesAllColumnsToFit](./autoresizesallcolumnstofit.md)
  Returns a Boolean value that indicates if the table view proportionally resizes its columns to fit when its superview’s frame changes.
- [- selectColumn:byExtendingSelection:](./selectcolumn_byextendingselection_.md)
  Selects the column at the specified index, optionally extending any existing selection.
- [- selectRow:byExtendingSelection:](./selectrow_byextendingselection_.md)
  Selects a row at the specified index, optionally extending any existing selection.
- [- setDrawsGrid:](./setdrawsgrid_.md)
  Sets whether the table view draws a grid.
- [- drawsGrid](./drawsgrid.md)
  Returns a Boolean value that indicates whether the table view draws a grid.
- [- selectedColumnEnumerator](./selectedcolumnenumerator.md)
  This method has been deprecated.
- [- selectedRowEnumerator](./selectedrowenumerator.md)
  This method has been deprecated.
- [- columnsInRect:](./columnsinrect_.md)
  Returns a range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of the specified rectangle.
- [- textShouldBeginEditing:](./textshouldbeginediting_.md)
  Queries the delegate to determine if the text should begin editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/performclickoncell(atcolumn:row:))*