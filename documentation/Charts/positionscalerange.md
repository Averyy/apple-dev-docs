# PositionScaleRange

**Framework**: Swift Charts  
**Kind**: protocol  
**Role**: Protocol

A type that configures the x-axis and y-axis values.

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
protocol PositionScaleRange : ScaleRange where Self.VisualValue == CGFloat
```

## Topics

### Type Properties
- [static var plotDimension: PlotDimensionScaleRange](./positionscalerange/plotdimension.md)
  A scale range that fills the plot area.
### Type Methods
- [static func plotDimension(padding: CGFloat) -> PlotDimensionScaleRange](./positionscalerange/plotdimension%28padding%29.md)
  A scale range that fills the plot area with the given padding value at start and end.
- [static func plotDimension(startPadding: CGFloat, endPadding: CGFloat) -> PlotDimensionScaleRange](./positionscalerange/plotdimension%28startpadding,endpadding%29.md)
  A scale range that fills the plot area with the given padding values at start and end, respectively.

## Relationships

### Inherits From
- [ScaleRange](./scalerange.md)
### Conforming Types
- [PlotDimensionScaleRange](./plotdimensionscalerange.md)

## See Also

### Scales
- [protocol ScaleRange](./scalerange.md)
  A type that you can use to configure the range of a chart.
- [struct PlotDimensionScaleRange](./plotdimensionscalerange.md)
  A range that represents the plot area’s width or height.
- [protocol ScaleDomain](./scaledomain.md)
  A type that you can use to configure the domain of a chart.
- [struct AutomaticScaleDomain](./automaticscaledomain.md)
  A domain that the chart infers from its data.
- [struct ScaleType](./scaletype.md)
  The ways you can scale the domain or range of a plot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/positionscalerange)*