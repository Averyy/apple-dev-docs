# telephonySpeechMetrics

**Framework**: SensorKit  
**Kind**: property

A sensor that provides data describing speech during phone calls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let telephonySpeechMetrics: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRSpeechMetrics`](srspeechmetrics.md).

The metrics provide details about the user’s voice, such as tenor, pitch, cadence, and speech timing, which includes words per minute and the average duration between words.

This sensor doesn’t provide raw audio data.

You need to provide a reason to analyze speech by adding the [`SRSensorUsageSpeechMetrics`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageSpeechMetrics) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let accelerometer: SRSensor](srsensor/accelerometer.md)
  A sensor that provides acceleration motion data.
- [static let faceMetrics: SRSensor](srsensor/facemetrics.md)
  A sensor that provides data describing a user’s face.
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
- [static let visits: SRSensor](srsensor/visits.md)
  A sensor that provides information about frequently visited locations.
- [static let wristTemperature: SRSensor](srsensor/wristtemperature.md)
  A sensor that provides wrist temperature while the user sleeps.
- [static let photoplethysmogram: SRSensor](srsensor/photoplethysmogram.md)
  A sensor that streams sample PPG sensor data.
- [static let electrocardiogram: SRSensor](srsensor/electrocardiogram.md)
  A sensor that streams sample ECG sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/telephonyspeechmetrics)*