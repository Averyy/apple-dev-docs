# selectedCells

**Framework**: AppKit  
**Kind**: property

An array containing all of the matrix’s highlighted cells plus its selected cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedCells: [NSCell] { get }
```

#### Discussion

See the class description for a discussion of the selected cell.

As an alternative to using [`setSelectionFrom(_:to:anchor:highlight:)`](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md) for programmatically making discontiguous selections of cells in a matrix, you could first set the single selected cell and then set subsequent cells to be highlighted; afterwards you can access [`selectedCells`](nsmatrix/selectedcells.md) to obtain the selection of cells.

## See Also

- [var isHighlighted: Bool](nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.
- [var selectedColumn: Int](nsmatrix/selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](nsmatrix/cell(atrow:column:).md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](nsmatrix/cell(withtag:).md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](nsmatrix/cells.md)
  An array containing the cells of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectedcells)*