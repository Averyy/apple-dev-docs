# HKUnitMolarMassBloodGlucose

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The molecular mass of blood glucose, typically used to create mole units for blood glucose.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var HKUnitMolarMassBloodGlucose: Double { get }
```

```c
#define HKUnitMolarMassBloodGlucose
```

## See Also

### Constructing mass units
- [class func gram() -> Self](./hkunit/gram%28%29.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func gramUnit(with: HKMetricPrefix) -> Self](./hkunit/gramunit%28with%29.md)
  Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.
- [class func ounce() -> Self](./hkunit/ounce%28%29.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](./hkunit/pound%28%29.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](./hkunit/stone%28%29.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](./hkunit/moleunit%28withmolarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](./hkunit/moleunit%28with,molarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunitmolarmassbloodglucose)*