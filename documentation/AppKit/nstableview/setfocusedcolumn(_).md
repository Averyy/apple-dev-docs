# setFocusedColumn(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the currently focused column to the specified index.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use a view-based table view and make a particular view the first responder to focus it.

## Declaration

```swift
func setFocusedColumn(_ focusedColumn: Int)
```

```objc
- (void) setFocusedColumn:(NSInteger) focusedColumn;
```

#### Discussion

This method will redisplay the previously focused column and (if required) the new `focusedColumn`.

The focused column has a focus ring drawn around the [`selectedRow`](./selectedrow.md) that intersects with `focusedColumn`.

You should not override this method.

> **Note**:  This method is not applicable for [`NSView`](../nsview.md)-based table views.

## Parameters

- `focusedColumn`: The index of the column to focus, or -1 if there should be no focused column.

## See Also

### Deprecated methods
- [func focusedColumn() -> Int](./focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](./performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setfocusedcolumn(_:))*