# basalEnergyBurned

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the resting energy burned by the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let basalEnergyBurned: HKQuantityTypeIdentifier
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
- [Running workout sessions](running-workout-sessions.md)

#### Discussion

Resting energy is the energy that the user’s body burns to maintain its normal, resting state. The body uses this energy to perform basic functions like breathing, circulating blood, and managing the growth and maintenance of cells. These samples use energy units (described in [`HKUnit`](hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). Sample data may be condensed and/or coalesced by HealthKit. For more information, see [`Accessing condensed workout samples`](accessing-condensed-workout-samples.md).

## See Also

- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](hkquantity.md)
  An object that stores a value for a given unit.
- [static let stepCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
- [static let runningSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningspeed.md)
  A quantity sample type that measures the runner’s speed.
- [static let runningStrideLength: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningstridelength.md)
  A quantity sample type that measures the distance covered by a single step while running.
- [static let runningPower: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningpower.md)
  A quantity sample type that measures the rate of work required for the runner to maintain their speed.
- [static let runningGroundContactTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runninggroundcontacttime.md)
  A quantity sample type that measures the amount of time the runner’s foot is in contact with the ground while running.
- [static let runningVerticalOscillation: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningverticaloscillation.md)
  A quantity sample type measuring pelvis vertical range of motion during a single running stride.
- [static let distanceCycling: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancecycling.md)
  A quantity sample type that measures the distance the user has moved by cycling.
- [static let pushCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/pushcount.md)
  A quantity sample type that measures the number of pushes that the user has performed while using a wheelchair.
- [static let distanceWheelchair: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewheelchair.md)
  A quantity sample type that measures the distance the user has moved using a wheelchair.
- [static let swimmingStrokeCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/swimmingstrokecount.md)
  A quantity sample type that measures the number of strokes performed while swimming.
- [static let distanceSwimming: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distanceswimming.md)
  A quantity sample type that measures the distance the user has moved while swimming.
- [static let distanceDownhillSnowSports: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancedownhillsnowsports.md)
  A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.
- [static let flightsClimbed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/flightsclimbed.md)
  A quantity sample type that measures the number flights of stairs that the user has climbed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/basalenergyburned)*