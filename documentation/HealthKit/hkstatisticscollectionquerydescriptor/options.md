# options

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A list of options that define the type of statistical calculations performed and the way in which HealthKit merges data from multiple sources.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
var options: HKStatisticsOptions
```

## See Also

### Accessing Query Properties
- [var predicate: HKSamplePredicate<HKQuantitySample>](./predicate.md)
  A predicate that defines the set of data that the query uses to calculate the statistics.
- [var anchorDate: Date](./anchordate.md)
  The date that anchors the collection’s time intervals.
- [var intervalComponents: DateComponents](./intervalcomponents.md)
  The date components that define the time interval for each statistics object in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/options)*