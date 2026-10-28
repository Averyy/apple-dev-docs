# maximumQuantity(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the maximum value from all the samples that match the query and that were created by the specified source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func maximumQuantity(for source: HKSource) -> HKQuantity?
```

```objc
- (HKQuantity *) maximumQuantityForSource:(HKSource *) source;
```

## Return Value

If both the [`discreteMax`](../hkstatisticsoptions/discretemax.md) option and the [`separateBySource`](../hkstatisticsoptions/separatebysource.md) option were set, this method returns a quantity object. This object contains the maximum value from all the samples that match the query and were created by the specified source. If the statistics options were not both set, this method returns `nil`.

## Parameters

- `source`: A data source from the statistics object’s [`sources`](./sources.md) array.

## See Also

### Related Documentation
- [var endDate: Date](./enddate.md)
  The end of the time period included in these statistics.
- [var sources: [HKSource]?](./sources.md)
  An array containing all the sources contributing to these statistics.
- [var startDate: Date](./startdate.md)
  The start of the time period included in these statistics.
### Getting Statistics Data
- [func averageQuantity() -> HKQuantity?](./averagequantity%28%29.md)
  Returns the average value from all the samples that match the query.
- [func averageQuantity(for: HKSource) -> HKQuantity?](./averagequantity%28for%29.md)
  Returns the average value from all the samples that match the query and that were created by the specified source.
- [func maximumQuantity() -> HKQuantity?](./maximumquantity%28%29.md)
  Returns the maximum value from all the samples that match the query.
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
- [func duration(for: HKSource) -> HKQuantity?](./duration%28for%29.md)
  Returns the total duration covering all the samples created by the specified source that also match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/maximumquantity(for:))*