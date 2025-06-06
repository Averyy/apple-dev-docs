# discreteMostRecent

**Framework**: HealthKit  
**Kind**: property

An option indicating that the system returns the most recent quantity from the matching samples.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var discreteMostRecent: HKStatisticsOptions { get }
```

## See Also

- [func mostRecentQuantity() -> HKQuantity?](hkstatistics/mostrecentquantity.md)
  Returns the most recent value from all the samples that match the query.
- [func mostRecentQuantity(for: HKSource) -> HKQuantity?](hkstatistics/mostrecentquantity(for:).md)
  Returns the most recent value from all the samples that match the query and were created by the specified source.
- [func mostRecentQuantityDateInterval() -> DateInterval?](hkstatistics/mostrecentquantitydateinterval.md)
  Returns the date interval of the most recent sample that matches the query.
- [func mostRecentQuantityDateInterval(for: HKSource) -> DateInterval?](hkstatistics/mostrecentquantitydateinterval(for:).md)
  Returns the date interval of the most recent sample that matches the query and was created by the specified source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/discretemostrecent)*