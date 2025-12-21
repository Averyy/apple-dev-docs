# environmentalSoundReduction

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the difference in sound intensity when wearing headphones that lower environmental sound levels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let environmentalSoundReduction: HKQuantityTypeIdentifier
```

#### Discussion

These samples use sound pressure units (described in [`HKUnit`](hkunit.md)). They measure discrete values of the equivalent continuous sound pressure level, described in [`HKQuantityAggregationStyle.discreteEquivalentContinuousLevel`](hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md). Environmental sound reduction values are automatically collected when wearing supported headphones.

## See Also

- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/environmentalsoundreduction)*