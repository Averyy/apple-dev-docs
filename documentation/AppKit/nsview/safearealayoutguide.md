# safeAreaLayoutGuide

**Framework**: AppKit  
**Kind**: property

The layout guide you use to position content inside your view’s safe area.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var safeAreaLayoutGuide: NSLayoutGuide { get }
```

#### Discussion

The layout guide in this property reflects the view’s frame minus its safe area insets. Use this guide to configure layout rules relative to this safe area.

## See Also

- [var safeAreaRect: NSRect](nsview/safearearect.md)
  A rectangle in the view’s coordinate system that contains the unobscured portion of the view.
- [var safeAreaInsets: NSEdgeInsets](nsview/safeareainsets.md)
  The distances from the edges of your view that define the safe area.
- [var additionalSafeAreaInsets: NSEdgeInsets](nsview/additionalsafeareainsets.md)
  Custom insets that you specify to modify your view’s safe area


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/safearealayoutguide)*