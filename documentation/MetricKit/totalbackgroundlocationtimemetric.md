# TotalBackgroundLocationTimeMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the total time the app spent in the background using location services.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct TotalBackgroundLocationTimeMetric
```

## Discussion

This metric corresponds to the [`MetricResult.totalBackgroundLocationTime(_:)`](./metricresult/totalbackgroundlocationtime%28_%29.md) case. It appears in both [`intervalEntries`](./metricreport/intervalentries.md) and [`stateEntries`](./metricreport/stateentries.md) when state reporting is enabled.

## Topics

### Measurements
- [let value: Measurement<UnitDuration>](./totalbackgroundlocationtimemetric/value.md)
  The total time the app is in the background and using location services.

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
- [struct TotalBackgroundTimeMetric](./totalbackgroundtimemetric.md)
  A metric that measures the total time the app spent active in the background.
- [struct TotalBackgroundAudioTimeMetric](./totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct LocationActivityTimeMetric](./locationactivitytimemetric.md)
  A metric that measures time spent using location services at each accuracy level.
- [struct CellularConditionTimeMetric](./cellularconditiontimemetric.md)
  A metric that measures time spent at each cellular signal strength.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/totalbackgroundlocationtimemetric)*