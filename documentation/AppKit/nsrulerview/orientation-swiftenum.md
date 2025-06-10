# NSRulerView.Orientation

**Framework**: AppKit  
**Kind**: enum

These constants are defined to specify a ruler’s orientation and are used by [`orientation`](nsrulerview/orientation-swift.property.md).

**Availability**:
- macOS ?+

## Declaration

```swift
enum Orientation
```

## Topics

### Constants
- [NSRulerView.Orientation.horizontalRuler](nsrulerview/orientation-swift.enum/horizontalruler.md)
  Ruler is oriented horizontally.
- [NSRulerView.Orientation.verticalRuler](nsrulerview/orientation-swift.enum/verticalruler.md)
  Ruler is oriented vertically.
### Initializers
- [init?(rawValue: UInt)](nsrulerview/orientation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var scrollView: NSScrollView?](nsrulerview/scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](nsrulerview/orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [var reservedThicknessForAccessoryView: CGFloat](nsrulerview/reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](nsrulerview/reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](nsrulerview/rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](nsrulerview/requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](nsrulerview/baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/orientation-swift.enum)*