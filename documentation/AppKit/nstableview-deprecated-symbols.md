# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func focusedColumn() -> Int](./nstableview/focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](./nstableview/setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./nstableview/shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](./nstableview/performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](./nstableview/preparedcell%28atcolumn,row%29.md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.
- [- dragImageForRows:event:dragImageOffset:](./nstableview/dragimageforrows_event_dragimageoffset_.md)
  Computes and returns an image to use for dragging.
- [- setAutoresizesAllColumnsToFit:](./nstableview/setautoresizesallcolumnstofit_.md)
  Controls whether the table view proportionally resizes its columns to fit when its superview’s frame changes.
- [- autoresizesAllColumnsToFit](./nstableview/autoresizesallcolumnstofit.md)
  Returns a Boolean value that indicates if the table view proportionally resizes its columns to fit when its superview’s frame changes.
- [- selectColumn:byExtendingSelection:](./nstableview/selectcolumn_byextendingselection_.md)
  Selects the column at the specified index, optionally extending any existing selection.
- [- selectRow:byExtendingSelection:](./nstableview/selectrow_byextendingselection_.md)
  Selects a row at the specified index, optionally extending any existing selection.
- [- setDrawsGrid:](./nstableview/setdrawsgrid_.md)
  Sets whether the table view draws a grid.
- [- drawsGrid](./nstableview/drawsgrid.md)
  Returns a Boolean value that indicates whether the table view draws a grid.
- [- selectedColumnEnumerator](./nstableview/selectedcolumnenumerator.md)
  This method has been deprecated.
- [- selectedRowEnumerator](./nstableview/selectedrowenumerator.md)
  This method has been deprecated.
- [- columnsInRect:](./nstableview/columnsinrect_.md)
  Returns a range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of the specified rectangle.
- [- textShouldBeginEditing:](./nstableview/textshouldbeginediting_.md)
  Queries the delegate to determine if the text should begin editing.
- [- textDidBeginEditing:](./nstableview/textdidbeginediting_.md)
  Posts an [`NSControlTextDidBeginEditingNotification`](./nscontrol/textdidbegineditingnotification.md) to the default notification center.
- [- textDidChange:](./nstableview/textdidchange_.md)
  Sends [`textDidChange:`](./nstableview/textdidchange_.md) to the edited cell and posts an [`NSControlTextDidChangeNotification`](./nscontrol/textdidchangenotification.md) to the default notification center.
- [- textShouldEndEditing:](./nstableview/textshouldendediting_.md)
  Validates the text object for the cell being edited by querying the delegate.queries the delegate using [`control:textShouldEndEditing:`](./nscontroltexteditingdelegate/control%28_,textshouldendediting%29.md), returning the delegate’s response if it responds to that method.
- [- textDidEndEditing:](./nstableview/textdidendediting_.md)
  Updates the data source based on the newly edited value and selects another cell for editing if possible according to the character that ended editing (Return, Tab, Backtab).

## See Also

### Deprecated
- [- tableView:writeRows:toPasteboard:](../ObjectiveC/nsobject-swift.class/tableview_writerows_topasteboard_.md)
  Writes the specified rows to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview-deprecated-symbols)*