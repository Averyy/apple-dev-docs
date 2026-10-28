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
func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape]) -> some View where Domain : ScaleDomain
```

**Other overloads**:

```swift
nonisolated
func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ChartSymbolShape
```

## Parameters

- `domain`: The possible data values plotted as symbols in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)
- `range`: The range of symbols that correspond to the scale domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:range:)-8nmd6)*