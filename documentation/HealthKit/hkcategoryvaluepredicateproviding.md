# HKCategoryValuePredicateProviding

**Framework**: HealthKit  
**Kind**: protocol

A protocol for objects that produce predicates that match category value samples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol HKCategoryValuePredicateProviding : Hashable, RawRepresentable
```

## Topics

### Creating predicates
- [static func predicateForSamples(NSComparisonPredicate.Operator, value: Self) -> NSPredicate](hkcategoryvaluepredicateproviding/predicateforsamples(_:value:).md)
  Returns a predicate that checks a category sample’s value.
- [static func predicateForSamples(equalTo: Set<Self>) -> NSPredicate](hkcategoryvaluepredicateproviding/predicateforsamples(equalto:).md)
  Returns a predicate that checks whether a category sample is equal to the provided set of values.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
### Conforming Types
- [HKCategoryValue](hkcategoryvalue.md)
- [HKCategoryValueAppetiteChanges](hkcategoryvalueappetitechanges.md)
- [HKCategoryValueAppleStandHour](hkcategoryvalueapplestandhour.md)
- [HKCategoryValueAppleWalkingSteadinessEvent](hkcategoryvalueapplewalkingsteadinessevent.md)
- [HKCategoryValueCervicalMucusQuality](hkcategoryvaluecervicalmucusquality.md)
- [HKCategoryValueContraceptive](hkcategoryvaluecontraceptive.md)
- [HKCategoryValueEnvironmentalAudioExposureEvent](hkcategoryvalueenvironmentalaudioexposureevent.md)
- [HKCategoryValueHeadphoneAudioExposureEvent](hkcategoryvalueheadphoneaudioexposureevent.md)
- [HKCategoryValueLowCardioFitnessEvent](hkcategoryvaluelowcardiofitnessevent.md)
- [HKCategoryValueMenstrualFlow](hkcategoryvaluemenstrualflow.md)
- [HKCategoryValueOvulationTestResult](hkcategoryvalueovulationtestresult.md)
- [HKCategoryValuePregnancyTestResult](hkcategoryvaluepregnancytestresult.md)
- [HKCategoryValuePresence](hkcategoryvaluepresence.md)
- [HKCategoryValueProgesteroneTestResult](hkcategoryvalueprogesteronetestresult.md)
- [HKCategoryValueSeverity](hkcategoryvalueseverity.md)
- [HKCategoryValueSleepAnalysis](hkcategoryvaluesleepanalysis.md)
- [HKCategoryValueVaginalBleeding](hkcategoryvaluevaginalbleeding.md)

## See Also

- [class func predicateForCategorySamples(with: NSComparisonPredicate.Operator, value: Int) -> NSPredicate](hkquery/predicateforcategorysamples(with:value:).md)
  Returns a predicate that checks a category sample’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepredicateproviding)*