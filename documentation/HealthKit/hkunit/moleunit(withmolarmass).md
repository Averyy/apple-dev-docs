# moleUnit(withMolarMass:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring mass in moles for a given molar mass.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func moleUnit(withMolarMass gramsPerMole: Double) -> Self
```

```objc
+ (instancetype) moleUnitWithMolarMass:(double) gramsPerMole;
```

#### Return Value

A HealthKit unit for measuring the mass of an item in moles.

#### Discussion

To create a unit for measuring an item in moles, you need to know that item’s molar mass. For example, you can use the [`HKUnitMolarMassBloodGlucose`](../hkunitmolarmassbloodglucose.md) constant to create the mole unit for blood glucose, as shown below.

**Swift**:

```swift
let molesOfBloodGlucose = HKUnit.moleUnitWithMolarMass(HKUnitMolarMassBloodGlucose)
```

**Objective-C**:

```objc
HKUnit *molesOfBloodGlucose =
[HKUnit moleUnitWithMolarMass:HKUnitMolarMassBloodGlucose];
```

## Parameters

- `gramsPerMole`: The molar mass (in g/mol) of the item to be weighed.

## See Also

### Constructing mass units
- [class func gram() -> Self](./gram%28%29.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func gramUnit(with: HKMetricPrefix) -> Self](./gramunit%28with%29.md)
  Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.
- [class func ounce() -> Self](./ounce%28%29.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](./pound%28%29.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](./stone%28%29.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](./moleunit%28with,molarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](../hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/moleunit(withmolarmass:))*