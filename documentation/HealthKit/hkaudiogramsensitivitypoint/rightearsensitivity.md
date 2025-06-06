# rightEarSensitivity

**Framework**: HealthKit  
**Kind**: property

The sensitivity of the right ear.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var rightEarSensitivity: HKQuantity? { get }
```

#### Discussion

This object uses [`decibelHearingLevel()`](hkunit/decibelhearinglevel().md) units to measure sensitivity in attenuated dB from a baseline of 0 dB.

## See Also

- [var frequency: HKQuantity](hkaudiogramsensitivitypoint/frequency.md)
  The frequency tested in the hearing test.
- [var leftEarSensitivity: HKQuantity?](hkaudiogramsensitivitypoint/leftearsensitivity.md)
  The sensitivity of the left ear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/rightearsensitivity)*