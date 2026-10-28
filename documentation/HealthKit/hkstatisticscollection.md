# HKStatisticsCollection

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An object that manages a collection of statistics, representing the results calculated over separate time intervals.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKStatisticsCollection
```

```objc
@interface HKStatisticsCollection : NSObject
```

## Overview

For more information on statistics objects, see [`HKStatistics`](./hkstatistics.md). For more information on calculating statistics over consecutive time intervals, see [`HKStatisticsCollectionQuery`](./hkstatisticscollectionquery.md).

## Topics

### Accessing Statistics Collections
- [func statistics() -> [HKStatistics]](./hkstatisticscollection/statistics%28%29.md)
  Returns an array of statistics objects representing the populated time intervals covered by the statistics collection query.
- [func statistics(for: Date) -> HKStatistics?](./hkstatisticscollection/statistics%28for%29.md)
  Returns the statistics object for the time interval that contains the provided date.
- [func enumerateStatistics(from: Date, to: Date, with: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)](./hkstatisticscollection/enumeratestatistics%28from,to,with%29.md)
  Enumerates the statistics objects for all the time intervals from the start date until the end date.
### Getting Information About Statistics Collections
- [func sources() -> Set<HKSource>](./hkstatisticscollection/sources%28%29.md)
  Returns a set containing all the sources that had samples matched by the statistics collection query.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Statistics
- [Executing Statistical Queries](./executing-statistical-queries.md)
  Create and run statistical queries.
- [Executing Statistics Collection Queries](./executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
- [struct HKStatisticsQueryDescriptor](./hkstatisticsquerydescriptor.md)
  A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsQuery](./hkstatisticsquery.md)
  A query that performs statistical calculations over a set of matching quantity samples, and returns the results.
- [struct HKStatisticsCollectionQueryDescriptor](./hkstatisticscollectionquerydescriptor.md)
  A query descriptor that gathers a collection of statistics calculated over a series of fixed-length time intervals.
- [class HKStatisticsCollectionQuery](./hkstatisticscollectionquery.md)
  A query that performs multiple statistics queries over a series of fixed-length time intervals.
- [class HKStatistics](./hkstatistics.md)
  An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [struct HKStatisticsOptions](./hkstatisticsoptions.md)
  Options for specifying the statistic to calculate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection)*