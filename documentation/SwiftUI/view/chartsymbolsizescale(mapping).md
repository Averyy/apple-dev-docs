# chartSymbolSizeScale(mapping:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func chartSymbolSizeScale<DataValue>(mapping: @escaping (DataValue) -> CGFloat) -> some View where DataValue : Plottable
```

## Parameters

- `mapping`: Maps data categories to symbol sizes.

## See Also

### Symbol size scales
- [func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) -> some View](./chartsymbolsizescale%28_%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartsymbolsizescale%28domain,range,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./chartsymbolsizescale%28domain,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element) -> CGFloat) -> some View](./chartsymbolsizescale%28domain,mapping%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some View](./chartsymbolsizescale%28range,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale(type: ScaleType?) -> some View](./chartsymbolsizescale%28type%29.md)
  Configures the symbol size scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolsizescale(mapping:))*