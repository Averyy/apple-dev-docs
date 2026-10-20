# audioExposureEvent

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A category sample type for audio exposure events.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: HKCategoryTypeIdentifier.environmentalAudioExposureEvent)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: HKCategoryTypeIdentifier.environmentalAudioExposureEvent)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: HKCategoryTypeIdentifier.environmentalAudioExposureEvent)
- macOS
- visionOS 1.0+ - Deprecated in 1.0 (renamed: HKCategoryTypeIdentifier.environmentalAudioExposureEvent)
- watchOS 6.0+ - Deprecated in 7.0 (renamed: HKCategoryTypeIdentifier.environmentalAudioExposureEvent)

> **Deprecated**: Use [`environmentalAudioExposureEvent`](./environmentalaudioexposureevent.md) instead.

## Declaration

```swift
static let audioExposureEvent: HKCategoryTypeIdentifier
```

```c
extern HKCategoryTypeIdentifier const HKCategoryTypeIdentifierAudioExposureEvent;
```

#### Discussion

These samples use values from [`HKCategoryValueAudioExposureEvent`](../hkcategoryvalueaudioexposureevent.md).

## Topics

### Metadata Keys
- [let HKMetadataKeyAudioExposureLevel: String](../hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.

## See Also

### Hearing
- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](./environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier](./headphoneaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/audioexposureevent)*