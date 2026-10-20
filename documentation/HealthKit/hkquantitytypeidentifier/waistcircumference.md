# waistCircumference

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the user’s waist circumference.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let waistCircumference: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierWaistCircumference;
```

#### Discussion

These samples use length units (described in [`HKUnit`](../hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Body measurements
- [static let height: HKQuantityTypeIdentifier](./height.md)
  A quantity sample type that measures the user’s height.
- [static let bodyMass: HKQuantityTypeIdentifier](./bodymass.md)
  A quantity sample type that measures the user’s weight.
- [static let bodyMassIndex: HKQuantityTypeIdentifier](./bodymassindex.md)
  A quantity sample type that measures the user’s body mass index.
- [static let leanBodyMass: HKQuantityTypeIdentifier](./leanbodymass.md)
  A quantity sample type that measures the user’s lean body mass.
- [static let bodyFatPercentage: HKQuantityTypeIdentifier](./bodyfatpercentage.md)
  A quantity sample type that measures the user’s body fat percentage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/waistcircumference)*