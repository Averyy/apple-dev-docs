# headphoneAudioExposureEvent

**Framework**: HealthKit  
**Kind**: property

A category sample type that records exposure to potentially damaging sounds from headphones.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.1+

## Declaration

```swift
static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier
```

#### Discussion

iPhone and Apple Watch save a [`headphoneAudioExposureEvent`](hkcategorytypeidentifier/headphoneaudioexposureevent.md) sample when the device generates a notification about loud headphone audio. Both devices generate these notifications when the user listens to audio long enough and at a volume that could affect their hearing. In some regions, users can enable or disable loud headphone notifications from Settings > Sounds & Haptics > Headphone Safety.

Samples of this type use values from the [`HKCategoryValueHeadphoneAudioExposureEvent`](hkcategoryvalueheadphoneaudioexposureevent.md) enumeration.

## Topics

### Metadata Keys
- [let HKMetadataKeyAudioExposureLevel: String](hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.
- [let HKMetadataKeyAudioExposureDuration: String](hkmetadatakeyaudioexposureduration.md)
  The audio exposure event’s duration.

## See Also

- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [static let audioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/audioexposureevent.md)
  A category sample type for audio exposure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/headphoneaudioexposureevent)*