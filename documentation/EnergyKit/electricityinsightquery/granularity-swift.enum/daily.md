# ElectricityInsightQuery.Granularity.daily

**Framework**: EnergyKit  
**Kind**: case

A daily aggregated insight record for at least one calendar month.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
case daily
```

#### Discussion

The data period returns insight records aggregated by day for at least one calendar month, and includes the requested date range, potentially starting before the query date. The data range begins and ends in a month or the last available data for the query.

## See Also

- [ElectricityInsightQuery.Granularity.hourly](electricityinsightquery/granularity-swift.enum/hourly.md)
  An hourly aggregated insight record for at least one calendar week.
- [ElectricityInsightQuery.Granularity.monthly](electricityinsightquery/granularity-swift.enum/monthly.md)
  A monthly aggregated insight record for at least 1 calendar year.
- [ElectricityInsightQuery.Granularity.weekly](electricityinsightquery/granularity-swift.enum/weekly.md)
  A weekly aggregated insight record for at least six months.
- [ElectricityInsightQuery.Granularity.yearly](electricityinsightquery/granularity-swift.enum/yearly.md)
  A yearly aggregated insight record for at least one calendar year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/granularity-swift.enum/daily)*