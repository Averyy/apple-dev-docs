# unitDivided(by:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Creates a complex unit by dividing the receiving unit by another unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
func unitDivided(by unit: HKUnit) -> HKUnit
```

```objc
- (HKUnit *) unitDividedByUnit:(HKUnit *) unit;
```

#### Return Value

A new, complex unit.

#### Discussion

This method creates a new, complex unit by dividing one unit by another. For example, you can create a meters-per-second unit by dividing a meters unit by a seconds unit, as shown below.

**Swift**:

```swift
let meters = HKUnit.meterUnit()
let seconds = HKUnit.secondUnit()
let metersPerSecond = meters.unitDividedByUnit(seconds)
```

**Objective-C**:

```objc
HKUnit *meters = [HKUnit meterUnit];
HKUnit *seconds = [HKUnit secondUnit];
HKUnit *metersPerSecond = [meters unitDividedByUnit:seconds];
```

## Parameters

- `unit`: The unit to be divided.

## See Also

### Related Documentation
- [convenience init(from: String)](./init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
### Performing unit math
- [func unitMultiplied(by: HKUnit) -> HKUnit](./unitmultiplied%28by%29.md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitRaised(toPower: Int) -> HKUnit](./unitraised%28topower%29.md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](./reciprocal%28%29.md)
  Returns a complex unit representing the unit’s reciprocal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/unitdivided(by:))*