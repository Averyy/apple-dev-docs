# ChartSymbolShape

**Framework**: Swift Charts  
**Kind**: protocol

A type that can act as a shape for the marks that you add to a chart.

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
protocol ChartSymbolShape : Shape
```

## Topics

### Instance Properties
- [var perceptualUnitRect: CGRect](chartsymbolshape/perceptualunitrect.md)
  Returns a rectangle that bounds the shape in such a way that viewers perceive it as having the same size and position as a unit rectangle.
### Instance Methods
- [func strokeBorder(lineWidth: CGFloat) -> some ChartSymbolShape](chartsymbolshape/strokeborder(linewidth:).md)
- [func strokeBorder(style: StrokeStyle) -> some ChartSymbolShape](chartsymbolshape/strokeborder(style:).md)
### Type Properties
- [static var asterisk: BasicChartSymbolShape](chartsymbolshape/asterisk.md)
  Asterisk symbol.
- [static var circle: BasicChartSymbolShape](chartsymbolshape/circle.md)
  Circle symbol.
- [static var cross: BasicChartSymbolShape](chartsymbolshape/cross.md)
  Cross symbol.
- [static var diamond: BasicChartSymbolShape](chartsymbolshape/diamond.md)
  Diamond symbol.
- [static var pentagon: BasicChartSymbolShape](chartsymbolshape/pentagon.md)
  Pentagon symbol.
- [static var plus: BasicChartSymbolShape](chartsymbolshape/plus.md)
  Plus symbol.
- [static var square: BasicChartSymbolShape](chartsymbolshape/square.md)
  Square symbol.
- [static var triangle: BasicChartSymbolShape](chartsymbolshape/triangle.md)
  Triangle symbol.

## Relationships

### Inherits From
- [Animatable](../SwiftUI/Animatable.md)
- [Sendable](../Swift/Sendable.md)
- [Shape](../SwiftUI/Shape.md)
- [View](../SwiftUI/View.md)
### Conforming Types
- [AnyChartSymbolShape](anychartsymbolshape.md)
- [BasicChartSymbolShape](basicchartsymbolshape.md)

## See Also

- [struct MarkStackingMethod](markstackingmethod.md)
  The ways in which you can stack marks in a chart.
- [struct MarkDimension](markdimension.md)
  An individual dimension representing a mark’s width or height.
- [struct InterpolationMethod](interpolationmethod.md)
  The ways in which line or area marks interpolate their data.
- [struct BasicChartSymbolShape](basicchartsymbolshape.md)
  A basic chart symbol shape.
- [struct AnyChartSymbolShape](anychartsymbolshape.md)
  A type-erased plotting shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartsymbolshape)*