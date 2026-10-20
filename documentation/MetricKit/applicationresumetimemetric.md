# ApplicationResumeTimeMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures app resume time durations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct ApplicationResumeTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.applicationResumeTime(_:)`](./metricresult/applicationresumetime%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](./applicationresumetimemetric/histogram.md)
  Histogram of application resume time durations.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Launch and responsiveness metrics
- [struct TimeToFirstDrawMetric](./timetofirstdrawmetric.md)
  A metric that measures time to first draw durations for app launches.
- [struct OptimizedTimeToFirstDrawMetric](./optimizedtimetofirstdrawmetric.md)
  A metric that measures optimized time to first draw durations for app launches.
- [struct ExtendedLaunchMetric](./extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](./hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](./hitchtimemetric.md)
  A metric that measures animation hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/applicationresumetimemetric)*