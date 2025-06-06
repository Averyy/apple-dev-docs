# chartSymbolSizeScale(domain:mapping:)

**Framework**: SwiftUI  
**Kind**: method

Configures the symbol size scale for charts.

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
func chartSymbolSizeScale<Domain>(domain: Domain, mapping: @escaping (Domain.Element) -> CGFloat) -> some View where Domain : Collection, Domain.Element : Plottable
```

## Parameters

- `domain`: The possible data values plotted as symbol size in the chart.
- `mapping`: Maps data categories to symbol sizes.

## See Also

- [func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) -> some View](view/chartsymbolsizescale(_:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartsymbolsizescale(domain:range:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartsymbolsizescale(domain:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some View](view/chartsymbolsizescale(mapping:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartsymbolsizescale(range:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale(type: ScaleType?) -> some View](view/chartsymbolsizescale(type:).md)
  Configures the symbol size scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolsizescale(domain:mapping:))*