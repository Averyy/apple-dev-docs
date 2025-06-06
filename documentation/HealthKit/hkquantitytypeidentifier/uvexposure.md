# uvExposure

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the user’s exposure to UV radiation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let uvExposure: HKQuantityTypeIdentifier
```

#### Discussion

These samples use count units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). The sample’s value represents the UV index that the user was exposed to during the sample’s duration.

## See Also

- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](hkquantity.md)
  An object that stores a value for a given unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/uvexposure)*