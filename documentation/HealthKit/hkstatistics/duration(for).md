# duration(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the total duration covering all the samples created by the specified source that also match the query.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func duration(for source: HKSource) -> HKQuantity?
```

#### Discussion

If you set both the [`duration`](hkstatisticsoptions/duration.md) and [`separateBySource`](hkstatisticsoptions/separatebysource.md) options, this method returns a quantity object. This object contains the total duration covering all the samples created by the specified source that also match the query. If the statistics options were not both set, this method returns `nil`.

## See Also

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
- [func minimumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/minimumquantity(for:).md)
  Returns the minimum value from all the samples that match the query and that were created by the specified source.
- [func sumQuantity() -> HKQuantity?](hkstatistics/sumquantity.md)
  Returns the sum of all the samples that match the query.
- [func sumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/sumquantity(for:).md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](hkstatistics/duration.md)
  Returns the total duration covering all the samples that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/duration(for:))*