# dietaryProtein

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the amount of protein consumed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let dietaryProtein: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierDietaryProtein;
```

## Discussion

These samples use mass units (described in [`HKUnit`](../hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Related Documentation
- [struct HKQuantityTypeIdentifier](../hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](../hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](../hkquantity.md)
  An object that stores a value for a given unit.
### Macronutrients
- [static let dietaryEnergyConsumed: HKQuantityTypeIdentifier](./dietaryenergyconsumed.md)
  A quantity sample type that measures the amount of energy consumed.
- [static let dietaryCarbohydrates: HKQuantityTypeIdentifier](./dietarycarbohydrates.md)
  A quantity sample type that measures the amount of carbohydrates consumed.
- [static let dietaryFiber: HKQuantityTypeIdentifier](./dietaryfiber.md)
  A quantity sample type that measures the amount of fiber consumed.
- [static let dietarySugar: HKQuantityTypeIdentifier](./dietarysugar.md)
  A quantity sample type that measures the amount of sugar consumed.
- [static let dietaryFatTotal: HKQuantityTypeIdentifier](./dietaryfattotal.md)
  A quantity sample type that measures the total amount of fat consumed.
- [static let dietaryFatMonounsaturated: HKQuantityTypeIdentifier](./dietaryfatmonounsaturated.md)
  A quantity sample type that measures the amount of monounsaturated fat consumed.
- [static let dietaryFatPolyunsaturated: HKQuantityTypeIdentifier](./dietaryfatpolyunsaturated.md)
  A quantity sample type that measures the amount of polyunsaturated fat consumed.
- [static let dietaryFatSaturated: HKQuantityTypeIdentifier](./dietaryfatsaturated.md)
  A quantity sample type that measures the amount of saturated fat consumed.
- [static let dietaryCholesterol: HKQuantityTypeIdentifier](./dietarycholesterol.md)
  A quantity sample type that measures the amount of cholesterol consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/dietaryprotein)*