# drawCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Displays the cell at the specified row and column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawCell(atRow row: Int, column col: Int)
```

## Parameters

- `row`: The row containing the cell to draw.
- `col`: The column containing the cell to draw.

## See Also

- [func drawCell(NSCell)](nscontrol/drawcell(_:).md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](nscontrol/drawcellinside(_:).md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func highlightCell(Bool, atRow: Int, column: Int)](nsmatrix/highlightcell(_:atrow:column:).md)
  Highlights or unhighlights the cell at the specified row and column location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/drawcell(atrow:column:))*