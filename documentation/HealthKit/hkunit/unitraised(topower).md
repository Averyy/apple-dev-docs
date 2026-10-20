# unitRaised(toPower:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Creates a complex unit by raising the unit to the given power.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
func unitRaised(toPower power: Int) -> HKUnit
```

```objc
- (HKUnit *) unitRaisedToPower:(NSInteger) power;
```

#### Return Value

A new, complex unit.

#### Discussion

This method creates a new, complex unit by raising the unit this method is called on by the given power. This task is often only one step in a series of operations. For example, you can use this method to create a meters-per-second-squared unit as shown below.

**Swift**:

```swift
let meters = HKUnit.meterUnit()
let seconds = HKUnit.secondUnit()
let squaredSeconds = seconds.unitRaisedToPower(2)
let metersPerSecondSquared = meters.unitDividedByUnit(squaredSeconds)
```

**Objective-C**:

```objc
HKUnit *meters = [HKUnit meterUnit];
HKUnit *seconds = [HKUnit secondUnit];
HKUnit *squaredSeconds = [seconds unitRaisedToPower:2];
HKUnit *metersPerSecondSquared = [meters unitDividedByUnit:squaredSeconds];
```

## Parameters

- `power`: The power by which to raise the unit.

## See Also

### Related Documentation
- [convenience init(from: String)](./init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
### Performing unit math
- [func unitMultiplied(by: HKUnit) -> HKUnit](./unitmultiplied%28by%29.md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitDivided(by: HKUnit) -> HKUnit](./unitdivided%28by%29.md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func reciprocal() -> HKUnit](./reciprocal%28%29.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitraised(topower:))*