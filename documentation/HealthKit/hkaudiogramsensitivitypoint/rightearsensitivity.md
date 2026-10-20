# rightEarSensitivity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The sensitivity of the right ear.

**Availability**:
- iOS 13.0+ - Deprecated in 18.1
- iPadOS 13.0+ - Deprecated in 18.1
- Mac Catalyst 13.1+ - Deprecated in 18.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 2.1
- watchOS 6.0+ - Deprecated in 11.1

> **Deprecated**: Use tests object which will contain a value for right ear

## Declaration

```swift
@NSCopying
var rightEarSensitivity: HKQuantity? { get }
```

```objc
@property (copy, readonly, nullable) HKQuantity * rightEarSensitivity;
```

#### Discussion

This object uses [`decibelHearingLevel()`](../hkunit/decibelhearinglevel%28%29.md) units to measure sensitivity in attenuated dB from a baseline of 0 dB.

## See Also

### Accessing Data
- [var frequency: HKQuantity](./frequency.md)
  The frequency tested in the hearing test.
- [var leftEarSensitivity: HKQuantity?](./leftearsensitivity.md)
  The sensitivity of the left ear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/rightearsensitivity)*