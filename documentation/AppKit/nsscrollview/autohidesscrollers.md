# autohidesScrollers

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autohidesScrollers: Bool { get set }
```

#### Discussion

The horizontal and vertical scroll bars are hidden independently of each other. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the content of the scroll view doesn’t extend beyond the size of the clip view on a given axis, the scroller on that axis is removed to leave more room for the content.

> **Note**:  The `autohidesScrollers` property introduced in OS X v10.3, while still relevant for legacy-style scrollers, does not apply to the automatic hiding behavior of overlay-style scrollers. The property may still be set, but is ignored by a scroll view that’s using overlay scrollers.

## See Also

- [var scrollerStyle: NSScroller.Style](nsscrollview/scrollerstyle.md)
  The scroller style used by the scroll view.
- [var horizontalScroller: NSScroller?](nsscrollview/horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var hasHorizontalScroller: Bool](nsscrollview/hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var verticalScroller: NSScroller?](nsscrollview/verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](nsscrollview/hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/autohidesscrollers)*