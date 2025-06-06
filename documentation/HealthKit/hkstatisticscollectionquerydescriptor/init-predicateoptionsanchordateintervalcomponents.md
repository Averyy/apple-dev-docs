# init(predicate:options:anchorDate:intervalComponents:)

**Framework**: HealthKit  
**Kind**: init

Creates a statistics collection query descriptor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKStatisticsOptions, anchorDate: Date, intervalComponents: DateComponents)
```

## Parameters

- `predicate`: A predicate that defines the set of data that the query uses to calculate the statistics.
- `options`: A list of options that define the type of statistical calculations performed and the way in which HealthKit merges data from multiple sources. For a list of valid options, see  .
- `anchorDate`: Technically, the anchor sets the start time for a single time interval. All other time intervals must align with this interval. The time intervals can extend before or after the anchor date. Each time interval has the same length, and there’s no gap between adjacent intervals. Think of time as a number line: The anchor date represents its origin, and the intervals create tick marks that extend away from the origin in both directions.
- `intervalComponents`: The date components that define the time interval for each statistics object in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/init(predicate:options:anchordate:intervalcomponents:))*