# ScaleType

**Framework**: Swift Charts  
**Kind**: struct

The ways you can scale the domain or range of a plot.

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
struct ScaleType
```

#### Overview

Use this type with the `type:` parameter of `.chartXScale` view modifiers to customize scale types.

## Topics

### Type Properties
- [static var category: ScaleType](scaletype/category.md)
  A scale that has discrete domain values as inputs.
- [static var date: ScaleType](scaletype/date.md)
  A date scale where each range value y can be expressed as a function of the domain value x’s timestamp, with `y = a * x.timeIntervalSinceReferenceDate + b`.
- [static var linear: ScaleType](scaletype/linear.md)
  A number scale where each range value y can be expressed as a linear function of the domain value x, with `y = a * x + b`.
- [static var log: ScaleType](scaletype/log.md)
  A number scale where each range value y can be expressed as a logarithmic function of the domain value x, with `y = a * log(x) + b`.
- [static var squareRoot: ScaleType](scaletype/squareroot.md)
  A number scale where each range value y can be expressed as a square root function of the domain value x, with `y = a * sqrt(x) + b`. This is equivalent to a power scale with exponent 0.5.
- [static var symmetricLog: ScaleType](scaletype/symmetriclog.md)
  A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`. The constant `slopeAtZero` defaults to 1. You can configure it with `symmetricLog(slopeAtZero:)`.
### Type Methods
- [static func power(exponent: Double) -> ScaleType](scaletype/power(exponent:).md)
  A number scale where each range value y can be expressed as a power function of the domain value x, with `y = a * pow(x, exponent) + b`.
- [static func symmetricLog(slopeAtZero: Double) -> ScaleType](scaletype/symmetriclog(slopeatzero:).md)
  A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`.

## See Also

- [protocol ScaleRange](scalerange.md)
  A type that you can use to configure the range of a chart.
- [protocol PositionScaleRange](positionscalerange.md)
  A type that configures the x-axis and y-axis values.
- [struct PlotDimensionScaleRange](plotdimensionscalerange.md)
  A range that represents the plot area’s width or height.
- [protocol ScaleDomain](scaledomain.md)
  A type that you can use to configure the domain of a chart.
- [struct AutomaticScaleDomain](automaticscaledomain.md)
  A domain that the chart infers from its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/scaletype)*