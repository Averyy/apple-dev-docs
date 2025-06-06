# unitString

**Framework**: HealthKit  
**Kind**: property

A string representation of the unit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var unitString: String { get }
```

#### Discussion

This property contains a string using the format required by [`init(from:)`](hkunit/init(from:)-9qont.md).

## See Also

- [func reciprocal() -> HKUnit](hkunit/reciprocal.md)
  Returns a complex unit representing the unit’s reciprocal.
- [func unitMultiplied(by: HKUnit) -> HKUnit](hkunit/unitmultiplied(by:).md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitRaised(toPower: Int) -> HKUnit](hkunit/unitraised(topower:).md)
  Creates a complex unit by raising the unit to the given power.
- [func unitDivided(by: HKUnit) -> HKUnit](hkunit/unitdivided(by:).md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [func isNull() -> Bool](hkunit/isnull.md)
  Returns a Boolean value indicating whether the unit is null.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitstring)*