# chartXScale(domain:range:type:)

**Framework**: SwiftUI  
**Kind**: method

Configures the x scale for charts.

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
nonisolated
func chartXScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
```

## Parameters

- `domain`: The possible data values along the x axis in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)
- `range`: The range of x positions that correspond to the scale domain. By default the range is determined by the dimension of the plot area. You can use `range: .plotDimension(startPadding:, endPadding:)` to add padding to the scale range.
- `type`: The scale type.

## See Also

- [func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartxscale(domain:type:).md)
  Configures the x scale for charts.
- [func chartXScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartxscale(range:type:).md)
  Configures the x scale for charts.
- [func chartXScale(type: ScaleType?) -> some View](view/chartxscale(type:).md)
  Configures the x scale for charts.
- [func chartYScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartyscale(domain:range:type:).md)
  Configures the y scale for charts.
- [func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartyscale(domain:type:).md)
  Configures the y scale for charts.
- [func chartYScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartyscale(range:type:).md)
  Configures the y scale for charts.
- [func chartYScale(type: ScaleType?) -> some View](view/chartyscale(type:).md)
  Configures the y scale for charts.
- [func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartzscale(domain:range:type:).md)
  Configures the z scale for 3D charts.
- [func chartZScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartzscale(domain:type:).md)
  Configures the z scale for 3D charts.
- [func chartZScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartzscale(range:type:).md)
  Configures the z scale for 3D charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartxscale(domain:range:type:))*