# headphoneAudioExposure

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures audio exposure from headphones.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let headphoneAudioExposure: HKQuantityTypeIdentifier
```

#### Discussion

These samples use sound pressure units (described in [`HKUnit`](hkunit.md)). You create these units using the [`decibelAWeightedSoundPressureLevel()`](hkunit/decibelaweightedsoundpressurelevel().md) method. They measure discrete values of the equivalent continuous sound pressure level, described in [`HKQuantityAggregationStyle.discreteEquivalentContinuousLevel`](hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md). Samples can be automatically detected by an iPhone or Apple Watch.

## See Also

- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/headphoneaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from headphones.
- [static let audioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/audioexposureevent.md)
  A category sample type for audio exposure events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/headphoneaudioexposure)*