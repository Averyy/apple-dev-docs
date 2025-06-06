# menstrualFlow

**Framework**: HealthKit  
**Kind**: property

A category sample type that records menstrual cycles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let menstrualFlow: HKCategoryTypeIdentifier
```

#### Discussion

These samples use values from the [`HKCategoryValueMenstrualFlow`](hkcategoryvaluemenstrualflow.md) enum. Additionally, these samples must include [`HKMetadataKeyMenstrualCycleStart`](hkmetadatakeymenstrualcyclestart.md)  metadata.

When recording data about the user’s menstrual cycle, you can either use a single sample for the entire period, or multiple samples to record changes over the cycle. When using single samples, pass the start of the menstrual period to the `startDate` parameter. Pass the end of the period to the `endDate` parameter, and set the [`HKMetadataKeyMenstrualCycleStart`](hkmetadatakeymenstrualcyclestart.md) value to [`true`](https://developer.apple.com/documentation/swift/true).

When using multiple samples to record a single period, the `startDate` and `endDate` parameters should mark the beginning and ending of each individual sample. Set the [`HKMetadataKeyMenstrualCycleStart`](hkmetadatakeymenstrualcyclestart.md) value for the first sample in the period to [`true`](https://developer.apple.com/documentation/swift/true). Use [`false`](https://developer.apple.com/documentation/swift/false) for any additional samples. Different samples can use different `menstrualFlow` values to record the changes in flow over time.

## Topics

### Metadata Keys
- [let HKMetadataKeyMenstrualCycleStart: String](hkmetadatakeymenstrualcyclestart.md)
  A key that indicates whether the sample represents the start of a menstrual cycle. This metadata key is required for [`menstrualFlow`](hkcategorytypeidentifier/menstrualflow.md) category samples.

## See Also

- [enum HKCategoryValue](hkcategoryvalue.md)
  Categories that are undefined.
- [struct HKCategoryTypeIdentifier](hkcategorytypeidentifier.md)
  Identifiers for creating category types.
- [class HKCategoryType](hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
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
- [static let basalBodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalbodytemperature.md)
  A quantity sample type that records the user’s basal body temperature.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/menstrualflow)*