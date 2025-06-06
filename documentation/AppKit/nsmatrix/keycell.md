# keyCell

**Framework**: AppKit  
**Kind**: property

The cell that will be clicked when the user presses the Space bar.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var keyCell: NSCell? { get set }
```

## See Also

- [var tabKeyTraversesCells: Bool](nsmatrix/tabkeytraversescells.md)
  A Boolean that indicates whether pressing the Tab key advances the key cell to the next selectable cell.
- [func selectCell(atRow: Int, column: Int)](nsmatrix/selectcell(atrow:column:).md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](nsmatrix/selectcell(withtag:).md)
  Selects the last cell with the given tag.
- [func selectAll(Any?)](nsmatrix/selectall(_:).md)
  Selects and highlights all cells in the receiver.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](nsmatrix/deselectallcells.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](nsmatrix/deselectselectedcell.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/keycell)*