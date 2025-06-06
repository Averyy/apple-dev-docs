# HKCategoryTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

Identifiers for creating category types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKCategoryTypeIdentifier
```

#### Overview

To create an [`HKCategoryType`](hkcategorytype.md) instance, pass an [`HKCategoryTypeIdentifier`](hkcategorytypeidentifier.md) value to the [`categoryType(forIdentifier:)`](hkobjecttype/categorytype(foridentifier:).md) method.

For the complete list of quantity type identifiers, see Activity.

## Topics

### Activity
- [static let appleStandHour: HKCategoryTypeIdentifier](hkcategorytypeidentifier/applestandhour.md)
  A category sample type that counts the number of hours in the day during which the user has stood and moved for at least one minute per hour.
- [static let lowCardioFitnessEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowcardiofitnessevent.md)
  An event that indicates the user’s VO2 max values consistently fall below a particular aerobic fitness threshold.
### Reproductive Health
- [static let menstrualFlow: HKCategoryTypeIdentifier](hkcategorytypeidentifier/menstrualflow.md)
  A category sample type that records menstrual cycles.
- [static let intermenstrualBleeding: HKCategoryTypeIdentifier](hkcategorytypeidentifier/intermenstrualbleeding.md)
  A category sample type that records spotting outside the normal menstruation period.
- [static let infrequentMenstrualCycles: HKCategoryTypeIdentifier](hkcategorytypeidentifier/infrequentmenstrualcycles.md)
  A category sample that indicates an infrequent menstrual cycle.
- [static let irregularMenstrualCycles: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularmenstrualcycles.md)
  A category sample that indicates an irregular menstrual cycle.
- [static let persistentIntermenstrualBleeding: HKCategoryTypeIdentifier](hkcategorytypeidentifier/persistentintermenstrualbleeding.md)
  A category sample that indicates persistent intermenstrual bleeding.
- [static let prolongedMenstrualPeriods: HKCategoryTypeIdentifier](hkcategorytypeidentifier/prolongedmenstrualperiods.md)
  A category sample that indicates a prolonged menstrual cycle.
- [static let cervicalMucusQuality: HKCategoryTypeIdentifier](hkcategorytypeidentifier/cervicalmucusquality.md)
  A category sample type that records the quality of the user’s cervical mucus.
- [static let ovulationTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/ovulationtestresult.md)
  A category sample type that records the result of an ovulation home test.
- [static let progesteroneTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/progesteronetestresult.md)
  A category type that represents the results from a home progesterone test.
- [static let sexualActivity: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sexualactivity.md)
  A category sample type that records sexual activity.
- [static let contraceptive: HKCategoryTypeIdentifier](hkcategorytypeidentifier/contraceptive.md)
  A category sample type that records the use of contraceptives.
- [static let pregnancy: HKCategoryTypeIdentifier](hkcategorytypeidentifier/pregnancy.md)
  A category type that records pregnancy.
- [static let pregnancyTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/pregnancytestresult.md)
  A category type that represents the results from a home pregnancy test.
- [static let lactation: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lactation.md)
  A category type that records lactation.
### Hearing
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [enum HKCategoryValueEnvironmentalAudioExposureEvent](hkcategoryvalueenvironmentalaudioexposureevent.md)
  Exposure events for environmental audio.
- [static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/headphoneaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from headphones.
- [enum HKCategoryValueHeadphoneAudioExposureEvent](hkcategoryvalueheadphoneaudioexposureevent.md)
  Exposure events for headphone audio.
- [static let audioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/audioexposureevent.md)
  A category sample type for audio exposure events.
### Vital Signs
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularheartrhythmevent.md)
  A category sample type for irregular heart rhythm events.
### Mobility
- [static let appleWalkingSteadinessEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/applewalkingsteadinessevent.md)
  A category sample type that records an incident where the user showed a reduced score for their gait’s steadiness.
### Symptoms
- [Symptom Type Identifiers](symptom-type-identifiers.md)
  Identifiers for medical symptoms.
### Mindfulness and Sleep
- [static let mindfulSession: HKCategoryTypeIdentifier](hkcategorytypeidentifier/mindfulsession.md)
  A category sample type for recording a mindful session.
- [static let sleepAnalysis: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sleepanalysis.md)
  A category sample type for sleep analysis information.
### Self Care
- [static let toothbrushingEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/toothbrushingevent.md)
  A category sample type for toothbrushing events.
- [static let handwashingEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/handwashingevent.md)
  A category sample type for handwashing events.
### Initializers
- [init(rawValue: String)](hkcategorytypeidentifier/init(rawvalue:).md)
  Returns a newly initialized category type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType?](hkobjecttype/categorytype(foridentifier:).md)
  Returns the shared category type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier)*