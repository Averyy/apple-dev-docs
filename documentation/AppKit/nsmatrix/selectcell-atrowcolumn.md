# selectCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Selects the cell at the specified row and column within the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectCell(atRow row: Int, column col: Int)
```

#### Discussion

If the specified cell is an editable text cell, its text is selected. If either `row` or `column` is –1, then the current selection is cleared (unless the receiver is an `NSRadioModeMatrix` and doesn’t allow empty selection). This method redraws the affected cells.

## Parameters

- `row`: The row of the cell to select.
- `col`: The column of the cell to select.

## See Also

- [var mode: NSMatrix.Mode](nsmatrix/mode-swift.property.md)
  The selection mode of the receiver.
- [func selectCell(NSCell)](nscontrol/selectcell(_:).md)
  Selects the specified cell and redraws the control as needed.
- [var allowsEmptySelection: Bool](nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
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
- [func deselectSelectedCell()](nsmatrix/deselectselectedcell.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectcell(atrow:column:))*