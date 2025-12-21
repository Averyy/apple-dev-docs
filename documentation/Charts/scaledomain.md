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

#### Overview

A type you use to configure the domain of a chart scale.

#### Including Zero in Number Scales

By default, number scales include zero in the domain to ensure charts follow the best practice to include a zero baseline in bar charts.

![Horizontal bar chart with y-axis showing categories A, B, and C and x-axis ranging from 0 to 15. There are three bars: A 5, B 10, C 15.](https://docs-assets.developer.apple.com/published/e68dd25b1f8124a7a86dd5304dbae2b3/Scales.ChartWithDefaultCategoryDomain%402x.png)

For other marks, this zero baseline isn’t as important, but the framework includes zero by default so the domain inference logic is consistent and deterministic.  Changing the mark type won’t suddenly affect scale domain.

![Horizontal dot plot with x-axis ranging from 0 to 100. It has 5 dots, at 12, 20, 50, 70, and 85.](https://docs-assets.developer.apple.com/published/51bce47e24c398752082b540615e4812/ExNumberScale%402x.png)

If you don’t want to include the zero baseline in certain cases, use `automatic(includeszero:reversed:)` to customize the scale domain and disable the automatic zero inclusion.

```swift
Chart([20, 30, 50, 70, 85], id: \.self) {
    PointMark(
        x: .value("Value", $0)
    )
}
.chartXScale(domain: .automatic(includesZero: false))
```

![Horizontal dot plot with x-axis ranging from 20 to 100. It has 5 dots, at 20, 30, 50, 70, and 85.](https://docs-assets.developer.apple.com/published/74790b460bf1b1cd57c6828ee5c8e922/ScaleDomain.ChartWithNumberScaleExcludingZero%402x.png)

#### Reversing the Order of Inferred Domain

You can also reverse the order of the inferred domain:

```swift
Chart([20, 30, 50, 70, 85], id: \.self) {
    PointMark(
        x: .value("Value", $0)
    )
}
.chartXScale(domain: .automatic(reversed: true))
```

![Horizontal dot plot with x-axis ranging from 100 to 0. It has 5 dots, at 85, 70, 50, 30, and 20.](https://docs-assets.developer.apple.com/published/a3d2d262c008a7ac3df5f2215a9ba61d/ScaleDomain.ChartWithNumberScaleReversed%402x.png)

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