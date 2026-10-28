# gramUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func gramUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) gramUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

## Return Value

A HealthKit unit for measuring mass based on grams and the given prefix.

## Discussion

This method is used to create prefixed versions of grams, typically kilogram units, as shown below.

**Swift**:

```swift
let kg = HKUnit.gramUnitWithMetricPrefix(.Kilo)
let kg = HKUnit.gramUnitWithMetricPrefix(.Kilo)
```

**Objective-C**:

```objc
HKUnit *kg = [HKUnit gramUnitWithMetricPrefix:HKMetricPrefixKilo];
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing mass units
- [class func gram() -> Self](./gram%28%29.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func ounce() -> Self](./ounce%28%29.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](./pound%28%29.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](./stone%28%29.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](./moleunit%28withmolarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](./moleunit%28with,molarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](../hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/gramunit(with:))*