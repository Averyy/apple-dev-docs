# init(from:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Converts a length formatter enumeration value into a corresponding HealthKit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(from lengthFormatterUnit: LengthFormatter.Unit)
```

```objc
+ (instancetype) unitFromLengthFormatterUnit:(NSLengthFormatterUnit) lengthFormatterUnit;
```

#### Return Value

A HealthKit unit object, or `nil` if the unit parameter is not a valid length formatter unit value.

## Parameters

- `lengthFormatterUnit`: A valid length formatter unit value. For a list of possible length formatter unit values, see [`LengthFormatter.Unit`](../../Foundation/lengthformatter/unit.md).

## See Also

### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](./energyformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](./init%28from%29-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](./lengthformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](./massformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](./init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/init(from:)-55e1u)*