# setScrollable(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies whether the cells in the matrix are scrollable.

**Availability**:
- macOS

## Declaration

```swift
func setScrollable(_ flag: Bool)
```

```objc
- (void) setScrollable:(BOOL) flag;
```

## Parameters

- `flag`: [`true`](../../Swift/true.md) to make all the cells in the receiver scrollable, so the text they contain scrolls to remain in view if the user types past the edge of the cell. If `flag` is [`false`](../../Swift/false.md), all cells are made nonscrolling. The prototype cell, if there is one, is also set accordingly

## See Also

### Related Documentation
- [var isScrollable: Bool](../nscell/isscrollable.md)
  A Boolean value indicating whether excess text scrolls past the cell’s bounds.
- [var prototype: NSCell?](./prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.
### Scrolling Cells in the Matrix
- [var isAutoscroll: Bool](./isautoscroll.md)
  A Boolean that indicates whether the receiver is automatically scrolled.
- [func scrollCellToVisible(atRow: Int, column: Int)](./scrollcelltovisible%28atrow,column%29.md)
  Scrolls the receiver so the specified cell is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setscrollable(_:))*