# ElectricityInsightQuery.Granularity

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

The specific temporal granularity of electricity insight records.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
enum Granularity
```

## Mentions

- [Providing charging history for electric vehicles](../providing-informative-charging-history-for-electric-vehicles.md)

## Topics

### Returning electricity insight records
- [ElectricityInsightQuery.Granularity.daily](./granularity-swift.enum/daily.md)
  A daily aggregated insight record for at least one calendar month.
- [ElectricityInsightQuery.Granularity.hourly](./granularity-swift.enum/hourly.md)
  An hourly aggregated insight record for at least one calendar week.
- [ElectricityInsightQuery.Granularity.monthly](./granularity-swift.enum/monthly.md)
  A monthly aggregated insight record for at least 1 calendar year.
- [ElectricityInsightQuery.Granularity.weekly](./granularity-swift.enum/weekly.md)
  A weekly aggregated insight record for at least six months.
- [ElectricityInsightQuery.Granularity.yearly](./granularity-swift.enum/yearly.md)
  A yearly aggregated insight record for at least one calendar year.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the query request information
- [let granularity: ElectricityInsightQuery.Granularity](./granularity-swift.property.md)
  The temporal granularity for returned electricity insight records.
- [let flowDirection: ElectricityFlowDirection](./flowdirection.md)
  A property that specifies whether the response contains imported or exported energy.
- [let range: DateInterval](./range.md)
  The requested date range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/granularity-swift.enum)*