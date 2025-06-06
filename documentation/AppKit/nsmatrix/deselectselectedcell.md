# deselectSelectedCell()

**Framework**: AppKit  
**Kind**: method

Deselects the selected cell or cells.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deselectSelectedCell()
```

#### Discussion

If the selection mode is `NSRadioModeMatrix` and empty selection is not allowed, or if nothing is currently selected, this method does nothing. This method doesn’t redisplay the receiver.

## See Also

- [var mode: NSMatrix.Mode](nsmatrix/mode-swift.property.md)
  The selection mode of the receiver.
- [var allowsEmptySelection: Bool](nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
- [func selectCell(atRow: Int, column: Int)](nsmatrix/selectcell(atrow:column:).md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](nsmatrix/selectcell(withtag:).md)
  Selects the last cell with the given tag.
- [func selectAll(Any?)](nsmatrix/selectall(_:).md)
  Selects and highlights all cells in the receiver.
- [var keyCell: NSCell?](nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](nsmatrix/deselectallcells.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/deselectselectedcell())*