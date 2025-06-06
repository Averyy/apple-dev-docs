# ScaleDomain

**Framework**: Swift Charts  
**Kind**: protocol

A type that you can use to configure the domain of a chart.

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
protocol ScaleDomain
```

## Topics

### Type Properties
- [static var automatic: AutomaticScaleDomain](scaledomain/automatic.md)
  Creates a scale domain configuration that infers the scale domain from data.
### Type Methods
- [static func automatic(includesZero: Bool?, reversed: Bool?) -> AutomaticScaleDomain](scaledomain/automatic(includeszero:reversed:).md)
  Creates a scale domain configuration that infers the scale domain from data.
- [static func automatic<DataValue>(includesZero: Bool?, reversed: Bool?, dataType: DataValue.Type, modifyInferredDomain: (inout [DataValue]) -> Void) -> AutomaticScaleDomain](scaledomain/automatic(includeszero:reversed:datatype:modifyinferreddomain:).md)
  Creates a scale domain configuration that infers the scale domain from data.

## Relationships

### Conforming Types
- [AutomaticScaleDomain](automaticscaledomain.md)

## See Also

- [protocol ScaleRange](scalerange.md)
  A type that you can use to configure the range of a chart.
- [protocol PositionScaleRange](positionscalerange.md)
  A type that configures the x-axis and y-axis values.
- [struct PlotDimensionScaleRange](plotdimensionscalerange.md)
  A range that represents the plot area’s width or height.
- [struct AutomaticScaleDomain](automaticscaledomain.md)
  A domain that the chart infers from its data.
- [struct ScaleType](scaletype.md)
  The ways you can scale the domain or range of a plot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/scaledomain)*