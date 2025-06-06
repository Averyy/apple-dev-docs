# lineScroll

**Framework**: AppKit  
**Kind**: property

The scroll view’s line by line scroll amount.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var lineScroll: CGFloat { get set }
```

#### Discussion

The value of this property is the amount by which the scroll view scrolls itself when scrolling line by line, expressed in the content view’s coordinate system. This value is used when the user clicks the scroll arrows without holding down a modifier key. When displaying text in a scroll view, for example, you might set this value to the height of a single line of text in the default font. As part of its implementation, this property accesses [`verticalLineScroll`](nsscrollview/verticallinescroll.md).

Note that a scroll view can have two different line scroll amounts: [`verticalLineScroll`](nsscrollview/verticallinescroll.md) and [`horizontalLineScroll`](nsscrollview/horizontallinescroll.md). Set this property only if you can be sure they’re both the same; setting this property sets both [`verticalLineScroll`](nsscrollview/verticallinescroll.md) and [`horizontalLineScroll`](nsscrollview/horizontallinescroll.md) to the same value.

## See Also

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
- [func scrollWheel(with: NSEvent)](nsscrollview/scrollwheel(with:).md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/linescroll)*