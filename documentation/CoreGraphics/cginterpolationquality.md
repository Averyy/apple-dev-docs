# CGInterpolationQuality

**Framework**: Core Graphics  
**Kind**: enum

Levels of interpolation quality for rendering an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGInterpolationQuality
```

#### Overview

You use the function [`CGContextSetInterpolationQuality`](cgcontextsetinterpolationquality.md) to set the interpolation quality in a graphics context.

## Topics

### Constants
- [CGInterpolationQuality.default](cginterpolationquality/default.md)
  The default level of quality.
- [CGInterpolationQuality.none](cginterpolationquality/none.md)
  No interpolation.
- [CGInterpolationQuality.low](cginterpolationquality/low.md)
  A low level of interpolation quality. This setting may speed up image rendering.
- [CGInterpolationQuality.medium](cginterpolationquality/medium.md)
  A medium level of interpolation quality. This setting is slower than the low setting but faster than the high setting.
- [CGInterpolationQuality.high](cginterpolationquality/high.md)
  A high level of interpolation quality. This setting may slow down image rendering.
### Initializers
- [init?(rawValue: Int32)](cginterpolationquality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func draw(CGImage, in: CGRect, byTiling: Bool)](cgcontext/draw(_:in:bytiling:).md)
  Draws an image in the specified area.
- [func drawPDFPage(CGPDFPage)](cgcontext/drawpdfpage(_:).md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cginterpolationquality)*