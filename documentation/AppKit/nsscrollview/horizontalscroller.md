# horizontalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s horizontal scroller.

**Availability**:
- macOS

## Declaration

```swift
var horizontalScroller: NSScroller? { get set }
```

```objc
@property (strong, nullable) NSScroller * horizontalScroller;
```

## Discussion

The value of this property is `nil` if the scroll view has no horizontal scroller.

You can access the horizontal scroller using this property even if the scroll view isn’t currently displaying it. To make sure the scroller is visible, set [`hasHorizontalScroller`](./hashorizontalscroller.md) to [`true`](../../Swift/true.md).

## See Also

### Managing scrollers
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var verticalScroller: NSScroller?](./verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](./autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/horizontalscroller)*