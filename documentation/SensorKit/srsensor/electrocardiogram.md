# electrocardiogram

**Framework**: SensorKit  
**Kind**: property

A sensor that streams sample ECG sensor data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
static let electrocardiogram: SRSensor
```

#### Discussion

The sample for this sensor is an array of [`SRElectrocardiogramSample`](srelectrocardiogramsample.md) objects.

You need to provide a reason to record electrocardiogram (ECG) data by adding the `SRSensorUsageECG` dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

You also need to add the `ecg` key to the `com.apple.developer.sensorkit.reader.allow` entitlement, as in:

```plist
<plist version="1.0">
<dict>
        <key>com.apple.developer.sensorkit.reader.allow</key>
        <array>
                <string>ecg</string>
        </array>
</dict>
</plist>
```

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
- [static let telephonySpeechMetrics: SRSensor](srsensor/telephonyspeechmetrics.md)
  A sensor that provides data describing speech during phone calls.
- [static let visits: SRSensor](srsensor/visits.md)
  A sensor that provides information about frequently visited locations.
- [static let wristTemperature: SRSensor](srsensor/wristtemperature.md)
  A sensor that provides wrist temperature while the user sleeps.
- [static let photoplethysmogram: SRSensor](srsensor/photoplethysmogram.md)
  A sensor that streams sample PPG sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/electrocardiogram)*