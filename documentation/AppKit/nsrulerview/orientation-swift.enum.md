# NSRulerView.Orientation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants are defined to specify a ruler’s orientation and are used by [`orientation`](./orientation-swift.property.md).

**Availability**:
- macOS

## Declaration

```swift
enum Orientation
```

```c
enum NSRulerOrientation : NSUInteger;
```

## Topics

### Constants
- [NSRulerView.Orientation.horizontalRuler](./orientation-swift.enum/horizontalruler.md)
  Ruler is oriented horizontally.
- [NSRulerView.Orientation.verticalRuler](./orientation-swift.enum/verticalruler.md)
  Ruler is oriented vertically.
### Initializers
- [init?(rawValue: UInt)](./orientation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Ruler layout
- [var scrollView: NSScrollView?](./scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](./orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [var reservedThicknessForAccessoryView: CGFloat](./reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](./reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](./rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](./requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](./baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/orientation-swift.enum)*