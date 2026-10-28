# dragImageForRows:event:dragImageOffset:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Computes and returns an image to use for dragging.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`dragImageForRows(with:tableColumns:event:offset:)`](./dragimageforrows%28with,tablecolumns,event,offset%29.md) instead.

## Declaration

```objc
- (NSImage *) dragImageForRows:(NSArray *) dragRows event:(NSEvent *) dragEvent dragImageOffset:(NSPointPointer) dragImageOffset;
```

## Discussion

Override this to return a custom image. `dragRows` represents the rows participating in the drag. `dragEvent` is a reference to the mouse-down event that began the drag. `dragImageOffset` is an in/out parameter.

This method is called with `dragImageOffset` set to `NSZeroPoint`, but it can be modified to reposition the returned image. A `dragImageOffset` of `NSZeroPoint` will cause the image to be centered under the cursor.

> **Note**:  To support multi-item drags, it is highly recommended to implement the delegate method [`tableView(_:pasteboardWriterForRow:)`](../nstableviewdatasource/tableview%28_,pasteboardwriterforrow%29.md) instead. Using that method will cause this method to not be called.

## See Also

### Deprecated methods
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
- [- columnsInRect:](./columnsinrect_.md)
  Returns a range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of the specified rectangle.
- [- textShouldBeginEditing:](./textshouldbeginediting_.md)
  Queries the delegate to determine if the text should begin editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/dragimageforrows:event:dragimageoffset:)*