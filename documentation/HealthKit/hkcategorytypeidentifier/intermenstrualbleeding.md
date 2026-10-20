# intermenstrualBleeding

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A category sample type that records spotting outside the normal menstruation period.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let intermenstrualBleeding: HKCategoryTypeIdentifier
```

```c
extern HKCategoryTypeIdentifier const HKCategoryTypeIdentifierIntermenstrualBleeding;
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
### Reproductive health
- [static let menstrualFlow: HKCategoryTypeIdentifier](./menstrualflow.md)
  A category sample type that records menstrual cycles.
- [static let infrequentMenstrualCycles: HKCategoryTypeIdentifier](./infrequentmenstrualcycles.md)
  A category sample that indicates an infrequent menstrual cycle.
- [static let irregularMenstrualCycles: HKCategoryTypeIdentifier](./irregularmenstrualcycles.md)
  A category sample that indicates an irregular menstrual cycle.
- [static let persistentIntermenstrualBleeding: HKCategoryTypeIdentifier](./persistentintermenstrualbleeding.md)
  A category sample that indicates persistent intermenstrual bleeding.
- [static let prolongedMenstrualPeriods: HKCategoryTypeIdentifier](./prolongedmenstrualperiods.md)
  A category sample that indicates a prolonged menstrual cycle.
- [static let basalBodyTemperature: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/basalbodytemperature.md)
  A quantity sample type that records the user’s basal body temperature.
- [static let cervicalMucusQuality: HKCategoryTypeIdentifier](./cervicalmucusquality.md)
  A category sample type that records the quality of the user’s cervical mucus.
- [static let ovulationTestResult: HKCategoryTypeIdentifier](./ovulationtestresult.md)
  A category sample type that records the result of an ovulation home test.
- [static let progesteroneTestResult: HKCategoryTypeIdentifier](./progesteronetestresult.md)
  A category type that represents the results from a home progesterone test.
- [static let sexualActivity: HKCategoryTypeIdentifier](./sexualactivity.md)
  A category sample type that records sexual activity.
- [static let contraceptive: HKCategoryTypeIdentifier](./contraceptive.md)
  A category sample type that records the use of contraceptives.
- [static let pregnancy: HKCategoryTypeIdentifier](./pregnancy.md)
  A category type that records pregnancy.
- [static let pregnancyTestResult: HKCategoryTypeIdentifier](./pregnancytestresult.md)
  A category type that represents the results from a home pregnancy test.
- [static let lactation: HKCategoryTypeIdentifier](./lactation.md)
  A category type that records lactation.
- [enum HKCategoryValueVaginalBleeding](../hkcategoryvaluevaginalbleeding.md)
  A value that indicates the intensity of vaginal bleeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/intermenstrualbleeding)*