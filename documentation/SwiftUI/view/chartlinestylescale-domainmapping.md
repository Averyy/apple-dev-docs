# chartLineStyleScale(domain:mapping:)

**Framework**: SwiftUI  
**Kind**: method

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

- [func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) -> some View](view/chartlinestylescale(_:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain) -> some View](view/chartlinestylescale(domain:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some View](view/chartlinestylescale(domain:range:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Range>(range: Range) -> some View](view/chartlinestylescale(range:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) -> some View](view/chartlinestylescale(mapping:).md)
  Configures the line style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(domain:mapping:))*