# HKMetadataKeyAudioExposureLevel

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The audio level associated with an audio event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let HKMetadataKeyAudioExposureLevel: String
```

```c
extern NSString * const HKMetadataKeyAudioExposureLevel;
```

## Discussion

Use this key on audio exposure events. It takes an [`HKQuantity`](./hkquantity.md) containing the audio level measured in [`decibelAWeightedSoundPressureLevel()`](./hkunit/decibelaweightedsoundpressurelevel%28%29.md) units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyaudioexposurelevel)*