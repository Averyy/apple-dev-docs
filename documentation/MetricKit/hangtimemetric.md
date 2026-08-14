# HangTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures app hang time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct HangTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.hangTime(_:)`](metricresult/hangtime(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

Hang durations that exceed 9 seconds of wall clock time are reported in the histogram’s final bucket.

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](hangtimemetric/histogram.md)
  Histogram of application hang time durations.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct TimeToFirstDrawMetric](timetofirstdrawmetric.md)
  A metric that measures time to first draw durations for app launches.
- [struct OptimizedTimeToFirstDrawMetric](optimizedtimetofirstdrawmetric.md)
  A metric that measures optimized time to first draw durations for app launches.
- [struct ApplicationResumeTimeMetric](applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/hangtimemetric)*