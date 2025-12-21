# isAutoscroll

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the receiver is automatically scrolled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isAutoscroll: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the matrix, if it is in a scrolling view, is automatically scrolled whenever the cursor is dragged outside the matrix after a mouse-down event within its bounds.

## See Also

- [func setScrollable(Bool)](nsmatrix/setscrollable(_:).md)
  Specifies whether the cells in the matrix are scrollable.
- [func scrollCellToVisible(atRow: Int, column: Int)](nsmatrix/scrollcelltovisible(atrow:column:).md)
  Scrolls the receiver so the specified cell is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/isautoscroll)*