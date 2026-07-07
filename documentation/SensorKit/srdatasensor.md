# SRDataSensor

**Framework**: SensorKit  
**Kind**: protocol

`SRDataSensor` serves as the foundational protocol for all sensor types, providing type safety and consistency across the SensorKit ecosystem. Each conforming sensor type specifies the kind of data it produces, enabling compile-time verification and type-safe data access patterns.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
protocol SRDataSensor : Hashable, Sendable
```

#### Protocol Requirements

#### Usage Example

```swift
// Using a specific sensor type
let temperatureSensor: SRWristTemperatureSensor = .wristTemperature

// Creating a reader with type safety
guard let reader = SRReader(sensor: temperatureSensor) else {
    print("Failed to create reader")
    return
}

// The reader automatically knows the sample type
for try await response in reader.fetch(request) {
    if let sample: SRWristTemperatureSession = response.sample() {
        // Type-safe access to temperature data
        print("Temperature: \(sample.temperature)")
    }
}
```

## Topics

### Associated Types
- [associatedtype Sample](srdatasensor/sample.md)
### Type Properties
- [static var accelerometer: SRAccelerometerSensor](srdatasensor/accelerometer.md)
- [static var acousticSettings: SRAcousticSettingsSensor](srdatasensor/acousticsettings.md)
- [static var ambientLight: SRAmbientLightSensor](srdatasensor/ambientlight.md)
- [static var ambientPressure: SRAmbientPressureSensor](srdatasensor/ambientpressure.md)
- [static var deviceUsage: SRDeviceUsageSensor](srdatasensor/deviceusage.md)
- [static var electrocardiogram: SRElectrocardiogramSensor](srdatasensor/electrocardiogram.md)
- [static var faceMetrics: SRFaceMetricsSensor](srdatasensor/facemetrics.md)
- [static var headphoneMotion: SRHeadphoneMotionSensor](srdatasensor/headphonemotion.md)
- [static var headphoneSettings: SRHeadphoneSettingsSensor](srdatasensor/headphonesettings.md)
- [static var heartRate: SRHeartRateSensor](srdatasensor/heartrate.md)
- [static var keyboardMetrics: SRKeyboardMetricsSensor](srdatasensor/keyboardmetrics.md)
- [static var mediaEvents: SRMediaEventsSensor](srdatasensor/mediaevents.md)
- [static var messagesUsage: SRMessagesUsageSensor](srdatasensor/messagesusage.md)
- [static var odometer: SROdometerSensor](srdatasensor/odometer.md)
- [static var onWristState: SROnWristStateSensor](srdatasensor/onwriststate.md)
- [static var pedometerData: SRPedometerDataSensor](srdatasensor/pedometerdata.md)
- [static var phoneUsage: SRPhoneUsageSensor](srdatasensor/phoneusage.md)
- [static var photoplethysmogram: SRPhotoplethysmogramSensor](srdatasensor/photoplethysmogram.md)
- [static var rotationRate: SRRotationRateSensor](srdatasensor/rotationrate.md)
- [static var siriSpeechMetrics: SRSiriSpeechMetricsSensor](srdatasensor/sirispeechmetrics.md)
- [static var sleepSessions: SRSleepSessionsSensor](srdatasensor/sleepsessions.md)
- [static var telephonySpeechMetrics: SRTelephonySpeechMetricsSensor](srdatasensor/telephonyspeechmetrics.md)
- [static var visits: SRVisitsSensor](srdatasensor/visits.md)
- [static var wristTemperature: SRWristTemperatureSensor](srdatasensor/wristtemperature.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [SRAccelerometerSensor](sraccelerometersensor.md)
- [SRAcousticSettingsSensor](sracousticsettingssensor.md)
- [SRAmbientLightSensor](srambientlightsensor.md)
- [SRAmbientPressureSensor](srambientpressuresensor.md)
- [SRDeviceUsageSensor](srdeviceusagesensor.md)
- [SRElectrocardiogramSensor](srelectrocardiogramsensor.md)
- [SRFaceMetricsSensor](srfacemetricssensor.md)
- [SRHeadphoneMotionSensor](srheadphonemotionsensor.md)
- [SRHeadphoneSettingsSensor](srheadphonesettingssensor.md)
- [SRHeartRateSensor](srheartratesensor.md)
- [SRKeyboardMetricsSensor](srkeyboardmetricssensor.md)
- [SRMediaEventsSensor](srmediaeventssensor.md)
- [SRMessagesUsageSensor](srmessagesusagesensor.md)
- [SROdometerSensor](srodometersensor.md)
- [SROnWristStateSensor](sronwriststatesensor.md)
- [SRPedometerDataSensor](srpedometerdatasensor.md)
- [SRPhoneUsageSensor](srphoneusagesensor.md)
- [SRPhotoplethysmogramSensor](srphotoplethysmogramsensor.md)
- [SRRotationRateSensor](srrotationratesensor.md)
- [SRSiriSpeechMetricsSensor](srsirispeechmetricssensor.md)
- [SRSleepSessionsSensor](srsleepsessionssensor.md)
- [SRTelephonySpeechMetricsSensor](srtelephonyspeechmetricssensor.md)
- [SRVisitsSensor](srvisitssensor.md)
- [SRWristTemperatureSensor](srwristtemperaturesensor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdatasensor)*