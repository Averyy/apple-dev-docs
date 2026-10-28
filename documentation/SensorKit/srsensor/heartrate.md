# heartRate

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that provides the user’s heart rate data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
static let heartRate: SRSensor
```

```c
extern SRSensor const SRSensorHeartRate;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`CMHighFrequencyHeartRateData`](../../CoreMotion/cmhighfrequencyheartratedata.md).

You need to provide a reason to record heart rates by adding the [`SRSensorUsageHeartRate`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusageheartrate.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading user activity sensors
- [static let accelerometer: SRSensor](./accelerometer.md)
  A sensor that provides acceleration motion data.
- [static let faceMetrics: SRSensor](./facemetrics.md)
  A sensor that provides data describing a user’s face.
- [static let mediaEvents: SRSensor](./mediaevents.md)
  A sensor that provides information about interactions with media, such as images and videos, in messaging apps.
- [static let odometer: SRSensor](./odometer.md)
  A sensor that provides information about speed and slope.
- [static let pedometerData: SRSensor](./pedometerdata.md)
  A sensor that provides information about the user’s steps.
- [static let rotationRate: SRSensor](./rotationrate.md)
  A sensor that provides rotation motion data.
- [static let siriSpeechMetrics: SRSensor](./sirispeechmetrics.md)
  A sensor that provides data describing a user’s speech to Siri.
- [static let telephonySpeechMetrics: SRSensor](./telephonyspeechmetrics.md)
  A sensor that provides data describing speech during phone calls.
- [static let visits: SRSensor](./visits.md)
  A sensor that provides information about frequently visited locations.
- [static let wristTemperature: SRSensor](./wristtemperature.md)
  A sensor that provides wrist temperature while the user sleeps.
- [static let photoplethysmogram: SRSensor](./photoplethysmogram.md)
  A sensor that streams sample PPG sensor data.
- [static let electrocardiogram: SRSensor](./electrocardiogram.md)
  A sensor that streams sample ECG sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/heartrate)*