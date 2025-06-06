# minimumQuantity(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the minimum value from all the samples that match the query and that were created by the specified source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func minimumQuantity(for source: HKSource) -> HKQuantity?
```

#### Return Value

If both the [`discreteMin`](hkstatisticsoptions/discretemin.md) option and the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option were set, this method returns a quantity object. This object contains the minimum value from all the samples that match the query and were created by the specified source. If the statistics options were not both set, this method returns `nil`.

## Parameters

- `source`: A data source from the statistics object’s   array.

## See Also

- [var endDate: Date](hkstatistics/enddate.md)
  The end of the time period included in these statistics.
- [var sources: [HKSource]?](hkstatistics/sources.md)
  An array containing all the sources contributing to these statistics.
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
- [func minimumQuantity() -> HKQuantity?](hkstatistics/minimumquantity.md)
  Returns the minimum value from all the samples that match the query.
- [func sumQuantity() -> HKQuantity?](hkstatistics/sumquantity.md)
  Returns the sum of all the samples that match the query.
- [func sumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/sumquantity(for:).md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](hkstatistics/duration.md)
  Returns the total duration covering all the samples that match the query.
- [func duration(for: HKSource) -> HKQuantity?](hkstatistics/duration(for:).md)
  Returns the total duration covering all the samples created by the specified source that also match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/minimumquantity(for:))*