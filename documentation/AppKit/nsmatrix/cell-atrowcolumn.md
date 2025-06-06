# cell(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Returns the cell at the specified row and column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cell(atRow row: Int, column col: Int) -> NSCell?
```

#### Return Value

The [`NSCell`](nscell.md) object at the specified row and column location specified, or `nil` if either `row` or `column` is outside the bounds of the receiver.

## Parameters

- `row`: The number of the row containing the cell to return.
- `col`: The number of the column containing the cell to return.

## See Also

- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, of: NSCell) -> Bool](nsmatrix/getrow(_:column:of:).md)
  Searches the receiver for the specified cell and returns the row and column of the cell
- [var selectedCells: [NSCell]](nsmatrix/selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](nsmatrix/selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(withTag: Int) -> NSCell?](nsmatrix/cell(withtag:).md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](nsmatrix/cells.md)
  An array containing the cells of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cell(atrow:column:))*