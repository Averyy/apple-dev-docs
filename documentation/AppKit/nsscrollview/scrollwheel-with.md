# scrollWheel(with:)

**Framework**: AppKit  
**Kind**: method

Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func scrollWheel(with event: NSEvent)
```

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
- [var scrollsDynamically: Bool](nsscrollview/scrollsdynamically.md)
  A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollwheel(with:))*