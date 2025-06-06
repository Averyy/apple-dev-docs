# decibelHearingLevel()

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring the intensity of a sound.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func decibelHearingLevel() -> Self
```

#### Discussion

This unit measures the intensity of the sound relative to the quietest sound a typical young, healthy individual can hear.

## See Also

- [class func decibelAWeightedSoundPressureLevel() -> Self](hkunit/decibelaweightedsoundpressurelevel.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/decibelhearinglevel())*