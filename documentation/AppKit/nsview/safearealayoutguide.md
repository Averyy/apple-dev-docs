# safeAreaLayoutGuide

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout guide you use to position content inside your view’s safe area.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var safeAreaLayoutGuide: NSLayoutGuide { get }
```

```objc
@property (strong, readonly) NSLayoutGuide * safeAreaLayoutGuide;
```

## Discussion

The layout guide in this property reflects the view’s frame minus its safe area insets. Use this guide to configure layout rules relative to this safe area.

## See Also

### Respecting the View’s Safe Area
- [var safeAreaRect: NSRect](./safearearect.md)
  A rectangle in the view’s coordinate system that contains the unobscured portion of the view.
- [var safeAreaInsets: NSEdgeInsets](./safeareainsets.md)
  The distances from the edges of your view that define the safe area.
- [var additionalSafeAreaInsets: NSEdgeInsets](./additionalsafeareainsets.md)
  Custom insets that you specify to modify your view’s safe area


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/safearealayoutguide)*