# chartSymbolScale(domain:range:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the symbol style scale for charts.

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
func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ChartSymbolShape
```

**Other overloads**:

```swift
nonisolated
func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape]) -> some View where Domain : ScaleDomain
```

## Parameters

- `domain`: The possible data values plotted as symbols in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)
- `range`: The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales
- [func chartSymbolScale(_:)](./chartsymbolscale%28_%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<Domain>(domain: Domain) -> some View](./chartsymbolscale%28domain%29.md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](./chartsymbolscale%28domain,mapping%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](./chartsymbolscale%28mapping%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](./chartsymbolscale%28range%29.md)
  Configures the symbol style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:range:))*