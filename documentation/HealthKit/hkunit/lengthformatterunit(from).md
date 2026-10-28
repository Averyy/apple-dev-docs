# lengthFormatterUnit(from:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Converts a HealthKit unit object into a corresponding length formatter enumeration value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func lengthFormatterUnit(from unit: HKUnit) -> LengthFormatter.Unit
```

```objc
+ (NSLengthFormatterUnit) lengthFormatterUnitFromUnit:(HKUnit *) unit;
```

## Return Value

A length formatter unit value. For a list of possible length formatter unit values see [`LengthFormatter.Unit`](../../Foundation/lengthformatter/unit.md).

## Parameters

- `unit`: A valid HealthKit unit object.  If the unit is not a length unit, this method throws an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

## See Also

### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](./energyformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](./init%28from%29-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [convenience init(from: LengthFormatter.Unit)](./init%28from%29-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](./massformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](./init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/lengthformatterunit(from:))*