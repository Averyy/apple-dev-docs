# basalBodyTemperature

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that records the user’s basal body temperature.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let basalBodyTemperature: HKQuantityTypeIdentifier
```

#### Discussion

Basal body temperature measures the body’s temperature when at rest (for example, taking the temperature immediately after waking). These samples use temperature units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

## See Also

- [enum HKCategoryValue](hkcategoryvalue.md)
  Categories that are undefined.
- [struct HKCategoryTypeIdentifier](hkcategorytypeidentifier.md)
  Identifiers for creating category types.
- [class HKCategoryType](hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/basalbodytemperature)*