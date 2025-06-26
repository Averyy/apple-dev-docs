# HKCategorySample

**Framework**: HealthKit  
**Kind**: class

A sample with values from a short list of possible values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKCategorySample
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

You can use category samples to record data associated with a [`HKCategoryType`](hkcategorytype.md). The value for the sample must come from the appropriate category value enumeration. Each category type uses its own enumeration. Individual samples represent a value and time period. Samples with different values may have overlapping time intervals.

The [`HKCategorySample`](hkcategorysample.md) class is a concrete subclass of the [`HKSample`](hksample.md) class. Category samples are immutable: You set the sample’s properties when you create it, and they can’t change.

##### Extend Category Samples

Like many HealthKit classes, don’t subclass the `HKCategorySample` class. You may extend the `HKCategorySample` class by adding metadata with custom keys as appropriate for your app.

For more information, see [`init(type:value:start:end:metadata:)`](hkcategorysample/init(type:value:start:end:metadata:).md).

## Topics

### Creating Category Samples
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date)](hkcategorysample/init(type:value:start:end:).md)
  Creates a newly instantiated category sample.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, metadata: [String : Any]?)](hkcategorysample/init(type:value:start:end:metadata:).md)
  Creates a newly instantiated category sample with the provided metadata.
- [convenience init(type: HKCategoryType, value: Int, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkcategorysample/init(type:value:start:end:device:metadata:).md)
  Creates a newly instantiated category sample including the provided device and metadata.
### Getting Property Data
- [var categoryType: HKCategoryType](hkcategorysample/categorytype.md)
  The category type for this sample.
- [var value: Int](hkcategorysample/value.md)
  The category value for this sample.
### Assigning Values
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
- [enum HKCategoryValueAppleWalkingSteadinessEvent](hkcategoryvalueapplewalkingsteadinessevent.md)
  The value of an event triggered by a reduced score for the steadiness of the user’s gait.
- [enum HKCategoryValuePregnancyTestResult](hkcategoryvaluepregnancytestresult.md)
  Category values that indicate the results of a home pregnancy test.
- [enum HKCategoryValueProgesteroneTestResult](hkcategoryvalueprogesteronetestresult.md)
  A category value that indicates the result from a home progesterone test.
- [enum HKCategoryValueAudioExposureEvent](hkcategoryvalueaudioexposureevent.md)
  Categories that indicate audio exposure events.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathCategoryValue: String](hkpredicatekeypathcategoryvalue.md)
  The key path for accessing the category sample’s value.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.
- [Metadata Keys](metadata-keys.md)
  Constants used to add metadata to objects stored in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorysample)*