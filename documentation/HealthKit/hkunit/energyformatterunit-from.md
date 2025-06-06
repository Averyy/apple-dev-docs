# energyFormatterUnit(from:)

**Framework**: HealthKit  
**Kind**: method

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

#### Return Value

An energy formatter unit value. For a list of possible energy formatter unit values, see [`EnergyFormatter.Unit`](https://developer.apple.com/documentation/Foundation/EnergyFormatter/Unit).

## Parameters

- `unit`: A valid HealthKit unit object. If the unit is not an energy-type unit, this method throws an exception ( ).

## See Also

- [convenience init(from: EnergyFormatter.Unit)](hkunit/init(from:)-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](hkunit/lengthformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](hkunit/init(from:)-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](hkunit/massformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](hkunit/init(from:)-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/energyformatterunit(from:))*