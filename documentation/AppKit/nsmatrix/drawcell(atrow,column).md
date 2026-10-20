# drawCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the cell at the specified row and column.

**Availability**:
- macOS

## Declaration

```swift
func drawCell(atRow row: Int, column col: Int)
```

```objc
- (void) drawCellAtRow:(NSInteger) row column:(NSInteger) col;
```

## Parameters

- `row`: The row containing the cell to draw.
- `col`: The column containing the cell to draw.

## See Also

### Related Documentation
- [func drawCell(NSCell)](../nscontrol/drawcell%28_%29.md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](../nscontrol/drawcellinside%28_%29.md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
### Displaying and Highlighting Cells
- [func highlightCell(Bool, atRow: Int, column: Int)](./highlightcell%28_,atrow,column%29.md)
  Highlights or unhighlights the cell at the specified row and column location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/drawcell(atrow:column:))*