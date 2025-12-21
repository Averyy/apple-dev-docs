# horizontalScroller

**Framework**: AppKit  
**Kind**: property

The scroll view’s horizontal scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var horizontalScroller: NSScroller? { get set }
```

#### Discussion

The value of this property is `nil` if the scroll view has no horizontal scroller.

You can access the horizontal scroller using this property even if the scroll view isn’t currently displaying it. To make sure the scroller is visible, set [`hasHorizontalScroller`](nsscrollview/hashorizontalscroller.md) to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var hasHorizontalScroller: Bool](nsscrollview/hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var verticalScroller: NSScroller?](nsscrollview/verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](nsscrollview/hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](nsscrollview/autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/horizontalscroller)*