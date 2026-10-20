# ElectricityInsightQuery.Granularity.monthly

**Framework**: EnergyKit  
**Kind**: case  
**Role**: Case

A monthly aggregated insight record for at least 1 calendar year.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
case monthly
```

#### Discussion

The data period returns insight records aggregated by month for at least one calendar year, and includes the requested date range, potentially starting before the query date. The data range begins and ends in a month or the last available data for the query.

## See Also

### Returning electricity insight records
- [ElectricityInsightQuery.Granularity.daily](./daily.md)
  A daily aggregated insight record for at least one calendar month.
- [ElectricityInsightQuery.Granularity.hourly](./hourly.md)
  An hourly aggregated insight record for at least one calendar week.
- [ElectricityInsightQuery.Granularity.weekly](./weekly.md)
  A weekly aggregated insight record for at least six months.
- [ElectricityInsightQuery.Granularity.yearly](./yearly.md)
  A yearly aggregated insight record for at least one calendar year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/granularity-swift.enum/monthly)*