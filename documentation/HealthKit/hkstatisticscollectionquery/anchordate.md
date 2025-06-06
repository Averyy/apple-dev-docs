# anchorDate

**Framework**: HealthKit  
**Kind**: property

The anchor date for the collection’s time intervals.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var anchorDate: Date { get }
```

#### Discussion

The date used to anchor the collection’s time intervals.

Use the anchor date to set the start time for your time intervals. For example, if you are using a day interval, you might create a date object with a time of 2:00 a.m. This value sets the start of each day for all of your time intervals.

Technically, the anchor sets the start time for a single time interval. All other time intervals must align with this interval. The time intervals can extend before or after the anchor date. Each time interval has the same length, and there is no gap between adjacent intervals.  Think of time as a number line: The anchor date represents its origin, with the intervals creating tick marks that extend away from the origin in both directions.

## See Also

- [var intervalComponents: DateComponents](hkstatisticscollectionquery/intervalcomponents.md)
  The date components that define the time interval for each statistics object in the collection.
- [var options: HKStatisticsOptions](hkstatisticscollectionquery/options.md)
  A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/anchordate)*