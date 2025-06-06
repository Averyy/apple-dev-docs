# scrollRowToVisible(_:inColumn:)

**Framework**: AppKit  
**Kind**: method

Scrolls the specified row to be visible within the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func scrollRowToVisible(_ row: Int, inColumn column: Int)
```

#### Discussion

The row’s column will not be scrolled to visible via this method. To scroll the column to visible, use [`scrollColumnToVisible(_:)`](nsbrowser/scrollcolumntovisible(_:).md).

## Parameters

- `row`: The index of the row to scroll.
- `column`: The index of the column containing the row to scroll.

## See Also

- [var hasHorizontalScroller: Bool](nsbrowser/hashorizontalscroller.md)
  A Boolean that indicates whether the browser has a horizontal scroller.
- [func scrollColumnToVisible(Int)](nsbrowser/scrollcolumntovisible(_:).md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](nsbrowser/scrollcolumnsleft(by:).md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](nsbrowser/scrollcolumnsright(by:).md)
  Scrolls columns right by the specified number of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/scrollrowtovisible(_:incolumn:))*