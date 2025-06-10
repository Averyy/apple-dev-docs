# NSImageInterpolation

**Framework**: AppKit  
**Kind**: enum

Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSImageInterpolation
```

#### Overview

Use these constants with the [`imageInterpolation`](nsgraphicscontext/imageinterpolation.md) property.

## Topics

### Constants
- [NSImageInterpolation.default](nsimageinterpolation/default.md)
  Use the context’s default interpolation.
- [NSImageInterpolation.none](nsimageinterpolation/none.md)
  No interpolation.
- [NSImageInterpolation.low](nsimageinterpolation/low.md)
  Fast, low-quality interpolation.
- [NSImageInterpolation.medium](nsimageinterpolation/medium.md)
  Medium quality, slower than the low interpolation option.
- [NSImageInterpolation.high](nsimageinterpolation/high.md)
  Highest quality, slower than the medium interpolation option.
### Initializers
- [init?(rawValue: UInt)](nsimageinterpolation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var compositingOperation: NSCompositingOperation](nsgraphicscontext/compositingoperation.md)
  The graphics context’s global compositing operation setting.
- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
- [var imageInterpolation: NSImageInterpolation](nsgraphicscontext/imageinterpolation.md)
  A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.
- [var shouldAntialias: Bool](nsgraphicscontext/shouldantialias.md)
  A Boolean value that indicates whether the graphics context uses antialiasing.
- [var patternPhase: NSPoint](nsgraphicscontext/patternphase.md)
  The amount to offset the pattern color when filling the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageinterpolation)*