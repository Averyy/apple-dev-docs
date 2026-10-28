# physicalEffort

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the estimated amount of energy being used to perform a task excluding other factors such as temperature, altitude, or heart rate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let physicalEffort: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierPhysicalEffort;
```

## Discussion

These samples use power in Metabolic Equivalent of Task (METs) units (described in [`HKUnit`](../hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)). Physical effort is estimated and recorded automatically by Apple Watch.

## See Also

### Related Documentation
- [let HKMetadataKeyAverageMETs: String](../hkmetadatakeyaveragemets.md)
  A key that indicates the average Metabolic Equivalent of Task (METs) during a workout.
### Activity
- [static let stepCount: HKQuantityTypeIdentifier](./stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](./distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
- [static let runningGroundContactTime: HKQuantityTypeIdentifier](./runninggroundcontacttime.md)
  A quantity sample type that measures the amount of time the runner’s foot is in contact with the ground while running.
- [static let runningPower: HKQuantityTypeIdentifier](./runningpower.md)
  A quantity sample type that measures the rate of work required for the runner to maintain their speed.
- [static let runningSpeed: HKQuantityTypeIdentifier](./runningspeed.md)
  A quantity sample type that measures the runner’s speed.
- [static let runningStrideLength: HKQuantityTypeIdentifier](./runningstridelength.md)
  A quantity sample type that measures the distance covered by a single step while running.
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
- [static let distanceSwimming: HKQuantityTypeIdentifier](./distanceswimming.md)
  A quantity sample type that measures the distance the user has moved while swimming.
- [static let distanceDownhillSnowSports: HKQuantityTypeIdentifier](./distancedownhillsnowsports.md)
  A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.
- [static let basalEnergyBurned: HKQuantityTypeIdentifier](./basalenergyburned.md)
  A quantity sample type that measures the resting energy burned by the user.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](./activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/physicaleffort)*