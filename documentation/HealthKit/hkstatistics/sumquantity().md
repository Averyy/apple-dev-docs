# sumQuantity()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the sum of all the samples that match the query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sumQuantity() -> HKQuantity?
```

```objc
- (HKQuantity *) sumQuantity;
```

## Mentions

- [Executing Statistics Collection Queries](../executing-statistics-collection-queries.md)

#### Return Value

If the [`cumulativeSum`](../hkstatisticsoptions/cumulativesum.md) option was set, this method returns a quantity object containing the sum of all the samples matching the query; otherwise, it returns `nil`.

## See Also

### Related Documentation
- [var endDate: Date](./enddate.md)
  The end of the time period included in these statistics.
- [var startDate: Date](./startdate.md)
  The start of the time period included in these statistics.
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
- [func sumQuantity(for: HKSource) -> HKQuantity?](./sumquantity%28for%29.md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](./duration%28%29.md)
  Returns the total duration covering all the samples that match the query.
- [func duration(for: HKSource) -> HKQuantity?](./duration%28for%29.md)
  Returns the total duration covering all the samples created by the specified source that also match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/sumquantity())*