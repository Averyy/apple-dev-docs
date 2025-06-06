# init(from:)

**Framework**: HealthKit  
**Kind**: init

Converts a mass formatter enumeration value into a corresponding HealthKit unit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(from massFormatterUnit: MassFormatter.Unit)
```

#### Return Value

A HealthKit unit object, or `nil` if the unit parameter is not a valid energy formatter unit value.

## Parameters

- `massFormatterUnit`: A valid mass formatter unit value. For a list of possible mass formatter unit values, see  .

## See Also

- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](hkunit/energyformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](hkunit/init(from:)-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](hkunit/lengthformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](hkunit/init(from:)-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](hkunit/massformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/init(from:)-7h2li)*