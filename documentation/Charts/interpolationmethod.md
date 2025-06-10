# InterpolationMethod

**Framework**: Swift Charts  
**Kind**: struct

The ways in which line or area marks interpolate their data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@frozen
struct InterpolationMethod
```

## Topics

### Type Properties
- [static var cardinal: InterpolationMethod](interpolationmethod/cardinal.md)
  Interpolate data points with cardinal spline.
- [static var catmullRom: InterpolationMethod](interpolationmethod/catmullrom.md)
  Interpolate data points with Catmull-Rom spline.
- [static var linear: InterpolationMethod](interpolationmethod/linear.md)
  Interpolate data points linearly.
- [static var monotone: InterpolationMethod](interpolationmethod/monotone.md)
  Interpolate data points with a cubic spline that preserves monotonicity of the data.
- [static var stepCenter: InterpolationMethod](interpolationmethod/stepcenter.md)
  Interpolate data points with a step, or piece-wise constant function, where the data point is at the center of the step.
- [static var stepEnd: InterpolationMethod](interpolationmethod/stepend.md)
  Interpolate data points with a step, or piece-wise constant function, where the data point is at the end of the step.
- [static var stepStart: InterpolationMethod](interpolationmethod/stepstart.md)
  Interpolate data points with a step, or piece-wise constant function, where the data point is at the start of the step.
### Type Methods
- [static func cardinal(tension: CGFloat) -> InterpolationMethod](interpolationmethod/cardinal(tension:).md)
  Interpolate data points with cardinal spline, using the given tension parameter.
- [static func catmullRom(alpha: CGFloat) -> InterpolationMethod](interpolationmethod/catmullrom(alpha:).md)
  Interpolate data points with Catmull-Rom spline, using the given alpha parameter.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MarkStackingMethod](markstackingmethod.md)
  The ways in which you can stack marks in a chart.
- [struct MarkDimension](markdimension.md)
  An individual dimension representing a mark’s width or height.
- [struct BasicChartSymbolShape](basicchartsymbolshape.md)
  A basic chart symbol shape.
- [protocol ChartSymbolShape](chartsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
- [struct AnyChartSymbolShape](anychartsymbolshape.md)
  A type-erased plotting shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/interpolationmethod)*