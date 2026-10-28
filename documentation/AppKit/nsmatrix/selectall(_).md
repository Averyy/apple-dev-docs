# selectAll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects and highlights all cells in the receiver.

**Availability**:
- macOS

## Declaration

```swift
func selectAll(_ sender: Any?)
```

```objc
- (void) selectAll:(id) sender;
```

## Discussion

Editable text cells and disabled cells are not selected. The receiver is redisplayed.

If the selection mode is not [`NSMatrix.Mode.listModeMatrix`](./mode-swift.enum/listmodematrix.md), this method does nothing.

## Parameters

- `sender`: This argument is ignored.

## See Also

### Related Documentation
- [func selectCell(NSCell)](../nscontrol/selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
### Selecting and Deselecting Cells
- [func selectCell(atRow: Int, column: Int)](./selectcell%28atrow,column%29.md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](./selectcell%28withtag%29.md)
  Selects the last cell with the given tag.
- [var keyCell: NSCell?](./keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](./setselectionfrom%28_,to,anchor,highlight%29.md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](./deselectallcells%28%29.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](./deselectselectedcell%28%29.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectall(_:))*