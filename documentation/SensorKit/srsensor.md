# SRSensor

**Framework**: SensorKit  
**Kind**: struct

The sensors an app can read.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct SRSensor
```

## Mentions

- [Configuring your project for sensor reading](configuring-your-project-for-sensor-reading.md)

#### Discussion

Use the properties in this structure to access the different sensors.

## Topics

### Reading device sensors
- [static let deviceUsageReport: SRSensor](srsensor/deviceusagereport.md)
  A sensor that provides information about device usage.
- [static let keyboardMetrics: SRSensor](srsensor/keyboardmetrics.md)
  A sensor that provides information about keyboard usage.
- [static let onWristState: SRSensor](srsensor/onwriststate.md)
  A sensor that describes the watch’s position on the wrist.
### Reading app activity sensors
- [static let messagesUsageReport: SRSensor](srsensor/messagesusagereport.md)
  A sensor that provides information about use of the Messages app.
- [static let phoneUsageReport: SRSensor](srsensor/phoneusagereport.md)
  A sensor that reports the amount of time that the user is on phone calls.
### Reading user activity sensors
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
### Reading environment sensors
- [static let ambientLightSensor: SRSensor](srsensor/ambientlightsensor.md)
  A sensor that provides ambient light information.
- [static let ambientPressure: SRSensor](srsensor/ambientpressure.md)
  A sensor that provides pressure and temperature metrics.
### Creating a sensor
- [init(rawValue: String)](srsensor/init(rawvalue:).md)
  Creates a sensor from a raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(sensor: SRSensor)](srsensorreader/init(sensor:).md)
  Initializes a new sensor reader object.
- [var sensor: SRSensor](srsensorreader/sensor.md)
  The particular sensor that this object reads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor)*