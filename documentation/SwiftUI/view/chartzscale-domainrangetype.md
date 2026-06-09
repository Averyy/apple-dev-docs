# chartZScale(domain:range:type:)

**Framework**: SwiftUI  
**Kind**: method

Configures the z scale for 3D charts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
```

## Parameters

- `domain`: The possible data values along the z axis in the chart. You can define the domain with a `ClosedRange` for numeric values.
- `range`: The range of x positions that correspond to the scale domain. By default the range is determined by the dimension of the plot area.
- `type`: The scale type.

## See Also

- [func chartXScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartxscale(domain:range:type:).md)
  Configures the x scale for charts.
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
- [func chartZScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartzscale(domain:type:).md)
  Configures the z scale for 3D charts.
- [func chartZScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartzscale(range:type:).md)
  Configures the z scale for 3D charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzscale(domain:range:type:))*