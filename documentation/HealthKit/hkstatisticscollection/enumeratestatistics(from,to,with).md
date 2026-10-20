# enumerateStatistics(from:to:with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Enumerates the statistics objects for all the time intervals from the start date until the end date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateStatistics(from startDate: Date, to endDate: Date, with block: @escaping (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateStatisticsFromDate:(NSDate *) startDate toDate:(NSDate *) endDate withBlock:(void (^)(HKStatistics *result, BOOL *stop)) block;
```

#### Discussion

This method enumerates the statistics in chronological order. It calls the block once for each time interval between the start and end dates. If there are no samples for a particular time interval, the corresponding statistic object has a `nil`-valued quantity.

## Parameters

- `startDate`: The start date for the calculation. The initial statistics come from the time interval that contains the start date.
- `endDate`: The end date for the calculation. The final statistics come from the time interval that contains the end date.
- `block`: A block that is called once for each time interval. This method passes the following parameters to the block:

  - **result**: The [`HKStatistics`](../hkstatistics.md) object containing the statistical data for this time interval.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the collection. The stop argument is an out-only argument. Only set this Boolean to [`true`](../../Swift/true.md) within the block.

## See Also

### Accessing Statistics Collections
- [func statistics() -> [HKStatistics]](./statistics%28%29.md)
  Returns an array of statistics objects representing the populated time intervals covered by the statistics collection query.
- [func statistics(for: Date) -> HKStatistics?](./statistics%28for%29.md)
  Returns the statistics object for the time interval that contains the provided date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/enumeratestatistics(from:to:with:))*