# HitchTimeMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures animation hitch time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct HitchTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.hitchTime(_:)`](./metricresult/hitchtime%28_%29.md) case. It appears in both [`intervalEntries`](./metricreport/intervalentries.md) and [`stateEntries`](./metricreport/stateentries.md) when state reporting is enabled.

The ratio is normalized against total animation duration and incorporates perceptual adjustments, making it the most accurate representation of the hitches users actually experience.

## Topics

### Measurements
- [let ratio: Measurement<HitchTimeRatio>](./hitchtimemetric/ratio.md)
  Ratio of time the application spent hitching during tracked animations.
- [let totalHitchTime: Measurement<UnitDuration>](./hitchtimemetric/totalhitchtime.md)
  Total time the application spent hitching during tracked animations.
- [let totalAnimationTime: Measurement<UnitDuration>](./hitchtimemetric/totalanimationtime.md)
  Total time the application spent animating.

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
- [struct ApplicationResumeTimeMetric](./applicationresumetimemetric.md)
  A metric that measures app resume time durations.
- [struct ExtendedLaunchMetric](./extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](./hangtimemetric.md)
  A metric that measures app hang time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/hitchtimemetric)*