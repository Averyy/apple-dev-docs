# chartSymbolSizeScale(domain:range:type:)

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
func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == CGFloat
```

## Parameters

- `domain`: The possible data values plotted as symbol sizes in   the chart. You can define the domain with an array for   categorical values (e.g.,  )
- `range`: The range of symbol size that correspond to the   scale domain.
- `type`: The scale type.

## See Also

- [func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) -> some View](view/chartsymbolsizescale(_:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartsymbolsizescale(domain:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element) -> CGFloat) -> some View](view/chartsymbolsizescale(domain:mapping:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some View](view/chartsymbolsizescale(mapping:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartsymbolsizescale(range:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale(type: ScaleType?) -> some View](view/chartsymbolsizescale(type:).md)
  Configures the symbol size scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolsizescale(domain:range:type:))*