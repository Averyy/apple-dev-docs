# verticalScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroll view’s vertical scroller.

**Availability**:
- macOS

## Declaration

```swift
var verticalScroller: NSScroller? { get set }
```

```objc
@property (strong, nullable) NSScroller * verticalScroller;
```

## Discussion

The value of this property is `nil` if the scroll view has no vertical scroller.

You can access the vertical scroller using this property even if the scroll view isn’t currently displaying it. To make sure the scroller is visible, set [`hasVerticalScroller`](./hasverticalscroller.md) to [`true`](../../Swift/true.md).

## See Also

### Managing Scrollers
- [var horizontalScroller: NSScroller?](./horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](./autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticalscroller)*