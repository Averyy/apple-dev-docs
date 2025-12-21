# verticalScroller

**Framework**: AppKit  
**Kind**: property

The scroll view’s vertical scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var verticalScroller: NSScroller? { get set }
```

#### Discussion

The value of this property is `nil` if the scroll view has no vertical scroller.

You can access the vertical scroller using this property even if the scroll view isn’t currently displaying it. To make sure the scroller is visible, set [`hasVerticalScroller`](nsscrollview/hasverticalscroller.md) to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var horizontalScroller: NSScroller?](nsscrollview/horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var hasHorizontalScroller: Bool](nsscrollview/hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var hasVerticalScroller: Bool](nsscrollview/hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](nsscrollview/autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticalscroller)*