# deselectSelectedCell()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deselects the selected cell or cells.

**Availability**:
- macOS

## Declaration

```swift
func deselectSelectedCell()
```

```objc
- (void) deselectSelectedCell;
```

## Discussion

If the selection mode is `NSRadioModeMatrix` and empty selection is not allowed, or if nothing is currently selected, this method does nothing. This method doesn’t redisplay the receiver.

## See Also

### Related Documentation
- [var mode: NSMatrix.Mode](./mode-swift.property.md)
  The selection mode of the receiver.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
### Selecting and Deselecting Cells
- [func selectCell(atRow: Int, column: Int)](./selectcell%28atrow,column%29.md)
  Selects the cell at the specified row and column within the receiver.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/deselectselectedcell())*