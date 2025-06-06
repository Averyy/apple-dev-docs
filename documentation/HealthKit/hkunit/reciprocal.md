# reciprocal()

**Framework**: HealthKit  
**Kind**: method

Returns a complex unit representing the unit’s reciprocal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func reciprocal() -> HKUnit
```

#### Return Value

A complex unit that is the reciprocal of the unit the method was called on.

#### Discussion

This method creates a new, complex unit by dividing 1 by the unit the method was called on. This is often only one step in a series of operations. For example, you can use this method to create a meters-per-second unit, as shown below.

## See Also

- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [func unitMultiplied(by: HKUnit) -> HKUnit](hkunit/unitmultiplied(by:).md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitDivided(by: HKUnit) -> HKUnit](hkunit/unitdivided(by:).md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func unitRaised(toPower: Int) -> HKUnit](hkunit/unitraised(topower:).md)
  Creates a complex unit by raising the unit to the given power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/reciprocal())*