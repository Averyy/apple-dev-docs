# scrollsDynamically

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var scrollsDynamically: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the scroll view redraws its document view while scrolling. When the value of this property is[`false`](https://developer.apple.com/documentation/Swift/false), the scroll view redraws only when the scroller knob is released. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var lineScroll: CGFloat](nsscrollview/linescroll.md)
  The scroll view’s line by line scroll amount.
- [var horizontalLineScroll: CGFloat](nsscrollview/horizontallinescroll.md)
  The scroll view’s horizontal line by line scroll amount.
- [var verticalLineScroll: CGFloat](nsscrollview/verticallinescroll.md)
  The scroll view’s vertical line by line scroll amount.
- [var pageScroll: CGFloat](nsscrollview/pagescroll.md)
  The amount of the document view kept visible when scrolling page by page.
- [var horizontalPageScroll: CGFloat](nsscrollview/horizontalpagescroll.md)
  The amount of the document view kept visible when scrolling horizontally page by page.
- [var verticalPageScroll: CGFloat](nsscrollview/verticalpagescroll.md)
  The amount of the document view kept visible when scrolling vertically page by page.
- [func scrollWheel(with: NSEvent)](nsscrollview/scrollwheel(with:).md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollsdynamically)*