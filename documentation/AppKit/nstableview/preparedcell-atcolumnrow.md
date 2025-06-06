# preparedCell(atColumn:row:)

**Framework**: Appkit  
**Kind**: method

Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func preparedCell(atColumn column: Int, row: Int) -> NSCell?
```

#### Return Value

New [`NSCell`](nscell.md) subclass instance to use for the specified `row` and `column`. The value for the cell is correctly set, and the delegate method [`tableView(_:willDisplayCell:for:row:)`](nstableviewdelegate/tableview(_:willdisplaycell:for:row:).md) will have been called.

#### Discussion

You can override this method to do any additional cell set up that is required, or invoke it to retrieve a cell that has its contents configured for the specified `column` and `row`.

> **Note**:  This method is only available to [`NSCell`](nscell.md)-based table views.

## Parameters

- `column`: The index in the   array for which to return the appropriate cell.
- `row`: The row index for which to return the appropriate cell.

## See Also

- [func focusedColumn() -> Int](nstableview/focusedcolumn.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](nstableview/setfocusedcolumn(_:).md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](nstableview/shouldfocuscell(_:atcolumn:row:).md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](nstableview/performclickoncell(atcolumn:row:).md)
  Performs a click action on the cell at the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/preparedcell(atcolumn:row:))*