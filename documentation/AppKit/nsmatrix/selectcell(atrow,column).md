# selectCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the cell at the specified row and column within the receiver.

**Availability**:
- macOS

## Declaration

```swift
func selectCell(atRow row: Int, column col: Int)
```

```objc
- (void) selectCellAtRow:(NSInteger) row column:(NSInteger) col;
```

#### Discussion

If the specified cell is an editable text cell, its text is selected. If either `row` or `column` is –1, then the current selection is cleared (unless the receiver is an `NSRadioModeMatrix` and doesn’t allow empty selection). This method redraws the affected cells.

## Parameters

- `row`: The row of the cell to select.
- `col`: The column of the cell to select.

## See Also

### Related Documentation
- [var mode: NSMatrix.Mode](./mode-swift.property.md)
  The selection mode of the receiver.
- [func selectCell(NSCell)](../nscontrol/selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
### Selecting and Deselecting Cells
- [func selectCell(withTag: Int) -> Bool](./selectcell%28withtag%29.md)
  Selects the last cell with the given tag.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects and highlights all cells in the receiver.
- [var keyCell: NSCell?](./keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](./setselectionfrom%28_,to,anchor,highlight%29.md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](./deselectallcells%28%29.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](./deselectselectedcell%28%29.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectcell(atrow:column:))*