# unitMultiplied(by:)

**Framework**: HealthKit  
**Kind**: method

Creates a complex unit by multiplying the receiving unit with another unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func unitMultiplied(by unit: HKUnit) -> HKUnit
```

#### Return Value

A new, complex unit.

#### Discussion

You can create a complex unit by multiplying two units together. For example, you could create a foot-pound unit by multiplying a foot unit by a pound unit as shown below.

## Parameters

- `unit`: The unit to be multiplied.

## See Also

- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [func unitDivided(by: HKUnit) -> HKUnit](hkunit/unitdivided(by:).md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func unitRaised(toPower: Int) -> HKUnit](hkunit/unitraised(topower:).md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](hkunit/reciprocal.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitmultiplied(by:))*