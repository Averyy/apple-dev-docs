# bodyMass

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the user’s weight.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let bodyMass: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierBodyMass;
```

## Mentions

- [Saving data to HealthKit](../saving-data-to-healthkit.md)

## Discussion

These samples use mass units (described in [`HKUnit`](../hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Related Documentation
- [struct HKQuantityTypeIdentifier](../hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](../hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](../hkquantity.md)
  An object that stores a value for a given unit.
### Body measurements
- [static let height: HKQuantityTypeIdentifier](./height.md)
  A quantity sample type that measures the user’s height.
- [static let bodyMassIndex: HKQuantityTypeIdentifier](./bodymassindex.md)
  A quantity sample type that measures the user’s body mass index.
- [static let leanBodyMass: HKQuantityTypeIdentifier](./leanbodymass.md)
  A quantity sample type that measures the user’s lean body mass.
- [static let bodyFatPercentage: HKQuantityTypeIdentifier](./bodyfatpercentage.md)
  A quantity sample type that measures the user’s body fat percentage.
- [static let waistCircumference: HKQuantityTypeIdentifier](./waistcircumference.md)
  A quantity sample type that measures the user’s waist circumference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/bodymass)*