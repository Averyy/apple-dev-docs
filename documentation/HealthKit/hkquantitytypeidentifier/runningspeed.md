# runningSpeed

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the runner’s speed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let runningSpeed: HKQuantityTypeIdentifier
```

#### Discussion

These samples use distance per time units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). During outdoor running workouts, the system automatically records running speed samples on Apple Watch. Sample data may be condensed and/or coalesced by HealthKit. For more information, see [`Accessing condensed workout samples`](accessing-condensed-workout-samples.md).

## See Also

- [static let appleWalkingSteadiness: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applewalkingsteadiness.md)
  A quantity sample type that measures the steadiness of the user’s gait.
- [static let appleWalkingSteadinessEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/applewalkingsteadinessevent.md)
  A category sample type that records an incident where the user showed a reduced score for their gait’s steadiness.
- [static let sixMinuteWalkTestDistance: HKQuantityTypeIdentifier](hkquantitytypeidentifier/sixminutewalktestdistance.md)
  A quantity sample type that stores the distance a user can walk during a six-minute walk test.
- [static let walkingSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingspeed.md)
  A quantity sample type that measures the user’s average speed when walking steadily over flat ground.
- [static let walkingStepLength: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingsteplength.md)
  A quantity sample type that measures the average length of the user’s step when walking steadily over flat ground.
- [static let walkingAsymmetryPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingasymmetrypercentage.md)
  A quantity sample type that measures the percentage of steps in which one foot moves at a different speed than the other when walking on flat ground.
- [static let walkingDoubleSupportPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingdoublesupportpercentage.md)
  A quantity sample type that measures the percentage of time when both of the user’s feet touch the ground while walking steadily over flat ground.
- [static let stairAscentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairascentspeed.md)
  A quantity sample type measuring the user’s speed while climbing a flight of stairs.
- [static let stairDescentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairdescentspeed.md)
  A quantity sample type measuring the user’s speed while descending a flight of stairs.
- [static let stepCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
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
- [static let basalEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalenergyburned.md)
  A quantity sample type that measures the resting energy burned by the user.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.
- [static let flightsClimbed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/flightsclimbed.md)
  A quantity sample type that measures the number flights of stairs that the user has climbed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningspeed)*