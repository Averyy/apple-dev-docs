# HKCategoryValueEnvironmentalAudioExposureEvent

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

Exposure events for environmental audio.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum HKCategoryValueEnvironmentalAudioExposureEvent
```

```c
enum HKCategoryValueEnvironmentalAudioExposureEvent : NSInteger;
```

## Topics

### Events
- [HKCategoryValueEnvironmentalAudioExposureEvent.momentaryLimit](./hkcategoryvalueenvironmentalaudioexposureevent/momentarylimit.md)
  A brief exposure to a loud environment.
### Metadata Keys
- [let HKMetadataKeyAudioExposureLevel: String](./hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.
### Initializers
- [init?(rawValue: Int)](./hkcategoryvalueenvironmentalaudioexposureevent/init%28rawvalue%29.md)

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
- [enum HKCategoryValuePresence](./hkcategoryvaluepresence.md)
  Categories that indicate whether a symptom is present.
- [enum HKCategoryValueSeverity](./hkcategoryvalueseverity.md)
  Categories that represent the severity of a symptom.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvalueenvironmentalaudioexposureevent)*