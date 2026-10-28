# duration(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (HKQuantity *) durationForSource:(HKSource *) source;
```

## Discussion

If you set both the [`duration`](../hkstatisticsoptions/duration.md) and [`separateBySource`](../hkstatisticsoptions/separatebysource.md) options, this method returns a quantity object. This object contains the total duration covering all the samples created by the specified source that also match the query. If the statistics options were not both set, this method returns `nil`.

## See Also

### Getting Statistics Data
- [func averageQuantity() -> HKQuantity?](./averagequantity%28%29.md)
  Returns the average value from all the samples that match the query.
- [func averageQuantity(for: HKSource) -> HKQuantity?](./averagequantity%28for%29.md)
  Returns the average value from all the samples that match the query and that were created by the specified source.
- [func maximumQuantity() -> HKQuantity?](./maximumquantity%28%29.md)
  Returns the maximum value from all the samples that match the query.
- [func maximumQuantity(for: HKSource) -> HKQuantity?](./maximumquantity%28for%29.md)
  Returns the maximum value from all the samples that match the query and that were created by the specified source.
- [func minimumQuantity() -> HKQuantity?](./minimumquantity%28%29.md)
  Returns the minimum value from all the samples that match the query.
- [func minimumQuantity(for: HKSource) -> HKQuantity?](./minimumquantity%28for%29.md)
  Returns the minimum value from all the samples that match the query and that were created by the specified source.
- [func sumQuantity() -> HKQuantity?](./sumquantity%28%29.md)
  Returns the sum of all the samples that match the query.
- [func sumQuantity(for: HKSource) -> HKQuantity?](./sumquantity%28for%29.md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](./duration%28%29.md)
  Returns the total duration covering all the samples that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/duration(for:))*