# init(frequency:leftEarSensitivity:rightEarSensitivity:)

**Framework**: HealthKit  
**Kind**: init

Creates a new sensitivity point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(frequency: HKQuantity, leftEarSensitivity: HKQuantity?, rightEarSensitivity: HKQuantity?) throws
```

## Parameters

- `frequency`: The frequency tested. This object uses   units.
- `leftEarSensitivity`: The sensitivity of the left ear, measured in attenuated dB from a baseline of 0 db. This object uses   units.
- `rightEarSensitivity`: The sensitivity of the right ear, measured in attenuated dB from a baseline of 0 db. This object uses   units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/init(frequency:leftearsensitivity:rightearsensitivity:))*