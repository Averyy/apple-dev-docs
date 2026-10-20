# cumulativeSum

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

An option indicating that the system calculates the sum of all the quantities for the samples.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var cumulativeSum: HKStatisticsOptions { get }
```

```c
HKStatisticsOptionCumulativeSum
```

## See Also

### Constants
- [static var separateBySource: HKStatisticsOptions](./separatebysource.md)
  An option indicating that the system calculates the specified statistics separately for each source.
- [static var discreteAverage: HKStatisticsOptions](./discreteaverage.md)
  An option indicating that the system calculates the average quantity for the samples.
- [static var discreteMin: HKStatisticsOptions](./discretemin.md)
  An option indicating that the system calculates the minimum quantity for the samples.
- [static var discreteMax: HKStatisticsOptions](./discretemax.md)
  An option indicating that the system calculates the maximum quantity for the samples.
- [static var mostRecent: HKStatisticsOptions](./mostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
- [static var duration: HKStatisticsOptions](./duration.md)
  An option indicating that the system calculates the total duration covering all the samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/cumulativesum)*