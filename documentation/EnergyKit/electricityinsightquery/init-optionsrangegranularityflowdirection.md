# init(options:range:granularity:flowDirection:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electricity insight query request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
init(options: ElectricityInsightQuery.Options, range: DateInterval, granularity: ElectricityInsightQuery.Granularity, flowDirection: ElectricityFlowDirection)
```

## Parameters

- `options`: The optional information included when the system returns electricity insight records.
- `range`: The requested date range.
- `granularity`: The temporal granularity for returned electricity insight records.
- `flowDirection`: The direction of the flow of electricity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/init(options:range:granularity:flowdirection:))*