# HKCategoryValuePresence

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

Categories that indicate whether a symptom is present.

**Availability**:
- iOS 13.6+
- iPadOS 13.6+
- Mac Catalyst 13.6+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum HKCategoryValuePresence
```

```c
enum HKCategoryValuePresence : NSInteger;
```

## Topics

### Presence of Symptoms
- [HKCategoryValuePresence.notPresent](./hkcategoryvaluepresence/notpresent.md)
  The symptom isn’t present.
- [HKCategoryValuePresence.present](./hkcategoryvaluepresence/present.md)
  The symptom is present.
### Initializers
- [init?(rawValue: Int)](./hkcategoryvaluepresence/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [HKCategoryValuePredicateProviding](./hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Assigning Values
- [enum HKCategoryValue](./hkcategoryvalue.md)
  Categories that are undefined.
- [enum HKCategoryValueCervicalMucusQuality](./hkcategoryvaluecervicalmucusquality.md)
  Categories that represent the user’s cervical mucus quality.
- [enum HKCategoryValueMenstrualFlow](./hkcategoryvaluemenstrualflow.md)
  Categories that indicate the amount of menstrual flow for a given sample.
- [enum HKCategoryValueOvulationTestResult](./hkcategoryvalueovulationtestresult.md)
  Categories that represent the result of an ovulation home test.
- [enum HKCategoryValueContraceptive](./hkcategoryvaluecontraceptive.md)
  The type of contraceptive.
- [enum HKCategoryValueSleepAnalysis](./hkcategoryvaluesleepanalysis.md)
  Categories that represent the result of a sleep analysis.
- [enum HKCategoryValueAppetiteChanges](./hkcategoryvalueappetitechanges.md)
  Categories that represent change in appetite.
- [enum HKCategoryValueSeverity](./hkcategoryvalueseverity.md)
  Categories that represent the severity of a symptom.
- [enum HKCategoryValueEnvironmentalAudioExposureEvent](./hkcategoryvalueenvironmentalaudioexposureevent.md)
  Exposure events for environmental audio.
- [enum HKCategoryValueHeadphoneAudioExposureEvent](./hkcategoryvalueheadphoneaudioexposureevent.md)
  Exposure events for headphone audio.
- [enum HKCategoryValueLowCardioFitnessEvent](./hkcategoryvaluelowcardiofitnessevent.md)
  A value that indicates a low-level cardio fitness event.
- [enum HKAppleWalkingSteadinessClassification](./hkapplewalkingsteadinessclassification.md)
  A classification of a score based on the steadiness of the user’s gait.
- [enum HKCategoryValueAppleWalkingSteadinessEvent](./hkcategoryvalueapplewalkingsteadinessevent.md)
  The value of an event triggered by a reduced score for the steadiness of the user’s gait.
- [enum HKCategoryValuePregnancyTestResult](./hkcategoryvaluepregnancytestresult.md)
  Category values that indicate the results of a home pregnancy test.
- [enum HKCategoryValueProgesteroneTestResult](./hkcategoryvalueprogesteronetestresult.md)
  A category value that indicates the result from a home progesterone test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepresence)*