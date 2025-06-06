# statistics(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the statistics object for the time interval that contains the provided date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func statistics(for date: Date) -> HKStatistics?
```

#### Return Value

A statistics object for the time interval containing the provided date. If there are no samples for the selected time interval, the statistics object has a `nil`-valued quantity.

## Parameters

- `date`: The target date.

## See Also

- [func statistics() -> [HKStatistics]](hkstatisticscollection/statistics.md)
  Returns an array of statistics objects representing the populated time intervals covered by the statistics collection query.
- [func enumerateStatistics(from: Date, to: Date, with: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)](hkstatisticscollection/enumeratestatistics(from:to:with:).md)
  Enumerates the statistics objects for all the time intervals from the start date until the end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/statistics(for:))*