# discreteMostRecent

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

An option indicating that the system returns the most recent quantity from the matching samples.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0 (renamed: HKStatisticsOptions.mostRecent)
- iPadOS 12.0+ - Deprecated in 13.0 (renamed: HKStatisticsOptions.mostRecent)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: HKStatisticsOptions.mostRecent)
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: HKStatisticsOptions.mostRecent)
- watchOS 5.0+ - Deprecated in 6.0 (renamed: HKStatisticsOptions.mostRecent)

> **Deprecated**: Use [`mostRecent`](./mostrecent.md) instead.

## Declaration

```swift
static var discreteMostRecent: HKStatisticsOptions { get }
```

```c
HKStatisticsOptionDiscreteMostRecent
```

## See Also

### Related Documentation
- [func mostRecentQuantity() -> HKQuantity?](../hkstatistics/mostrecentquantity%28%29.md)
  Returns the most recent value from all the samples that match the query.
- [func mostRecentQuantity(for: HKSource) -> HKQuantity?](../hkstatistics/mostrecentquantity%28for%29.md)
  Returns the most recent value from all the samples that match the query and were created by the specified source.
- [func mostRecentQuantityDateInterval() -> DateInterval?](../hkstatistics/mostrecentquantitydateinterval%28%29.md)
  Returns the date interval of the most recent sample that matches the query.
- [func mostRecentQuantityDateInterval(for: HKSource) -> DateInterval?](../hkstatistics/mostrecentquantitydateinterval%28for%29.md)
  Returns the date interval of the most recent sample that matches the query and was created by the specified source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/discretemostrecent)*