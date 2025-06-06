# enumerateStatistics(from:to:with:)

**Framework**: HealthKit  
**Kind**: method

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

#### Discussion

This method enumerates the statistics in chronological order. It calls the block once for each time interval between the start and end dates. If there are no samples for a particular time interval, the corresponding statistic object has a `nil`-valued quantity.

## Parameters

- `startDate`: The start date for the calculation. The initial statistics come from the time interval that contains the start date.
- `endDate`: The end date for the calculation. The final statistics come from the time interval that contains the end date.
- `block`: A block that is called once for each time interval. This method passes the following parameters to the block:

## See Also

- [func statistics() -> [HKStatistics]](hkstatisticscollection/statistics.md)
  Returns an array of statistics objects representing the populated time intervals covered by the statistics collection query.
- [func statistics(for: Date) -> HKStatistics?](hkstatisticscollection/statistics(for:).md)
  Returns the statistics object for the time interval that contains the provided date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/enumeratestatistics(from:to:with:))*