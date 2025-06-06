# gramUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func gramUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring mass based on grams and the given prefix.

#### Discussion

This method is used to create prefixed versions of grams, typically kilogram units, as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func gram() -> Self](hkunit/gram.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func ounce() -> Self](hkunit/ounce.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](hkunit/pound.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](hkunit/stone.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](hkunit/moleunit(withmolarmass:).md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](hkunit/moleunit(with:molarmass:).md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/gramunit(with:))*