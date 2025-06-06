# moleUnit(with:molarMass:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func moleUnit(with prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self
```

#### Return Value

A HealthKit unit for measuring mass in moles.

#### Discussion

This method allows the creation of units to measure mass in moles with a given metric prefix and molecular mass. For example, to measure blood glucose in millimoles, you need to use both the correct prefix (milli-) and the [`HKUnitMolarMassBloodGlucose`](hkunitmolarmassbloodglucose.md) constant.).

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .
- `gramsPerMole`: The molar mass, in grams per mole, of the item to be weighed.

## See Also

- [class func gram() -> Self](hkunit/gram.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func gramUnit(with: HKMetricPrefix) -> Self](hkunit/gramunit(with:).md)
  Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.
- [class func ounce() -> Self](hkunit/ounce.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](hkunit/pound.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](hkunit/stone.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](hkunit/moleunit(withmolarmass:).md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/moleunit(with:molarmass:))*