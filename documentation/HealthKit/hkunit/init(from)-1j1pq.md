# init(from:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Converts an energy formatter enumeration value into a corresponding HealthKit unit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(from energyFormatterUnit: EnergyFormatter.Unit)
```

```objc
+ (instancetype) unitFromEnergyFormatterUnit:(NSEnergyFormatterUnit) energyFormatterUnit;
```

## Return Value

A HealthKit unit object, or `nil` if the unit parameter is not a valid energy formatter unit value.

## Parameters

- `energyFormatterUnit`: A valid energy formatter unit value. For a list of possible energy formatter unit values, see [`EnergyFormatter.Unit`](../../Foundation/energyformatter/unit.md).

## See Also

### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](./energyformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](./lengthformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](./init%28from%29-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](./massformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](./init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/init(from:)-1j1pq)*