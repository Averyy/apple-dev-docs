# HKMetadataKeyAudioExposureDuration

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The audio exposure event’s duration.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.1+

## Declaration

```swift
let HKMetadataKeyAudioExposureDuration: String
```

```c
extern NSString * const HKMetadataKeyAudioExposureDuration;
```

## Discussion

Use this key on headphone audio exposure events. It takes an [`HKQuantity`](./hkquantity.md) containing the audio level measured in units of time.

## See Also

### Metadata Keys
- [let HKMetadataKeyAudioExposureLevel: String](./hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyaudioexposureduration)*