# HKCategoryValueSleepAnalysis

**Framework**: Healthkit  
**Kind**: enum

Categories that represent the result of a sleep analysis.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKCategoryValueSleepAnalysis
```

## Mentions

- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

These values provide the set of valid categories for sleep tracking in HealthKit. To record a sleep sample, create an [`HKCategorySample`](hkcategorysample.md) using a [`sleepAnalysis`](hkcategorytypeidentifier/sleepanalysis.md) identifier and a [`HKCategoryValueSleepAnalysis`](hkcategoryvaluesleepanalysis.md) value.

```swift
let sleepSampleType = HKCategoryType(.sleepAnalysis)
let sleepCategory = HKCategoryValueSleepAnalysis.asleepDeep.rawValue
let deepSleepSample  = HKCategorySample(type: sleepSampleType,
                                        value:sleepCategory,
                                        start: startDate,
                                        end: endDate)
```

Each sleep analysis sample can have only one value. To track both the amount of time a person spends in bed and the quality and quantity of their sleep, use samples with overlapping times.

![An illustration showing the in-bed sample and the overlapping awake, REM, core and deep sleep samples.](https://docs-assets.developer.apple.com/published/9d8f3608cc6f723dbcd923546c79061e/media-4110084%402x.png)

One set of samples tracks the amount of time the user spent in bed. Then, you can partition the in-bed time into a more-detailed set of samples. These detailed samples show when the user was awake, in core sleep, in deep sleep, or in rapid eye movement (REM) sleep. The detailed samples overlap the in-bed sample, but they don’t overlap each other.

> **Note**:  Samples recorded by Apple Watch only include awake samples that occur between two sleep samples. When reading sleep samples from HealthKit, there might not be any detailed samples that correspond to the beginning or ending of an in-bed sample.

By comparing the start and end times of these samples, apps can calculate secondary statistics. For example: the amount of time it took for the user to fall asleep, the percentage of sleep time spent in deep sleep, the number of times the user woke while in bed, and the total amount of time spent both in bed and asleep.

## Topics

### Values for Tracking Time In-Bed
- [HKCategoryValueSleepAnalysis.inBed](hkcategoryvaluesleepanalysis/inbed.md)
  The user is in bed.
### Values for Tracking Sleep States
- [HKCategoryValueSleepAnalysis.awake](hkcategoryvaluesleepanalysis/awake.md)
  The user is awake.
- [HKCategoryValueSleepAnalysis.asleepCore](hkcategoryvaluesleepanalysis/asleepcore.md)
  The user is in light or intermediate sleep.
- [HKCategoryValueSleepAnalysis.asleepDeep](hkcategoryvaluesleepanalysis/asleepdeep.md)
  The user is in deep sleep.
- [HKCategoryValueSleepAnalysis.asleepREM](hkcategoryvaluesleepanalysis/asleeprem.md)
  The user is in REM sleep.
- [HKCategoryValueSleepAnalysis.asleepUnspecified](hkcategoryvaluesleepanalysis/asleepunspecified.md)
  The user is asleep, but the specific stage isn’t known.
### Deprecated values
- [static var asleep: HKCategoryValueSleepAnalysis](hkcategoryvaluesleepanalysis/asleep.md)
  The user is sleeping.
### Initializers
- [init?(rawValue: Int)](hkcategoryvaluesleepanalysis/init(rawvalue:).md)
### Type Properties
- [static var allAsleepValues: Set<HKCategoryValueSleepAnalysis>](hkcategoryvaluesleepanalysis/allasleepvalues.md)
  A set of values that represents the possible stages of sleep.

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

*[View on Apple Developer](https://developer.apple.com/documentation/HealthKit/hkcategoryvaluesleepanalysis)*