# CellularConditionTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures time spent at each cellular signal strength.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct CellularConditionTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.cellularConditionTime(_:)`](metricresult/cellularconditiontime(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

The histogram represents the fraction of the reporting interval spent at each cellular signal strength tier. If no cellular data was collected during the interval, the histogram is empty.

## Topics

### Measurements
- [let histogram: Histogram<SignalBars>](cellularconditiontimemetric/histogram.md)
  Histogram of cellular condition time.

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
- [struct TotalBackgroundTimeMetric](totalbackgroundtimemetric.md)
  A metric that measures the total time the app spent active in the background.
- [struct TotalBackgroundAudioTimeMetric](totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct TotalBackgroundLocationTimeMetric](totalbackgroundlocationtimemetric.md)
  A metric that measures the total time the app spent in the background using location services.
- [struct LocationActivityTimeMetric](locationactivitytimemetric.md)
  A metric that measures time spent using location services at each accuracy level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/cellularconditiontimemetric)*