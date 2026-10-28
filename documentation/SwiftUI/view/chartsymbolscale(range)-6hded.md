# chartSymbolScale(range:)

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
func chartSymbolScale<Range>(range: Range) -> some View where Range : ScaleRange, Range.VisualValue : ChartSymbolShape
```

**Other overloads**:

```swift
nonisolated
func chartSymbolScale(range: [any ChartSymbolShape]) -> some View
```

## Parameters

- `range`: The range of symbols that correspond to the scale domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(range:)-6hded)*