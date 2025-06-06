# unitDivided(by:)

**Framework**: HealthKit  
**Kind**: method

Creates a complex unit by dividing the receiving unit by another unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func unitDivided(by unit: HKUnit) -> HKUnit
```

#### Return Value

A new, complex unit.

#### Discussion

This method creates a new, complex unit by dividing one unit by another. For example, you can create a meters-per-second unit by dividing a meters unit by a seconds unit, as shown below.

## Parameters

- `unit`: The unit to be divided.

## See Also

- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [func unitMultiplied(by: HKUnit) -> HKUnit](hkunit/unitmultiplied(by:).md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitRaised(toPower: Int) -> HKUnit](hkunit/unitraised(topower:).md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](hkunit/reciprocal.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitdivided(by:))*