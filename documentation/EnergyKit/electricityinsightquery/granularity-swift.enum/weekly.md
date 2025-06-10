# ElectricityInsightQuery.Granularity.weekly

**Framework**: EnergyKit  
**Kind**: case

A weekly aggregated insight record for at least six months.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case weekly
```

#### Discussion

The data period returns insight records aggregated by week for at least six calendar months, and includes the requested date range, potentially starting before the query date. In the data range, the data begins on the first Monday of January or the first Monday of July. Data ends on the first Monday of July or the first Monday of January or the last available data for the query.

## See Also

- [ElectricityInsightQuery.Granularity.daily](electricityinsightquery/granularity-swift.enum/daily.md)
  A daily aggregated insight record for at least one calendar month.
- [ElectricityInsightQuery.Granularity.hourly](electricityinsightquery/granularity-swift.enum/hourly.md)
  An hourly aggregated insight record for at least one calendar week.
- [ElectricityInsightQuery.Granularity.monthly](electricityinsightquery/granularity-swift.enum/monthly.md)
  A monthly aggregated insight record for at least 1 calendar year.
- [ElectricityInsightQuery.Granularity.yearly](electricityinsightquery/granularity-swift.enum/yearly.md)
  A yearly aggregated insight record for at least one calendar year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/granularity-swift.enum/weekly)*