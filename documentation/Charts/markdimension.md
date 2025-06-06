# MarkDimension

**Framework**: Swift Charts  
**Kind**: struct

An individual dimension representing a mark’s width or height.

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
struct MarkDimension
```

## Topics

### Supporting types
- [struct MarkDimensions](markdimensions.md)
### Initializers
- [init(floatLiteral: Double)](markdimension/init(floatliteral:).md)
  Creates a constant width or height from a floating point value.
- [init(integerLiteral: Int)](markdimension/init(integerliteral:).md)
  Creates a constant width or height from an integer.
### Type Properties
- [static var automatic: MarkDimension](markdimension/automatic.md)
  A dimension that determines its value automatically.
### Type Methods
- [static func fixed(CGFloat) -> MarkDimension](markdimension/fixed(_:).md)
  A constant dimension.
- [static func inset(CGFloat) -> MarkDimension](markdimension/inset(_:).md)
  A dimension that’s the step size minus the specified inset value on each side.
- [static func ratio(CGFloat) -> MarkDimension](markdimension/ratio(_:).md)
  A dimension that’s proportional to the scale step size, using the specified ratio.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MarkStackingMethod](markstackingmethod.md)
  The ways in which you can stack marks in a chart.
- [struct InterpolationMethod](interpolationmethod.md)
  The ways in which line or area marks interpolate their data.
- [struct BasicChartSymbolShape](basicchartsymbolshape.md)
  A basic chart symbol shape.
- [protocol ChartSymbolShape](chartsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
- [struct AnyChartSymbolShape](anychartsymbolshape.md)
  A type-erased plotting shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/markdimension)*