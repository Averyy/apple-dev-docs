# OptimizedTimeToFirstDrawMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures optimized time to first draw durations for app launches.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct OptimizedTimeToFirstDrawMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.optimizedTimeToFirstDraw(_:)`](metricresult/optimizedtimetofirstdraw(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

Optimized time to first draw reflects the actual user-perceived launch time when the system applies prefetching optimizations. The system may start the app in the background before the user taps its icon, so this metric can be shorter than [`TimeToFirstDrawMetric`](timetofirstdrawmetric.md).

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](optimizedtimetofirstdrawmetric/histogram.md)
  Histogram of optimized time to first draw durations.

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
- [struct ApplicationResumeTimeMetric](applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/optimizedtimetofirstdrawmetric)*