# scrollRowToVisible(_:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the specified row to be visible within the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func scrollRowToVisible(_ row: Int, inColumn column: Int)
```

```objc
- (void) scrollRowToVisible:(NSInteger) row inColumn:(NSInteger) column;
```

## Discussion

The row’s column will not be scrolled to visible via this method. To scroll the column to visible, use [`scrollColumnToVisible(_:)`](./scrollcolumntovisible%28_%29.md).

## Parameters

- `row`: The index of the row to scroll.
- `column`: The index of the column containing the row to scroll.

## See Also

### Scrolling
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  A Boolean that indicates whether the browser has a horizontal scroller.
- [func scrollColumnToVisible(Int)](./scrollcolumntovisible%28_%29.md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](./scrollcolumnsleft%28by%29.md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](./scrollcolumnsright%28by%29.md)
  Scrolls columns right by the specified number of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/scrollrowtovisible(_:incolumn:))*