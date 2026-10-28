# chartSymbolScale(_:)

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
func chartSymbolScale<DataValue>(_ mapping: KeyValuePairs<DataValue, any ChartSymbolShape>) -> some View where DataValue : Plottable
```

**Other overloads**:

```swift
nonisolated
func chartSymbolScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ChartSymbolShape
```

## Parameters

- `mapping`: Maps data categories to symbol shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(_:)-58llj)*