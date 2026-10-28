# frequency

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) HKQuantity * frequency;
```

## Discussion

This object uses [`hertz()`](../hkunit/hertz%28%29.md) units.

## See Also

### Accessing Data
- [var leftEarSensitivity: HKQuantity?](./leftearsensitivity.md)
  The sensitivity of the left ear.
- [var rightEarSensitivity: HKQuantity?](./rightearsensitivity.md)
  The sensitivity of the right ear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/frequency)*