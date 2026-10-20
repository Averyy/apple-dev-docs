# chartZScale(domain:type:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func chartZScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain
```

## Parameters

- `domain`: The possible data values along the z axis in the chart. You can define the domain with a `ClosedRange` for numeric values (e.g., `0 ... 500`).
- `type`: The scale type.

## See Also

### Axis scales
- [func chartXScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartxscale%28domain,range,type%29.md)
  Configures the x scale for charts.
- [func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./chartxscale%28domain,type%29.md)
  Configures the x scale for charts.
- [func chartXScale<Range>(range: Range, type: ScaleType?) -> some View](./chartxscale%28range,type%29.md)
  Configures the x scale for charts.
- [func chartXScale(type: ScaleType?) -> some View](./chartxscale%28type%29.md)
  Configures the x scale for charts.
- [func chartYScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartyscale%28domain,range,type%29.md)
  Configures the y scale for charts.
- [func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./chartyscale%28domain,type%29.md)
  Configures the y scale for charts.
- [func chartYScale<Range>(range: Range, type: ScaleType?) -> some View](./chartyscale%28range,type%29.md)
  Configures the y scale for charts.
- [func chartYScale(type: ScaleType?) -> some View](./chartyscale%28type%29.md)
  Configures the y scale for charts.
- [func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartzscale%28domain,range,type%29.md)
  Configures the z scale for 3D charts.
- [func chartZScale<Range>(range: Range, type: ScaleType?) -> some View](./chartzscale%28range,type%29.md)
  Configures the z scale for 3D charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzscale(domain:type:))*