# unitString

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, readonly) NSString * unitString;
```

## Discussion

This property contains a string using the format required by [`init(from:)`](./init%28from%29-9qont.md).

## See Also

### Related Documentation
- [func reciprocal() -> HKUnit](./reciprocal%28%29.md)
  Returns a complex unit representing the unit’s reciprocal.
- [func unitMultiplied(by: HKUnit) -> HKUnit](./unitmultiplied%28by%29.md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitRaised(toPower: Int) -> HKUnit](./unitraised%28topower%29.md)
  Creates a complex unit by raising the unit to the given power.
- [func unitDivided(by: HKUnit) -> HKUnit](./unitdivided%28by%29.md)
  Creates a complex unit by dividing the receiving unit by another unit.
### Working with units
- [convenience init(from: String)](./init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
- [func isNull() -> Bool](./isnull%28%29.md)
  Returns a Boolean value indicating whether the unit is null.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitstring)*