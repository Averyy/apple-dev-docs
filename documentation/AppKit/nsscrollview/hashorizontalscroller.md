# hasHorizontalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view has a horizontal scroller.

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

When the value of this property is [`true`](../../Swift/true.md), the scroll view allocates and displays a horizontal scroller as needed. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing scrollers
- [var horizontalScroller: NSScroller?](./horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var verticalScroller: NSScroller?](./verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](./autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hashorizontalscroller)*