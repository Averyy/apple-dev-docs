# CGGradientDrawingOptions

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

Drawing locations for gradients.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CGGradientDrawingOptions
```

```c
enum CGGradientDrawingOptions : uint32_t;
```

## Topics

### Constants
- [static var drawsBeforeStartLocation: CGGradientDrawingOptions](./cggradientdrawingoptions/drawsbeforestartlocation.md)
  The fill should extend beyond the starting location. The color that extends beyond the starting point is the solid color defined by the [`CGGradient`](./cggradient.md) object to be at location 0.
- [static var drawsAfterEndLocation: CGGradientDrawingOptions](./cggradientdrawingoptions/drawsafterendlocation.md)
  The fill should extend beyond the ending location. The color that extends beyond the ending point is the solid color defined by the [`CGGradient`](./cggradient.md) object to be at location 1.
### Initializers
- [init(rawValue: UInt32)](./cggradientdrawingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Drawing Gradients and Shadings
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](./cgcontext/drawlineargradient%28_,start,end,options%29.md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](./cgcontext/drawradialgradient%28_,startcenter,startradius,endcenter,endradius,options%29.md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [func drawShading(CGShading)](./cgcontext/drawshading%28_%29.md)
  Fills the clipping path of a context with the specified shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions)*