# highlightCell(_:atRow:column:)

**Framework**: AppKit  
**Kind**: method

Highlights or unhighlights the cell at the specified row and column location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlightCell(_ flag: Bool, atRow row: Int, column col: Int)
```

## Parameters

- `flag`:   to highlight the cell;   to unhighlight the cell.
- `row`: The row containing the cell.
- `col`: The column containing the cell.

## See Also

- [func drawCell(atRow: Int, column: Int)](nsmatrix/drawcell(atrow:column:).md)
  Displays the cell at the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/highlightcell(_:atrow:column:))*