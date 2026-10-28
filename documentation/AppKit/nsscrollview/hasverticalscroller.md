# hasVerticalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view has a vertical scroller.

**Availability**:
- macOS

## Declaration

```swift
var hasVerticalScroller: Bool { get set }
```

```objc
@property BOOL hasVerticalScroller;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroll view allocates and displays a vertical scroller as needed. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing Scrollers
- [var horizontalScroller: NSScroller?](./horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var verticalScroller: NSScroller?](./verticalscroller.md)
  The scroll view’s vertical scroller.
- [var autohidesScrollers: Bool](./autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hasverticalscroller)*