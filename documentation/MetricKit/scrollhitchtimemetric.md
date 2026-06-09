# ScrollHitchTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures scroll hitch time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ScrollHitchTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.scrollHitchTime(_:)`](metricresult/scrollhitchtime(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

This type replaces the `scrollHitchTimeRatio` property of [`MXAnimationMetric`](mxanimationmetric.md).

## Topics

### Measurements
- [let ratio: Measurement<Unit>](scrollhitchtimemetric/ratio.md)
  Ratio of time the application spent hitching while scrolling.
- [let totalHitchTime: Measurement<UnitDuration>](scrollhitchtimemetric/totalhitchtime.md)
  Total time the application spent hitching while scrolling.
- [let totalScrollTime: Measurement<UnitDuration>](scrollhitchtimemetric/totalscrolltime.md)
  Total time the application spent scrolling.

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
- [struct ExtendedLaunchMetric](extendedlaunchmetric.md)
  A metric that measures extended launch task durations.
- [struct HangTimeMetric](hangtimemetric.md)
  A metric that measures app hang time.
- [struct HitchTimeMetric](hitchtimemetric.md)
  A metric that measures animation hitch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/scrollhitchtimemetric)*