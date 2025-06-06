# unitRaised(toPower:)

**Framework**: HealthKit  
**Kind**: method

Creates a complex unit by raising the unit to the given power.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func unitRaised(toPower power: Int) -> HKUnit
```

#### Return Value

A new, complex unit.

#### Discussion

This method creates a new, complex unit by raising the unit this method is called on by the given power. This task is often only one step in a series of operations. For example, you can use this method to create a meters-per-second-squared unit as shown below.

## Parameters

- `power`: The power by which to raise the unit.

## See Also

- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [func unitMultiplied(by: HKUnit) -> HKUnit](hkunit/unitmultiplied(by:).md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitDivided(by: HKUnit) -> HKUnit](hkunit/unitdivided(by:).md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func reciprocal() -> HKUnit](hkunit/reciprocal.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitraised(topower:))*