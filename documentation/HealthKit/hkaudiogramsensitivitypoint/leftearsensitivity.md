# leftEarSensitivity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The sensitivity of the left ear.

**Availability**:
- iOS 13.0+ - Deprecated in 18.1
- iPadOS 13.0+ - Deprecated in 18.1
- Mac Catalyst 13.1+ - Deprecated in 18.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 2.1
- watchOS 6.0+ - Deprecated in 11.1

> **Deprecated**: Use tests object which will contain a value for left ear

## Declaration

```swift
@NSCopying
var leftEarSensitivity: HKQuantity? { get }
```

```objc
@property (copy, readonly, nullable) HKQuantity * leftEarSensitivity;
```

#### Discussion

This object uses [`decibelHearingLevel()`](../hkunit/decibelhearinglevel%28%29.md) units to measure sensitivity in attenuated dB from a baseline of 0 dB.

## See Also

### Accessing Data
- [var frequency: HKQuantity](./frequency.md)
  The frequency tested in the hearing test.
- [var rightEarSensitivity: HKQuantity?](./rightearsensitivity.md)
  The sensitivity of the right ear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/leftearsensitivity)*