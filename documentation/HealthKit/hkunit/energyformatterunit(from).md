# energyFormatterUnit(from:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Converts a HealthKit unit object into a corresponding energy formatter enumeration value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func energyFormatterUnit(from unit: HKUnit) -> EnergyFormatter.Unit
```

```objc
+ (NSEnergyFormatterUnit) energyFormatterUnitFromUnit:(HKUnit *) unit;
```

#### Return Value

An energy formatter unit value. For a list of possible energy formatter unit values, see [`EnergyFormatter.Unit`](../../Foundation/energyformatter/unit.md).

## Parameters

- `unit`: A valid HealthKit unit object. If the unit is not an energy-type unit, this method throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

## See Also

### Working with formatter units
- [convenience init(from: EnergyFormatter.Unit)](./init%28from%29-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](./lengthformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](./init%28from%29-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](./massformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](./init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/energyformatterunit(from:))*