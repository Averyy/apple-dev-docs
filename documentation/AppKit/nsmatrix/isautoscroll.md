# isAutoscroll

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the receiver is automatically scrolled.

**Availability**:
- macOS

## Declaration

```swift
var isAutoscroll: Bool { get set }
```

```objc
@property (getter=isAutoscroll) BOOL autoscroll;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the matrix, if it is in a scrolling view, is automatically scrolled whenever the cursor is dragged outside the matrix after a mouse-down event within its bounds.

## See Also

### Scrolling Cells in the Matrix
- [func setScrollable(Bool)](./setscrollable%28_%29.md)
  Specifies whether the cells in the matrix are scrollable.
- [func scrollCellToVisible(atRow: Int, column: Int)](./scrollcelltovisible%28atrow,column%29.md)
  Scrolls the receiver so the specified cell is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/isautoscroll)*