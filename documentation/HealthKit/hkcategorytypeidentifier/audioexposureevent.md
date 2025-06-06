# audioExposureEvent

**Framework**: HealthKit  
**Kind**: property

A category sample type for audio exposure events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let audioExposureEvent: HKCategoryTypeIdentifier
```

#### Discussion

These samples use values from [`HKCategoryValueAudioExposureEvent`](hkcategoryvalueaudioexposureevent.md).

## Topics

### Metadata Keys
- [let HKMetadataKeyAudioExposureLevel: String](hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.

## See Also

- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/headphoneaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/audioexposureevent)*