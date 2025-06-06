# duration

**Framework**: HealthKit  
**Kind**: property

An option indicating that the system calculates the total duration covering all the samples.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var duration: HKStatisticsOptions { get }
```

## See Also

- [static var separateBySource: HKStatisticsOptions](hkstatisticsoptions/separatebysource.md)
  An option indicating that the system calculates the specified statistics separately for each source.
- [static var discreteAverage: HKStatisticsOptions](hkstatisticsoptions/discreteaverage.md)
  An option indicating that the system calculates the average quantity for the samples.
- [static var discreteMin: HKStatisticsOptions](hkstatisticsoptions/discretemin.md)
  An option indicating that the system calculates the minimum quantity for the samples.
- [static var discreteMax: HKStatisticsOptions](hkstatisticsoptions/discretemax.md)
  An option indicating that the system calculates the maximum quantity for the samples.
- [static var cumulativeSum: HKStatisticsOptions](hkstatisticsoptions/cumulativesum.md)
  An option indicating that the system calculates the sum of all the quantities for the samples.
- [static var mostRecent: HKStatisticsOptions](hkstatisticsoptions/mostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions/duration)*