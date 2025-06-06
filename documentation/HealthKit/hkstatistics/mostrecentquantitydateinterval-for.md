# mostRecentQuantityDateInterval(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the date interval of the most recent sample that matches the query and was created by the specified source.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func mostRecentQuantityDateInterval(for source: HKSource) -> DateInterval?
```

## See Also

- [static var discreteMostRecent: HKStatisticsOptions](hkstatisticsoptions/discretemostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
- [func mostRecentQuantity() -> HKQuantity?](hkstatistics/mostrecentquantity.md)
  Returns the most recent value from all the samples that match the query.
- [func mostRecentQuantity(for: HKSource) -> HKQuantity?](hkstatistics/mostrecentquantity(for:).md)
  Returns the most recent value from all the samples that match the query and were created by the specified source.
- [func mostRecentQuantityDateInterval() -> DateInterval?](hkstatistics/mostrecentquantitydateinterval.md)
  Returns the date interval of the most recent sample that matches the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/mostrecentquantitydateinterval(for:))*