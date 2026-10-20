# scrollColumnsRight(by:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls columns right by the specified number of columns.

**Availability**:
- macOS

## Declaration

```swift
func scrollColumnsRight(by shiftAmount: Int)
```

```objc
- (void) scrollColumnsRightBy:(NSInteger) shiftAmount;
```

## Parameters

- `shiftAmount`: The number of columns by which to scroll the browser.

## See Also

### Scrolling
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  A Boolean that indicates whether the browser has a horizontal scroller.
- [func scrollColumnToVisible(Int)](./scrollcolumntovisible%28_%29.md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](./scrollcolumnsleft%28by%29.md)
  Scrolls columns left by the specified number of columns.
- [func scrollRowToVisible(Int, inColumn: Int)](./scrollrowtovisible%28_,incolumn%29.md)
  Scrolls the specified row to be visible within the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/scrollcolumnsright(by:))*