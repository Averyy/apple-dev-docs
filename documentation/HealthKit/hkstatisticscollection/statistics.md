# statistics()

**Framework**: HealthKit  
**Kind**: method

Returns an array of statistics objects representing the populated time intervals covered by the statistics collection query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func statistics() -> [HKStatistics]
```

#### Return Value

An array of statistics objects. The statistics objects are sorted in chronological order.

#### Discussion

The resulting array contains a statistics object for each time interval that has at least one sample that matches the query. The statistics objects are returned in chronological order, but they are not necessarily contiguous. This method ignores time intervals that do not have any samples. As a result, there may be arbitrarily large gaps in time between adjacent statistics objects in the array.

## See Also

- [func statistics(for: Date) -> HKStatistics?](hkstatisticscollection/statistics(for:).md)
  Returns the statistics object for the time interval that contains the provided date.
- [func enumerateStatistics(from: Date, to: Date, with: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)](hkstatisticscollection/enumeratestatistics(from:to:with:).md)
  Enumerates the statistics objects for all the time intervals from the start date until the end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/statistics())*