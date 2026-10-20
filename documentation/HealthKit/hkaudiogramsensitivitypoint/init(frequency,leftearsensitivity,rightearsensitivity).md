# init(frequency:leftEarSensitivity:rightEarSensitivity:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a new sensitivity point.

**Availability**:
- iOS 13.0+ - Deprecated in 18.1
- iPadOS 13.0+ - Deprecated in 18.1
- Mac Catalyst 13.1+ - Deprecated in 18.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 2.1
- watchOS 6.0+ - Deprecated in 11.1

> **Deprecated**: Use +[HKAudiogramSensitivityPoint sensitivityPointWithFrequency:tests:error:]

## Declaration

```swift
convenience init(frequency: HKQuantity, leftEarSensitivity: HKQuantity?, rightEarSensitivity: HKQuantity?) throws
```

```objc
+ (instancetype) sensitivityPointWithFrequency:(HKQuantity *) frequency leftEarSensitivity:(HKQuantity *) leftEarSensitivity rightEarSensitivity:(HKQuantity *) rightEarSensitivity error:(NSError **) error;
```

## Parameters

- `frequency`: The frequency tested. This object uses [`hertz()`](../hkunit/hertz%28%29.md) units.
- `leftEarSensitivity`: The sensitivity of the left ear, measured in attenuated dB from a baseline of 0 db. This object uses [`decibelHearingLevel()`](../hkunit/decibelhearinglevel%28%29.md) units.
- `rightEarSensitivity`: The sensitivity of the right ear, measured in attenuated dB from a baseline of 0 db. This object uses [`decibelHearingLevel()`](../hkunit/decibelhearinglevel%28%29.md) units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/init(frequency:leftearsensitivity:rightearsensitivity:))*