# chartSymbolScale(_:)

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
func chartSymbolScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ChartSymbolShape
```

## Parameters

- `mapping`: Maps data categories to symbol shapes.

## See Also

- [func chartSymbolScale<Domain>(domain: Domain) -> some View](view/chartsymbolscale(domain:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale(domain:range:)](view/chartsymbolscale(domain:range:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](view/chartsymbolscale(domain:mapping:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](view/chartsymbolscale(mapping:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](view/chartsymbolscale(range:).md)
  Configures the symbol style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(_:))*