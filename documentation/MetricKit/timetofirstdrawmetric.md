# TimeToFirstDrawMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures time to first draw durations for app launches.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct TimeToFirstDrawMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.timeToFirstDraw(_:)`](metricresult/timetofirstdraw(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

The measurement ends at the first Core Animation commit, which corresponds to the moment the first rendered frame is submitted to the display pipeline.

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](timetofirstdrawmetric/histogram.md)
  Histogram of time to first draw durations.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct OptimizedTimeToFirstDrawMetric](optimizedtimetofirstdrawmetric.md)
  A metric that measures optimized time to first draw durations for app launches.
- [struct ApplicationResumeTimeMetric](applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/timetofirstdrawmetric)*