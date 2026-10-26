# separateBySource

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

An option indicating that the system calculates the specified statistics separately for each source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var separateBySource: HKStatisticsOptions { get }
```

```c
HKStatisticsOptionSeparateBySource
```

## See Also

### Constants
- [static var discreteAverage: HKStatisticsOptions](./discreteaverage.md)
  An option indicating that the system calculates the average quantity for the samples.
- [static var discreteMin: HKStatisticsOptions](./discretemin.md)
  An option indicating that the system calculates the minimum quantity for the samples.
- [static var discreteMax: HKStatisticsOptions](./discretemax.md)
  An option indicating that the system calculates the maximum quantity for the samples.
- [static var cumulativeSum: HKStatisticsOptions](./cumulativesum.md)
  An option indicating that the system calculates the sum of all the quantities for the samples.
- [static var mostRecent: HKStatisticsOptions](./mostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
- [static var duration: HKStatisticsOptions](./duration.md)
  An option indicating that the system calculates the total duration covering all the samples.
- [HKStatisticsOptionNone](./hkstatisticsoptionnone.md)
  An option indicating that the system will not calculate any statistics values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/separatebysource)*