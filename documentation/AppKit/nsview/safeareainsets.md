# safeAreaInsets

**Framework**: AppKit  
**Kind**: property

The distances from the edges of your view that define the safe area.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var safeAreaInsets: NSEdgeInsets { get }
```

#### Discussion

A view’s safe area reflects the portion of the view not covered by the window’s title bar or any ancestor views. This property reflects the superview’s safe area plus any additional insets you specify in the [`additionalSafeAreaInsets`](nsview/additionalsafeareainsets.md) property. If the view is not currently installed in a view hierarchy, or is not yet visible onscreen, the insets in this property are `0`.

## See Also

- [var safeAreaRect: NSRect](nsview/safearearect.md)
  A rectangle in the view’s coordinate system that contains the unobscured portion of the view.
- [var additionalSafeAreaInsets: NSEdgeInsets](nsview/additionalsafeareainsets.md)
  Custom insets that you specify to modify your view’s safe area
- [var safeAreaLayoutGuide: NSLayoutGuide](nsview/safearealayoutguide.md)
  The layout guide you use to position content inside your view’s safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/safeareainsets)*