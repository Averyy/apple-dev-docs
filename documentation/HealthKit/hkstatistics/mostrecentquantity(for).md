# mostRecentQuantity(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the most recent value from all the samples that match the query and were created by the specified source.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func mostRecentQuantity(for source: HKSource) -> HKQuantity?
```

```objc
- (HKQuantity *) mostRecentQuantityForSource:(HKSource *) source;
```

## See Also

### Related Documentation
- [static var discreteMostRecent: HKStatisticsOptions](../hkstatisticsoptions/discretemostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
### Getting the Most Recent Quantity
- [func mostRecentQuantity() -> HKQuantity?](./mostrecentquantity%28%29.md)
  Returns the most recent value from all the samples that match the query.
- [func mostRecentQuantityDateInterval() -> DateInterval?](./mostrecentquantitydateinterval%28%29.md)
  Returns the date interval of the most recent sample that matches the query.
- [func mostRecentQuantityDateInterval(for: HKSource) -> DateInterval?](./mostrecentquantitydateinterval%28for%29.md)
  Returns the date interval of the most recent sample that matches the query and was created by the specified source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/mostrecentquantity(for:))*