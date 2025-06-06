# chartSymbolScale(domain:mapping:)

**Framework**: SwiftUI  
**Kind**: method

Configures the symbol scale for charts.

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
func chartSymbolScale<Domain, S>(domain: Domain, mapping: @escaping (Domain.Element) -> S) -> some View where Domain : Collection, S : ChartSymbolShape, Domain.Element : Plottable
```

## Parameters

- `domain`: The possible data values plotted as symbol in the chart.
- `mapping`: Maps data categories to symbol shapes.

## See Also

- [func chartSymbolScale(_:)](view/chartsymbolscale(_:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<Domain>(domain: Domain) -> some View](view/chartsymbolscale(domain:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale(domain:range:)](view/chartsymbolscale(domain:range:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](view/chartsymbolscale(mapping:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](view/chartsymbolscale(range:).md)
  Configures the symbol style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:mapping:))*