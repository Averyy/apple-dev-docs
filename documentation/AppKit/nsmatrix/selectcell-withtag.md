# selectCell(withTag:)

**Framework**: AppKit  
**Kind**: method

Selects the last cell with the given tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectCell(withTag tag: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver contains a cell whose tag matches `anInt`, or [`false`](https://developer.apple.com/documentation/Swift/false) if no such cell exists

#### Discussion

If the matrix has at least one cell whose tag is equal to `anInt`, the last cell (when viewing the matrix as a row-ordered array) is selected. If the specified cell is an editable text cell, its text is selected.

## Parameters

- `tag`: The tag of the cell to select.

## See Also

- [func cell(withTag: Int) -> NSCell?](nsmatrix/cell(withtag:).md)
  Searches the receiver and returns the last cell matching the specified tag.
- [func selectCell(NSCell)](nscontrol/selectcell(_:).md)
  Selects the specified cell and redraws the control as needed.
- [func selectCell(atRow: Int, column: Int)](nsmatrix/selectcell(atrow:column:).md)
  Selects the cell at the specified row and column within the receiver.
- [func selectAll(Any?)](nsmatrix/selectall(_:).md)
  Selects and highlights all cells in the receiver.
- [var keyCell: NSCell?](nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](nsmatrix/deselectallcells.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](nsmatrix/deselectselectedcell.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectcell(withtag:))*