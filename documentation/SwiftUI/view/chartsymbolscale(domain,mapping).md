# chartSymbolScale(domain:mapping:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Symbol scales
- [func chartSymbolScale(_:)](./chartsymbolscale%28_%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<Domain>(domain: Domain) -> some View](./chartsymbolscale%28domain%29.md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale(domain:range:)](./chartsymbolscale%28domain,range%29.md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](./chartsymbolscale%28mapping%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](./chartsymbolscale%28range%29.md)
  Configures the symbol style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:mapping:))*