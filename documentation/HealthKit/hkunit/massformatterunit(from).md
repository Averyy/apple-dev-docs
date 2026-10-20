# massFormatterUnit(from:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Converts a HealthKit unit object into a corresponding mass formatter enumeration value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func massFormatterUnit(from unit: HKUnit) -> MassFormatter.Unit
```

```objc
+ (NSMassFormatterUnit) massFormatterUnitFromUnit:(HKUnit *) unit;
```

#### Return Value

A mass formatter unit value. For a list of possible mass formatter unit values, see [`MassFormatter.Unit`](../../Foundation/massformatter/unit.md).

## Parameters

- `unit`: A valid HealthKit unit object. If the unit is not a mass-type unit, this method throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

## See Also

### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](./energyformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](./init%28from%29-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](./lengthformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](./init%28from%29-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [convenience init(from: MassFormatter.Unit)](./init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/massformatterunit(from:))*