# setScrollable(_:)

**Framework**: AppKit  
**Kind**: method

Specifies whether the cells in the matrix are scrollable.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setScrollable(_ flag: Bool)
```

## Parameters

- `flag`:   to make all the cells in the receiver scrollable, so the text they contain scrolls to remain in view if the user types past the edge of the cell. If   is  , all cells are made nonscrolling. The prototype cell, if there is one, is also set accordingly

## See Also

- [var isScrollable: Bool](nscell/isscrollable.md)
  A Boolean value indicating whether excess text scrolls past the cell’s bounds.
- [var prototype: NSCell?](nsmatrix/prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.
- [var isAutoscroll: Bool](nsmatrix/isautoscroll.md)
  A Boolean that indicates whether the receiver is automatically scrolled.
- [func scrollCellToVisible(atRow: Int, column: Int)](nsmatrix/scrollcelltovisible(atrow:column:).md)
  Scrolls the receiver so the specified cell is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setscrollable(_:))*