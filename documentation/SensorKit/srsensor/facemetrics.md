# faceMetrics

**Framework**: SensorKit  
**Kind**: property

A sensor that provides data describing a user’s face.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
static let faceMetrics: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRFaceMetrics`](srfacemetrics.md).

You need to provide a reason to record face metrics by adding the [`SRSensorUsageFacialMetrics`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageFacialMetrics) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let accelerometer: SRSensor](srsensor/accelerometer.md)
  A sensor that provides acceleration motion data.
- [static let heartRate: SRSensor](srsensor/heartrate.md)
  A sensor that provides the user’s heart rate data.
- [static let mediaEvents: SRSensor](srsensor/mediaevents.md)
  A sensor that provides information about interactions with media, such as images and videos, in messaging apps.
- [static let odometer: SRSensor](srsensor/odometer.md)
  A sensor that provides information about speed and slope.
- [static let pedometerData: SRSensor](srsensor/pedometerdata.md)
  A sensor that provides information about the user’s steps.
- [static let rotationRate: SRSensor](srsensor/rotationrate.md)
  A sensor that provides rotation motion data.
- [static let siriSpeechMetrics: SRSensor](srsensor/sirispeechmetrics.md)
  A sensor that provides data describing a user’s speech to Siri.
- [static let telephonySpeechMetrics: SRSensor](srsensor/telephonyspeechmetrics.md)
  A sensor that provides data describing speech during phone calls.
- [static let visits: SRSensor](srsensor/visits.md)
  A sensor that provides information about frequently visited locations.
- [static let wristTemperature: SRSensor](srsensor/wristtemperature.md)
  A sensor that provides wrist temperature while the user sleeps.
- [static let photoplethysmogram: SRSensor](srsensor/photoplethysmogram.md)
  A sensor that streams sample PPG sensor data.
- [static let electrocardiogram: SRSensor](srsensor/electrocardiogram.md)
  A sensor that streams sample ECG sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/facemetrics)*