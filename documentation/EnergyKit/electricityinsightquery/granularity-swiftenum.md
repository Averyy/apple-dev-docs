# ElectricityInsightQuery.Granularity

**Framework**: EnergyKit  
**Kind**: enum

The specific temporal granularity of electricity insight records.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum Granularity
```

## Topics

### Returning electricity insight records
- [ElectricityInsightQuery.Granularity.daily](electricityinsightquery/granularity-swift.enum/daily.md)
  A daily aggregated insight record for at least one calendar month.
- [ElectricityInsightQuery.Granularity.hourly](electricityinsightquery/granularity-swift.enum/hourly.md)
  An hourly aggregated insight record for at least one calendar week.
- [ElectricityInsightQuery.Granularity.monthly](electricityinsightquery/granularity-swift.enum/monthly.md)
  A monthly aggregated insight record for at least 1 calendar year.
- [ElectricityInsightQuery.Granularity.weekly](electricityinsightquery/granularity-swift.enum/weekly.md)
  A weekly aggregated insight record for at least six months.
- [ElectricityInsightQuery.Granularity.yearly](electricityinsightquery/granularity-swift.enum/yearly.md)
  A yearly aggregated insight record for at least one calendar year.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let granularity: ElectricityInsightQuery.Granularity](electricityinsightquery/granularity-swift.property.md)
  The temporal granularity for returned electricity insight records.
- [let flowDirection: ElectricityFlowDirection](electricityinsightquery/flowdirection.md)
  A property that specifies whether the response contains imported or exported energy.
- [let range: DateInterval](electricityinsightquery/range.md)
  The requested date range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/granularity-swift.enum)*