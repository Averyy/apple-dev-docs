# mindfulSession

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A category sample type for recording a mindful session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let mindfulSession: HKCategoryTypeIdentifier
```

```c
extern HKCategoryTypeIdentifier const HKCategoryTypeIdentifierMindfulSession;
```

#### Discussion

Use a [`HKCategoryValue.notApplicable`](../hkcategoryvalue/notapplicable.md) value with these samples.

## See Also

### Related Documentation
- [enum HKCategoryValue](../hkcategoryvalue.md)
  Categories that are undefined.
- [struct HKCategoryTypeIdentifier](../hkcategorytypeidentifier.md)
  Identifiers for creating category types.
- [class HKCategoryType](../hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCategorySample](../hkcategorysample.md)
  A sample with values from a short list of possible values.
### Mindfulness and sleep
- [static let sleepAnalysis: HKCategoryTypeIdentifier](./sleepanalysis.md)
  A category sample type for sleep analysis information.
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.
- [enum HKAppleSleepingBreathingDisturbancesClassification](../hkapplesleepingbreathingdisturbancesclassification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/mindfulsession)*