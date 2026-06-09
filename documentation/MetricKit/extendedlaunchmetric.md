# ExtendedLaunchMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures extended launch task durations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ExtendedLaunchMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.extendedLaunch(_:)`](metricresult/extendedlaunch(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

The end point of an extended launch is the later of the first rendered frame and the completion of all tasks you track with [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](metricmanager/tracklaunchtask(id:ontrackingerror:_:)-jnu1.md).

This type replaces the `histogrammedExtendedLaunch` property of [`MXAppLaunchMetric`](mxapplaunchmetric.md).

## Topics

### Measurements
- [let histogram: Histogram<UnitDuration>](extendedlaunchmetric/histogram.md)
  Histogram of extended launch durations.

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
- [struct ApplicationResumeTimeMetric](applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.
- [struct ScrollHitchTimeMetric](scrollhitchtimemetric.md)
  A metric that measures scroll hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/extendedlaunchmetric)*