# unitMultiplied(by:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Creates a complex unit by multiplying the receiving unit with another unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
func unitMultiplied(by unit: HKUnit) -> HKUnit
```

```objc
- (HKUnit *) unitMultipliedByUnit:(HKUnit *) unit;
```

## Return Value

A new, complex unit.

## Discussion

You can create a complex unit by multiplying two units together. For example, you could create a foot-pound unit by multiplying a foot unit by a pound unit as shown below.

**Swift**:

```swift
let foot = HKUnit.footUnit()
let pound = HKUnit.poundUnit()
let footPound = foot.unitMultipliedByUnit(pound)
```

**Objective-C**:

```objc
HKUnit *foot = [HKUnit footUnit];
HKUnit *pound = [HKUnit poundUnit];
HKUnit *footPound = [foot unitMultipliedByUnit:pound];
```

## Parameters

- `unit`: The unit to be multiplied.

## See Also

### Related Documentation
- [convenience init(from: String)](./init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
### Performing unit math
- [func unitDivided(by: HKUnit) -> HKUnit](./unitdivided%28by%29.md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func unitRaised(toPower: Int) -> HKUnit](./unitraised%28topower%29.md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](./reciprocal%28%29.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitmultiplied(by:))*