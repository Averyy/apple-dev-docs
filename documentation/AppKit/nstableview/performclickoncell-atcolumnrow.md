# performClickOnCell(atColumn:row:)

**Framework**: Appkit  
**Kind**: method

Performs a click action on the cell at the specified row and column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func performClickOnCell(atColumn column: Int, row: Int)
```

#### Discussion

Acquires the [`NSTableView`](nstableview.md), copies it, invokes [`performClick(_:)`](nscell/performclick(_:).md) or [`performClick(withFrame:in:)`](nspopupbuttoncell/performclick(withframe:in:).md) (if the cell is an [`NSPopUpButtonCell`](nspopupbuttoncell.md)), and then updates the data source, if required. This method does not do any checks to see if the cell is enabled.

> **Note**:  This method is only available to [`NSCell`](nscell.md)-based table views.

## Parameters

- `column`: The column of the cell.
- `row`: The row of the cell.

## See Also

- [func focusedColumn() -> Int](nstableview/focusedcolumn.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](nstableview/setfocusedcolumn(_:).md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](nstableview/shouldfocuscell(_:atcolumn:row:).md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](nstableview/preparedcell(atcolumn:row:).md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/performclickoncell(atcolumn:row:))*