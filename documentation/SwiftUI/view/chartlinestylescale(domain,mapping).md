# chartLineStyleScale(domain:mapping:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the line style scale for charts.

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
func chartLineStyleScale<Domain>(domain: Domain, mapping: @escaping (Domain.Element) -> StrokeStyle) -> some View where Domain : Collection, Domain.Element : Plottable
```

## Parameters

- `domain`: The possible data values plotted as line style in the chart.
- `mapping`: Maps data categories to line styles.

## See Also

### Line style scales
- [func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) -> some View](./chartlinestylescale%28_%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain) -> some View](./chartlinestylescale%28domain%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some View](./chartlinestylescale%28domain,range%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Range>(range: Range) -> some View](./chartlinestylescale%28range%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) -> some View](./chartlinestylescale%28mapping%29.md)
  Configures the line style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(domain:mapping:))*