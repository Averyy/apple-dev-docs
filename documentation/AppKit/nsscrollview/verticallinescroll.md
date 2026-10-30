# verticalLineScroll

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s vertical line by line scroll amount.

**Availability**:
- macOS

## Declaration

```swift
var verticalLineScroll: CGFloat { get set }
```

```objc
@property CGFloat verticalLineScroll;
```

## Discussion

The value of this property is the amount by which the scroll view scrolls itself vertically when scrolling line by line, expressed in the content view’s coordinate system. This value is used when the user clicks the scroll arrows on the vertical scroll bar without holding down a modifier key.

## See Also

### Setting scrolling behavior
- [var lineScroll: CGFloat](./linescroll.md)
  The scroll view’s line by line scroll amount.
- [var horizontalLineScroll: CGFloat](./horizontallinescroll.md)
  The scroll view’s horizontal line by line scroll amount.
- [var pageScroll: CGFloat](./pagescroll.md)
  The amount of the document view kept visible when scrolling page by page.
- [var horizontalPageScroll: CGFloat](./horizontalpagescroll.md)
  The amount of the document view kept visible when scrolling horizontally page by page.
- [var verticalPageScroll: CGFloat](./verticalpagescroll.md)
  The amount of the document view kept visible when scrolling vertically page by page.
- [var scrollsDynamically: Bool](./scrollsdynamically.md)
  A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.
- [func scrollWheel(with: NSEvent)](./scrollwheel%28with%29.md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticallinescroll)*