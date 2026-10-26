# columnsInRect:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of the specified rectangle.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`columnIndexes(in:)`](./columnindexes%28in%29.md) instead.

## Declaration

```objc
- (NSRange) columnsInRect:(NSRect) rect;
```

#### Return Value

A range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of `aRect`. If the width or height of `aRect` is `0`, returns an `NSRange` whose length is `0`.

#### Discussion

The location of the range is the first such column’s index, and the length is the number of columns that lie in `aRect`.

## Parameters

- `rect`: A rectangle in the coordinate system of the table view.

## See Also

### Related Documentation
- [func rows(in: NSRect) -> NSRange](./rows%28in%29.md)
  Returns a range of indexes for the rows that lie wholly or partially within the vertical boundaries of the specified rectangle.
### Deprecated methods
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
- [func focusedColumn() -> Int](./focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](./setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](./performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](./preparedcell%28atcolumn,row%29.md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.
- [- textShouldBeginEditing:](./textshouldbeginediting_.md)
  Queries the delegate to determine if the text should begin editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columnsinrect:)*