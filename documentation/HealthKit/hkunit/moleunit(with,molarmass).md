# moleUnit(with:molarMass:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func moleUnit(with prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self
```

```objc
+ (instancetype) moleUnitWithMetricPrefix:(HKMetricPrefix) prefix molarMass:(double) gramsPerMole;
```

#### Return Value

A HealthKit unit for measuring mass in moles.

#### Discussion

This method allows the creation of units to measure mass in moles with a given metric prefix and molecular mass. For example, to measure blood glucose in millimoles, you need to use both the correct prefix (milli-) and the [`HKUnitMolarMassBloodGlucose`](../hkunitmolarmassbloodglucose.md) constant.).

**Swift**:

```swift
let millimolesOfBloodGlucose =
    HKUnit.moleUnitWithMetricPrefix(HKMetricPrefix.Milli,
                                    molarMass: HKUnitMolarMassBloodGlucose)
```

**Objective-C**:

```objc
HKUnit *millimolesOfBloodGlucose =
[HKUnit moleUnitWithMetricPrefix:HKMetricPrefixMilli molarMass:HKUnitMolarMassBloodGlucose];
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).
- `gramsPerMole`: The molar mass, in grams per mole, of the item to be weighed.

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
- [class func moleUnit(withMolarMass: Double) -> Self](./moleunit%28withmolarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](../hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/moleunit(with:molarmass:))*