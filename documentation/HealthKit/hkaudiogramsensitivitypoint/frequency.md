# frequency

**Framework**: HealthKit  
**Kind**: property

The frequency tested in the hearing test.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var frequency: HKQuantity { get }
```

#### Discussion

This object uses [`hertz()`](hkunit/hertz().md) units.

## See Also

- [var leftEarSensitivity: HKQuantity?](hkaudiogramsensitivitypoint/leftearsensitivity.md)
  The sensitivity of the left ear.
- [var rightEarSensitivity: HKQuantity?](hkaudiogramsensitivitypoint/rightearsensitivity.md)
  The sensitivity of the right ear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/frequency)*