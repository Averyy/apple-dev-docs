# literUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring volume, using liter units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func literUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring volume based on liters and the provided prefix.

#### Discussion

This method is used to create prefixed versions of liters, typically milliliter units, as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func liter() -> Self](hkunit/liter.md)
  Returns a HealthKit unit for measuring volume in liters.
- [class func fluidOunceUS() -> Self](hkunit/fluidounceus.md)
  Returns a HealthKit unit for measuring volume in US fluid ounces.
- [class func fluidOunceImperial() -> Self](hkunit/fluidounceimperial.md)
  Returns a HealthKit unit for measuring volume in imperial fluid ounces.
- [class func cupUS() -> Self](hkunit/cupus.md)
  Returns a HealthKit unit for measuring volume in US cups.
- [class func cupImperial() -> Self](hkunit/cupimperial.md)
  Returns a HealthKit unit for measuring volume in imperial cups.
- [class func pintUS() -> Self](hkunit/pintus.md)
  Returns a HealthKit unit for measuring volume in US pints.
- [class func pintImperial() -> Self](hkunit/pintimperial.md)
  Returns a HealthKit unit for measuring volume in imperial pints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/literunit(with:))*