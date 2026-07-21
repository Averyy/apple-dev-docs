# ApplicationResumeTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures app resume time durations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ApplicationResumeTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.applicationResumeTime(_:)`](metricresult/applicationresumetime(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](applicationresumetimemetric/histogram.md)
  Histogram of application resume time durations.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct TimeToFirstDrawMetric](timetofirstdrawmetric.md)
  A metric that measures time to first draw durations for app launches.
- [struct OptimizedTimeToFirstDrawMetric](optimizedtimetofirstdrawmetric.md)
  A metric that measures optimized time to first draw durations for app launches.
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.
- [struct ScrollHitchTimeMetric](scrollhitchtimemetric.md)
  A metric that measures scroll hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/applicationresumetimemetric)*