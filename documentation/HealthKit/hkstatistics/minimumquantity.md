# minimumQuantity()

**Framework**: HealthKit  
**Kind**: method

Returns the minimum value from all the samples that match the query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func minimumQuantity() -> HKQuantity?
```

#### Return Value

If the [`discreteMin`](hkstatisticsoptions/discretemin.md) option was set, this method returns a quantity object containing the minimum value from all the samples matching the query; otherwise, it returns `nil`.

## See Also

- [var endDate: Date](hkstatistics/enddate.md)
  The end of the time period included in these statistics.
- [var startDate: Date](hkstatistics/startdate.md)
  The start of the time period included in these statistics.
- [func averageQuantity() -> HKQuantity?](hkstatistics/averagequantity.md)
  Returns the average value from all the samples that match the query.
- [func averageQuantity(for: HKSource) -> HKQuantity?](hkstatistics/averagequantity(for:).md)
  Returns the average value from all the samples that match the query and that were created by the specified source.
- [func maximumQuantity() -> HKQuantity?](hkstatistics/maximumquantity.md)
  Returns the maximum value from all the samples that match the query.
- [func maximumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/maximumquantity(for:).md)
  Returns the maximum value from all the samples that match the query and that were created by the specified source.
- [func minimumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/minimumquantity(for:).md)
  Returns the minimum value from all the samples that match the query and that were created by the specified source.
- [func sumQuantity() -> HKQuantity?](hkstatistics/sumquantity.md)
  Returns the sum of all the samples that match the query.
- [func sumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/sumquantity(for:).md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](hkstatistics/duration.md)
  Returns the total duration covering all the samples that match the query.
- [func duration(for: HKSource) -> HKQuantity?](hkstatistics/duration(for:).md)
  Returns the total duration covering all the samples created by the specified source that also match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/minimumquantity())*