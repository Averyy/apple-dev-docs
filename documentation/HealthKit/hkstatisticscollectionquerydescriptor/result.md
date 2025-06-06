# HKStatisticsCollectionQueryDescriptor.Result

**Framework**: HealthKit  
**Kind**: struct

A collection of results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Result
```

#### Overview

The first set of results reflects the current state of the statistics collection. Additional results represent updates to the collection. When possible, HealthKit populates the `updateStatistics` property to indicate which statistics have changed.

## Topics

### Accessing Statistical Data
- [let statisticsCollection: HKStatisticsCollection](hkstatisticscollectionquerydescriptor/result/statisticscollection.md)
  A collection of statistics, representing the results calculated over separate time intervals.
- [let updatedStatistics: [HKStatistics]?](hkstatisticscollectionquerydescriptor/result/updatedstatistics.md)
  A collection of statistics that have changed.

## See Also

- [HKStatisticsCollectionQueryDescriptor.Results.Iterator](hkstatisticscollectionquerydescriptor/results/iterator.md)
  An iterator for statistics collection query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/result)*