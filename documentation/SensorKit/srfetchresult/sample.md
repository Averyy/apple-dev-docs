# sample

**Framework**: SensorKit  
**Kind**: property

A recording that the sensor reader fetches.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@NSCopying
var sample: SampleType { get }
```

#### Discussion

The framework expects the app to know the result type based on the reader’s sensor.

##### Sample Types

This property’s type is a superclass from which the framework derives discrete sample types. Depending on the sensor associated with your app’s sensor reader, type cast the fetch result’s [`sample`](srfetchresult/sample.md) to the sensor’s associated sample type. The following list provides the sample type per sensor:

- **[`accelerometer`](srsensor/accelerometer.md)**: [[`CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)]
- **[`ambientLightSensor`](srsensor/ambientlightsensor.md)**: [`SRAmbientLightSample`](srambientlightsample.md)
- **[`ambientPressure`](srsensor/ambientpressure.md)**: `[`[`CMRecordedPressureData`](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)`]`
- **[`deviceUsageReport`](srsensor/deviceusagereport.md)**: [`SRDeviceUsageReport`](srdeviceusagereport.md)
- **[`faceMetrics`](srsensor/facemetrics.md)**: [`SRFaceMetrics`](srfacemetrics.md)
- **[`heartRate`](srsensor/heartrate.md)**: [`CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)
- **[`keyboardMetrics`](srsensor/keyboardmetrics.md)**: [`SRKeyboardMetrics`](srkeyboardmetrics.md)
- **[`mediaEvents`](srsensor/mediaevents.md)**: [`SRMediaEvent`](srmediaevent.md)
- **[`messagesUsageReport`](srsensor/messagesusagereport.md)**: [`SRMessagesUsageReport`](srmessagesusagereport.md)
- **[`odometer`](srsensor/odometer.md)**: [`CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)
- **[`onWristState`](srsensor/onwriststate.md)**: [`SRWristDetection`](srwristdetection.md)
- **[`pedometerData`](srsensor/pedometerdata.md)**: [`CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)
- **[`phoneUsageReport`](srsensor/phoneusagereport.md)**: [`SRPhoneUsageReport`](srphoneusagereport.md)
- **[`rotationRate`](srsensor/rotationrate.md)**: [[`CMRecordedRotationRateData`](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)]
- **[`siriSpeechMetrics`](srsensor/sirispeechmetrics.md)**: [`SRSpeechMetrics`](srspeechmetrics.md)
- **[`telephonySpeechMetrics`](srsensor/telephonyspeechmetrics.md)**: [`SRSpeechMetrics`](srspeechmetrics.md)
- **[`visits`](srsensor/visits.md)**: [`SRVisit`](srvisit.md)
- **[`wristTemperature`](srsensor/wristtemperature.md)**: [`SRWristTemperature`](srwristtemperature.md)

## See Also

- [var timestamp: SRAbsoluteTime](srfetchresult/timestamp.md)
  The time when the framework records the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)*