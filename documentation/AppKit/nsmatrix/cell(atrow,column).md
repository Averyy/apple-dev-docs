# cell(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the cell at the specified row and column.

**Availability**:
- macOS

## Declaration

```swift
func cell(atRow row: Int, column col: Int) -> NSCell?
```

```objc
- (NSCell *) cellAtRow:(NSInteger) row column:(NSInteger) col;
```

## Return Value

The [`NSCell`](../nscell.md) object at the specified row and column location specified, or `nil` if either `row` or `column` is outside the bounds of the receiver.

## Parameters

- `row`: The number of the row containing the cell to return.
- `col`: The number of the column containing the cell to return.

## See Also

### Related Documentation
- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, of: NSCell) -> Bool](./getrow%28_,column,of%29.md)
  Searches the receiver for the specified cell and returns the row and column of the cell
### Finding Cells
- [var selectedCells: [NSCell]](./selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](./selectedrow.md)
  The row number of the selected cell.
- [func cell(withTag: Int) -> NSCell?](./cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](./cells.md)
  An array containing the cells of the matrix.
- [selectedCell](./selectedcell.md)
  The most recently selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cell(atrow:column:))*