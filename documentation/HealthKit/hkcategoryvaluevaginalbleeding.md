# HKCategoryValueVaginalBleeding

**Framework**: HealthKit  
**Kind**: enum

A value that indicates the intensity of vaginal bleeding.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum HKCategoryValueVaginalBleeding
```

#### Overview

Use these values when creating [`HKCategorySample`](hkcategorysample.md) instances for bleeding-related category types, including [`bleedingDuringPregnancy`](hkcategorytypeidentifier/bleedingduringpregnancy.md), [`bleedingAfterMenopause`](hkcategorytypeidentifier/bleedingaftermenopause.md), and other vaginal bleeding types. Each value represents a different intensity level or confirmation of no bleeding.

## Topics

### Specifiying bleeding intensity values
- [HKCategoryValueVaginalBleeding.unspecified](hkcategoryvaluevaginalbleeding/unspecified.md)
  A value that indicates an unspecified amount of vaginal bleeding.
- [HKCategoryValueVaginalBleeding.light](hkcategoryvaluevaginalbleeding/light.md)
  A value that indicates light vaginal bleeding.
- [HKCategoryValueVaginalBleeding.medium](hkcategoryvaluevaginalbleeding/medium.md)
  A value that indicates a medium amount of vaginal bleeding.
- [HKCategoryValueVaginalBleeding.heavy](hkcategoryvaluevaginalbleeding/heavy.md)
  A value that indicates a heavy amount of vaginal bleeding.
- [HKCategoryValueVaginalBleeding.none](hkcategoryvaluevaginalbleeding/none.md)
  A value that indicates no vaginal bleeding.
### Creating a value
- [init?(rawValue: Int)](hkcategoryvaluevaginalbleeding/init(rawvalue:).md)
  Initializes a vaginal bleeding value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [HKCategoryValuePredicateProviding](hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluevaginalbleeding)*