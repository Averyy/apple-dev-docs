# TotalBackgroundTimeMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the total time the app spent active in the background.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct TotalBackgroundTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.totalBackgroundTime(_:)`](./metricresult/totalbackgroundtime%28_%29.md) case. It appears in both [`intervalEntries`](./metricreport/intervalentries.md) and [`stateEntries`](./metricreport/stateentries.md) when state reporting is enabled.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](./totalbackgroundtimemetric/value.md)
  The total time the app is active in the background.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Time-in-use metrics
- [struct TotalForegroundTimeMetric](./totalforegroundtimemetric.md)
  A metric that measures the total time the app spent in the foreground.
- [struct TotalBackgroundAudioTimeMetric](./totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct TotalBackgroundLocationTimeMetric](./totalbackgroundlocationtimemetric.md)
  A metric that measures the total time the app spent in the background using location services.
- [struct LocationActivityTimeMetric](./locationactivitytimemetric.md)
  A metric that measures time spent using location services at each accuracy level.
- [struct CellularConditionTimeMetric](./cellularconditiontimemetric.md)
  A metric that measures time spent at each cellular signal strength.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalbackgroundtimemetric)*