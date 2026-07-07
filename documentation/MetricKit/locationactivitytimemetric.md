# LocationActivityTimeMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures time spent using location services at each accuracy level.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct LocationActivityTimeMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.locationActivityTime(_:)`](metricresult/locationactivitytime(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

This type replaces [`MXLocationActivityMetric`](mxlocationactivitymetric.md).

## Topics

### Accuracy levels
- [let bestAccuracyForNavigation: Measurement<UnitDuration>](locationactivitytimemetric/bestaccuracyfornavigation.md)
  The total time spent tracking the current location at the best accuracy for navigation.
- [let bestAccuracy: Measurement<UnitDuration>](locationactivitytimemetric/bestaccuracy.md)
  The total time spent tracking the current location at the best accuracy.
- [let tenMeters: Measurement<UnitDuration>](locationactivitytimemetric/tenmeters.md)
  The total time spent tracking the current location to an accuracy of 10 meters.
- [let oneHundredMeter: Measurement<UnitDuration>](locationactivitytimemetric/onehundredmeter.md)
  The total time spent tracking the current location to an accuracy of 100 meters.
- [let oneKilometer: Measurement<UnitDuration>](locationactivitytimemetric/onekilometer.md)
  The total time spent tracking the current location to an accuracy of 1 kilometer.
- [let threeKilometers: Measurement<UnitDuration>](locationactivitytimemetric/threekilometers.md)
  The total time spent tracking the current location to an accuracy of 3 kilometers.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct TotalForegroundTimeMetric](totalforegroundtimemetric.md)
  A metric that measures the total time the app spent in the foreground.
- [struct TotalBackgroundTimeMetric](totalbackgroundtimemetric.md)
  A metric that measures the total time the app spent active in the background.
- [struct TotalBackgroundAudioTimeMetric](totalbackgroundaudiotimemetric.md)
  A metric that measures the total time the app spent in the background playing audio.
- [struct TotalBackgroundLocationTimeMetric](totalbackgroundlocationtimemetric.md)
  A metric that measures the total time the app spent in the background using location services.
- [struct CellularConditionTimeMetric](cellularconditiontimemetric.md)
  A metric that measures time spent at each cellular signal strength.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/locationactivitytimemetric)*