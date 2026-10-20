# keyCell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell that will be clicked when the user presses the Space bar.

**Availability**:
- macOS

## Declaration

```swift
var keyCell: NSCell? { get set }
```

```objc
@property (strong, nullable) NSCell * keyCell;
```

## See Also

### Related Documentation
- [var tabKeyTraversesCells: Bool](./tabkeytraversescells.md)
  A Boolean that indicates whether pressing the Tab key advances the key cell to the next selectable cell.
### Selecting and Deselecting Cells
- [func selectCell(atRow: Int, column: Int)](./selectcell%28atrow,column%29.md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](./selectcell%28withtag%29.md)
  Selects the last cell with the given tag.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects and highlights all cells in the receiver.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](./setselectionfrom%28_,to,anchor,highlight%29.md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](./deselectallcells%28%29.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](./deselectselectedcell%28%29.md)
  Deselects the selected cell or cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/keycell)*