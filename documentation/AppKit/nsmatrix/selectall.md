# selectAll(_:)

**Framework**: AppKit  
**Kind**: method

Selects and highlights all cells in the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectAll(_ sender: Any?)
```

#### Discussion

Editable text cells and disabled cells are not selected. The receiver is redisplayed.

If the selection mode is not [`NSMatrix.Mode.listModeMatrix`](nsmatrix/mode-swift.enum/listmodematrix.md), this method does nothing.

## Parameters

- `sender`: This argument is ignored.

## See Also

- [func selectCell(NSCell)](nscontrol/selectcell(_:).md)
  Selects the specified cell and redraws the control as needed.
- [func selectCell(atRow: Int, column: Int)](nsmatrix/selectcell(atrow:column:).md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](nsmatrix/selectcell(withtag:).md)
  Selects the last cell with the given tag.
- [var keyCell: NSCell?](nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](nsmatrix/deselectallcells.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](nsmatrix/deselectselectedcell.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectall(_:))*