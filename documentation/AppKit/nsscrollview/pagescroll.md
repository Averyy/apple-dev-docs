# pageScroll

**Framework**: AppKit  
**Kind**: property

The amount of the document view kept visible when scrolling page by page.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var pageScroll: CGFloat { get set }
```

#### Discussion

The value of this property is the amount of the document view kept visible when scrolling page by page, expressed in the content view’s coordinate system. This value is used when the user clicks the scroll arrows while holding down the Option key. As part of its implementation, this property accesses [`verticalPageScroll`](nsscrollview/verticalpagescroll.md).

This amount expresses the context that remains when the scroll view scrolls by one page, allowing the user to orient to the new display. It differs from the line scroll amount, which indicates how far the document view moves. The page scroll amount is the amount common to the content view before and after the document view is scrolled by one page. Thus, setting the page scroll amount to `0.0` implies that the entire visible portion of the document view is replaced when a page scroll occurs.

Note that a scroll view can have two different page scroll amounts: [`verticalPageScroll`](nsscrollview/verticalpagescroll.md) and [`horizontalPageScroll`](nsscrollview/horizontalpagescroll.md). Set this property only if you can be sure they’re both the same; setting this property sets both [`verticalPageScroll`](nsscrollview/verticalpagescroll.md) and [`horizontalPageScroll`](nsscrollview/horizontalpagescroll.md) to the same value.

## See Also

- [var lineScroll: CGFloat](nsscrollview/linescroll.md)
  The scroll view’s line by line scroll amount.
- [var horizontalLineScroll: CGFloat](nsscrollview/horizontallinescroll.md)
  The scroll view’s horizontal line by line scroll amount.
- [var verticalLineScroll: CGFloat](nsscrollview/verticallinescroll.md)
  The scroll view’s vertical line by line scroll amount.
- [var horizontalPageScroll: CGFloat](nsscrollview/horizontalpagescroll.md)
  The amount of the document view kept visible when scrolling horizontally page by page.
- [var verticalPageScroll: CGFloat](nsscrollview/verticalpagescroll.md)
  The amount of the document view kept visible when scrolling vertically page by page.
- [var scrollsDynamically: Bool](nsscrollview/scrollsdynamically.md)
  A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.
- [func scrollWheel(with: NSEvent)](nsscrollview/scrollwheel(with:).md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/pagescroll)*