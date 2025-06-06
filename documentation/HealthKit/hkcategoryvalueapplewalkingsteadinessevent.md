# HKCategoryValueAppleWalkingSteadinessEvent

**Framework**: HealthKit  
**Kind**: enum

The value of an event triggered by a reduced score for the steadiness of the user’s gait.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum HKCategoryValueAppleWalkingSteadinessEvent
```

#### Overview

These values indicate that the user received a Low or Very Low score for their Walking Steadiness. The [`HKCategoryValueAppleWalkingSteadinessEvent.repeatLow`](hkcategoryvalueapplewalkingsteadinessevent/repeatlow.md) and [`HKCategoryValueAppleWalkingSteadinessEvent.repeatVeryLow`](hkcategoryvalueapplewalkingsteadinessevent/repeatverylow.md) values indicate that the Low and Very Low scores persisted over a significant period of time.

## Topics

### Steadiness Values
- [HKCategoryValueAppleWalkingSteadinessEvent.initialLow](hkcategoryvalueapplewalkingsteadinessevent/initiallow.md)
  The user received a below-normal steadiness score for their gait while walking.
- [HKCategoryValueAppleWalkingSteadinessEvent.initialVeryLow](hkcategoryvalueapplewalkingsteadinessevent/initialverylow.md)
  The user received a steadiness score for their gait while walking that was considerably below normal.
- [HKCategoryValueAppleWalkingSteadinessEvent.repeatLow](hkcategoryvalueapplewalkingsteadinessevent/repeatlow.md)
  The user’s below-normal score persists over a significant period of time.
- [HKCategoryValueAppleWalkingSteadinessEvent.repeatVeryLow](hkcategoryvalueapplewalkingsteadinessevent/repeatverylow.md)
  The user’s considerably below-normal score persists over a significant period of time.
### Initializers
- [init?(rawValue: Int)](hkcategoryvalueapplewalkingsteadinessevent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [HKCategoryValuePredicateProviding](hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum HKCategoryValue](hkcategoryvalue.md)
  Categories that are undefined.
- [enum HKCategoryValueCervicalMucusQuality](hkcategoryvaluecervicalmucusquality.md)
  Categories that represent the user’s cervical mucus quality.
- [enum HKCategoryValueMenstrualFlow](hkcategoryvaluemenstrualflow.md)
  Categories that indicate the amount of menstrual flow for a given sample.
- [enum HKCategoryValueOvulationTestResult](hkcategoryvalueovulationtestresult.md)
  Categories that represent the result of an ovulation home test.
- [enum HKCategoryValueContraceptive](hkcategoryvaluecontraceptive.md)
  The type of contraceptive.
- [enum HKCategoryValueSleepAnalysis](hkcategoryvaluesleepanalysis.md)
  Categories that represent the result of a sleep analysis.
- [enum HKCategoryValueAppetiteChanges](hkcategoryvalueappetitechanges.md)
  Categories that represent change in appetite.
- [enum HKCategoryValuePresence](hkcategoryvaluepresence.md)
  Categories that indicate whether a symptom is present.
- [enum HKCategoryValueSeverity](hkcategoryvalueseverity.md)
  Categories that represent the severity of a symptom.
- [enum HKCategoryValueEnvironmentalAudioExposureEvent](hkcategoryvalueenvironmentalaudioexposureevent.md)
  Exposure events for environmental audio.
- [enum HKCategoryValueHeadphoneAudioExposureEvent](hkcategoryvalueheadphoneaudioexposureevent.md)
  Exposure events for headphone audio.
- [enum HKCategoryValueLowCardioFitnessEvent](hkcategoryvaluelowcardiofitnessevent.md)
  A value that indicates a low-level cardio fitness event.
- [enum HKAppleWalkingSteadinessClassification](hkapplewalkingsteadinessclassification.md)
  A classification of a score based on the steadiness of the user’s gait.
- [enum HKCategoryValuePregnancyTestResult](hkcategoryvaluepregnancytestresult.md)
  Category values that indicate the results of a home pregnancy test.
- [enum HKCategoryValueProgesteroneTestResult](hkcategoryvalueprogesteronetestresult.md)
  A category value that indicates the result from a home progesterone test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplewalkingsteadinessevent)*