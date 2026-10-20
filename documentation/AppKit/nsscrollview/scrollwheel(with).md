# scrollWheel(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.

**Availability**:
- macOS

## Declaration

```swift
func scrollWheel(with event: NSEvent)
```

```objc
- (void) scrollWheel:(NSEvent *) event;
```

## See Also

### Setting Scrolling Behavior
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
- [var scrollsDynamically: Bool](./scrollsdynamically.md)
  A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollwheel(with:))*