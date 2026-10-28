# distanceSwimming

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the distance the user has moved while swimming.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let distanceSwimming: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierDistanceSwimming;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## Discussion

These samples use length units (described in [`HKUnit`](../hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Related Documentation
- [struct HKQuantityTypeIdentifier](../hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](../hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](../hkquantity.md)
  An object that stores a value for a given unit.
### Activity
- [static let stepCount: HKQuantityTypeIdentifier](./stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](./distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
- [static let runningSpeed: HKQuantityTypeIdentifier](./runningspeed.md)
  A quantity sample type that measures the runner’s speed.
- [static let runningStrideLength: HKQuantityTypeIdentifier](./runningstridelength.md)
  A quantity sample type that measures the distance covered by a single step while running.
- [static let runningPower: HKQuantityTypeIdentifier](./runningpower.md)
  A quantity sample type that measures the rate of work required for the runner to maintain their speed.
- [static let runningGroundContactTime: HKQuantityTypeIdentifier](./runninggroundcontacttime.md)
  A quantity sample type that measures the amount of time the runner’s foot is in contact with the ground while running.
- [static let runningVerticalOscillation: HKQuantityTypeIdentifier](./runningverticaloscillation.md)
  A quantity sample type measuring pelvis vertical range of motion during a single running stride.
- [static let distanceCycling: HKQuantityTypeIdentifier](./distancecycling.md)
  A quantity sample type that measures the distance the user has moved by cycling.
- [static let pushCount: HKQuantityTypeIdentifier](./pushcount.md)
  A quantity sample type that measures the number of pushes that the user has performed while using a wheelchair.
- [static let distanceWheelchair: HKQuantityTypeIdentifier](./distancewheelchair.md)
  A quantity sample type that measures the distance the user has moved using a wheelchair.
- [static let swimmingStrokeCount: HKQuantityTypeIdentifier](./swimmingstrokecount.md)
  A quantity sample type that measures the number of strokes performed while swimming.
- [static let distanceDownhillSnowSports: HKQuantityTypeIdentifier](./distancedownhillsnowsports.md)
  A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.
- [static let basalEnergyBurned: HKQuantityTypeIdentifier](./basalenergyburned.md)
  A quantity sample type that measures the resting energy burned by the user.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](./activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.
- [static let flightsClimbed: HKQuantityTypeIdentifier](./flightsclimbed.md)
  A quantity sample type that measures the number flights of stairs that the user has climbed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/distanceswimming)*