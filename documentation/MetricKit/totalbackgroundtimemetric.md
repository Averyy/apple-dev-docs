# TotalBackgroundTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures the total time the app spent active in the background.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct TotalBackgroundTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalBackgroundTime(_:)`](metricresult/totalbackgroundtime(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](totalbackgroundtimemetric/value.md)
  The total time the app is active in the background.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct TotalForegroundTimeMetric](totalforegroundtimemetric.md)
  A metric that measures the total time the app spent in the foreground.
- [struct TotalBackgroundAudioTimeMetric](totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct TotalBackgroundLocationTimeMetric](totalbackgroundlocationtimemetric.md)
  A metric that measures the total time the app spent in the background using location services.
- [struct LocationActivityTimeMetric](locationactivitytimemetric.md)
  A metric that measures time spent using location services at each accuracy level.
- [struct CellularConditionTimeMetric](cellularconditiontimemetric.md)
  A metric that measures time spent at each cellular signal strength.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalbackgroundtimemetric)*