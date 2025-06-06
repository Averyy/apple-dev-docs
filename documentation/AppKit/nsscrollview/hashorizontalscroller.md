# hasHorizontalScroller

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view has a horizontal scroller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasHorizontalScroller: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view allocates and displays a horizontal scroller as needed. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var horizontalScroller: NSScroller?](nsscrollview/horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var verticalScroller: NSScroller?](nsscrollview/verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](nsscrollview/hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](nsscrollview/autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hashorizontalscroller)*