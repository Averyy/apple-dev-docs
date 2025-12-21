# hasHorizontalScroller

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the browser has a horizontal scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasHorizontalScroller: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the browser uses an `NSScroller` object to scroll horizontally.

## See Also

- [func scrollColumnToVisible(Int)](nsbrowser/scrollcolumntovisible(_:).md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](nsbrowser/scrollcolumnsleft(by:).md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](nsbrowser/scrollcolumnsright(by:).md)
  Scrolls columns right by the specified number of columns.
- [func scrollRowToVisible(Int, inColumn: Int)](nsbrowser/scrollrowtovisible(_:incolumn:).md)
  Scrolls the specified row to be visible within the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/hashorizontalscroller)*