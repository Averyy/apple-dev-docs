# bodyFatPercentage

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the user’s body fat percentage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let bodyFatPercentage: HKQuantityTypeIdentifier
```

#### Discussion

These samples use percent units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

## See Also

- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](hkquantity.md)
  An object that stores a value for a given unit.
- [static let height: HKQuantityTypeIdentifier](hkquantitytypeidentifier/height.md)
  A quantity sample type that measures the user’s height.
- [static let bodyMass: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodymass.md)
  A quantity sample type that measures the user’s weight.
- [static let bodyMassIndex: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodymassindex.md)
  A quantity sample type that measures the user’s body mass index.
- [static let leanBodyMass: HKQuantityTypeIdentifier](hkquantitytypeidentifier/leanbodymass.md)
  A quantity sample type that measures the user’s lean body mass.
- [static let waistCircumference: HKQuantityTypeIdentifier](hkquantitytypeidentifier/waistcircumference.md)
  A quantity sample type that measures the user’s waist circumference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/bodyfatpercentage)*