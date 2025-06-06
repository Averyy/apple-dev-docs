# CGGradientDrawingOptions

**Framework**: Core Graphics  
**Kind**: struct

Drawing locations for gradients.

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
struct CGGradientDrawingOptions
```

## Topics

### Constants
- [static var drawsBeforeStartLocation: CGGradientDrawingOptions](cggradientdrawingoptions/drawsbeforestartlocation.md)
  The fill should extend beyond the starting location. The color that extends beyond the starting point is the solid color defined by the [`CGGradient`](cggradient.md) object to be at location 0.
- [static var drawsAfterEndLocation: CGGradientDrawingOptions](cggradientdrawingoptions/drawsafterendlocation.md)
  The fill should extend beyond the ending location. The color that extends beyond the ending point is the solid color defined by the [`CGGradient`](cggradient.md) object to be at location 1.
### Initializers
- [init(rawValue: UInt32)](cggradientdrawingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:).md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [func drawShading(CGShading)](cgcontext/drawshading(_:).md)
  Fills the clipping path of a context with the specified shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions)*