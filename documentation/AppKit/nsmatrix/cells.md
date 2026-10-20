# cells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the cells of the matrix.

**Availability**:
- macOS

## Declaration

```swift
var cells: [NSCell] { get }
```

```objc
@property (copy, readonly) NSArray<NSCell *> * cells;
```

#### Discussion

The cells in the array are row-ordered; that is, the first row of cells appears first in the array, followed by the second row, and so forth.

## See Also

### Finding Cells
- [var selectedCells: [NSCell]](./selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](./selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](./cell%28atrow,column%29.md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](./cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cells)*