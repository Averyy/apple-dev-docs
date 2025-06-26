# HKCategoryValueOvulationTestResult

**Framework**: HealthKit  
**Kind**: enum

Categories that represent the result of an ovulation home test.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKCategoryValueOvulationTestResult
```

## Topics

### Ovulation Test Results
- [HKCategoryValueOvulationTestResult.negative](hkcategoryvalueovulationtestresult/negative.md)
  The ovulation test is negative.
- [HKCategoryValueOvulationTestResult.luteinizingHormoneSurge](hkcategoryvalueovulationtestresult/luteinizinghormonesurge.md)
  The ovulation test detected a surge in the luteinizing hormone. This value often refers to a `Positive` or `Peak` result.
- [HKCategoryValueOvulationTestResult.indeterminate](hkcategoryvalueovulationtestresult/indeterminate.md)
  The ovulation test is inconclusive.
- [HKCategoryValueOvulationTestResult.estrogenSurge](hkcategoryvalueovulationtestresult/estrogensurge.md)
  The ovulation test detected a surge in estrogen. This value often refers to a `High` result.
- [static var positive: HKCategoryValueOvulationTestResult](hkcategoryvalueovulationtestresult/positive.md)
  The ovulation test is positive.
### Initializers
- [init?(rawValue: Int)](hkcategoryvalueovulationtestresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [HKCategoryValuePredicateProviding](hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum HKCategoryValue](hkcategoryvalue.md)
  Categories that are undefined.
- [enum HKCategoryValueCervicalMucusQuality](hkcategoryvaluecervicalmucusquality.md)
  Categories that represent the user’s cervical mucus quality.
- [enum HKCategoryValueMenstrualFlow](hkcategoryvaluemenstrualflow.md)
  Categories that indicate the amount of menstrual flow for a given sample.
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
- [enum HKCategoryValueAppleWalkingSteadinessEvent](hkcategoryvalueapplewalkingsteadinessevent.md)
  The value of an event triggered by a reduced score for the steadiness of the user’s gait.
- [enum HKCategoryValuePregnancyTestResult](hkcategoryvaluepregnancytestresult.md)
  Category values that indicate the results of a home pregnancy test.
- [enum HKCategoryValueProgesteroneTestResult](hkcategoryvalueprogesteronetestresult.md)
  A category value that indicates the result from a home progesterone test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult)*