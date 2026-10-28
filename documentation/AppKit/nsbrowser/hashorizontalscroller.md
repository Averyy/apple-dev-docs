# hasHorizontalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the browser has a horizontal scroller.

**Availability**:
- macOS

## Declaration

```swift
var hasHorizontalScroller: Bool { get set }
```

```objc
@property BOOL hasHorizontalScroller;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the browser uses an `NSScroller` object to scroll horizontally.

## See Also

### Scrolling
- [func scrollColumnToVisible(Int)](./scrollcolumntovisible%28_%29.md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](./scrollcolumnsleft%28by%29.md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](./scrollcolumnsright%28by%29.md)
  Scrolls columns right by the specified number of columns.
- [func scrollRowToVisible(Int, inColumn: Int)](./scrollrowtovisible%28_,incolumn%29.md)
  Scrolls the specified row to be visible within the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/hashorizontalscroller)*