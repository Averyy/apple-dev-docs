# intervalComponents

**Framework**: HealthKit  
**Kind**: property

The date components that define the time interval for each statistics object in the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var intervalComponents: DateComponents { get }
```

#### Discussion

This property defines the length of the time intervals for your collection. The following code sample shows a number of common time intervals.

## See Also

- [var anchorDate: Date](hkstatisticscollectionquery/anchordate.md)
  The anchor date for the collection’s time intervals.
- [var options: HKStatisticsOptions](hkstatisticscollectionquery/options.md)
  A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/intervalcomponents)*