# highlightCell(_:atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Highlights or unhighlights the cell at the specified row and column location.

**Availability**:
- macOS

## Declaration

```swift
func highlightCell(_ flag: Bool, atRow row: Int, column col: Int)
```

```objc
- (void) highlightCell:(BOOL) flag atRow:(NSInteger) row column:(NSInteger) col;
```

## Parameters

- `flag`: [`true`](../../Swift/true.md) to highlight the cell; [`false`](../../Swift/false.md) to unhighlight the cell.
- `row`: The row containing the cell.
- `col`: The column containing the cell.

## See Also

### Displaying and Highlighting Cells
- [func drawCell(atRow: Int, column: Int)](./drawcell%28atrow,column%29.md)
  Displays the cell at the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/highlightcell(_:atrow:column:))*