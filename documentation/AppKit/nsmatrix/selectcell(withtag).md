# selectCell(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the last cell with the given tag.

**Availability**:
- macOS

## Declaration

```swift
func selectCell(withTag tag: Int) -> Bool
```

```objc
- (BOOL) selectCellWithTag:(NSInteger) tag;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver contains a cell whose tag matches `anInt`, or [`false`](../../Swift/false.md) if no such cell exists

## Discussion

If the matrix has at least one cell whose tag is equal to `anInt`, the last cell (when viewing the matrix as a row-ordered array) is selected. If the specified cell is an editable text cell, its text is selected.

## Parameters

- `tag`: The tag of the cell to select.

## See Also

### Related Documentation
- [func cell(withTag: Int) -> NSCell?](./cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.
- [func selectCell(NSCell)](../nscontrol/selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
### Selecting and Deselecting Cells
- [func selectCell(atRow: Int, column: Int)](./selectcell%28atrow,column%29.md)
  Selects the cell at the specified row and column within the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectcell(withtag:))*