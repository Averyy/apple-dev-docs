# scrollsDynamically

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.

**Availability**:
- macOS

## Declaration

```swift
var scrollsDynamically: Bool { get set }
```

```objc
@property BOOL scrollsDynamically;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroll view redraws its document view while scrolling. When the value of this property is[`false`](../../Swift/false.md), the scroll view redraws only when the scroller knob is released. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Setting scrolling behavior
- [var lineScroll: CGFloat](./linescroll.md)
  The scroll view’s line by line scroll amount.
- [var horizontalLineScroll: CGFloat](./horizontallinescroll.md)
  The scroll view’s horizontal line by line scroll amount.
- [var verticalLineScroll: CGFloat](./verticallinescroll.md)
  The scroll view’s vertical line by line scroll amount.
- [var pageScroll: CGFloat](./pagescroll.md)
  The amount of the document view kept visible when scrolling page by page.
- [var horizontalPageScroll: CGFloat](./horizontalpagescroll.md)
  The amount of the document view kept visible when scrolling horizontally page by page.
- [var verticalPageScroll: CGFloat](./verticalpagescroll.md)
  The amount of the document view kept visible when scrolling vertically page by page.
- [func scrollWheel(with: NSEvent)](./scrollwheel%28with%29.md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollsdynamically)*