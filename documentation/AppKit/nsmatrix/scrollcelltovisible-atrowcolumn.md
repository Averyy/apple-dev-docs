# scrollCellToVisible(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Scrolls the receiver so the specified cell is visible.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func scrollCellToVisible(atRow row: Int, column col: Int)
```

#### Discussion

This method scrolls if the receiver is in a scrolling view and `row` and `column` represent a valid cell within the receiver.

## Parameters

- `row`: The row of the cell to make visible.
- `col`: The column of the cell to make visible.

## See Also

- [func scrollToVisible(NSRect) -> Bool](nsview/scrolltovisible(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object the minimum distance needed so a specified region of the view becomes visible in the clip view.
- [var isAutoscroll: Bool](nsmatrix/isautoscroll.md)
  A Boolean that indicates whether the receiver is automatically scrolled.
- [func setScrollable(Bool)](nsmatrix/setscrollable(_:).md)
  Specifies whether the cells in the matrix are scrollable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/scrollcelltovisible(atrow:column:))*