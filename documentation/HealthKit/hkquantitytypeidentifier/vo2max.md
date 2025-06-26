# vo2Max

**Framework**: HealthKit  
**Kind**: property

A quantity sample that measures the maximal oxygen consumption during exercise.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let vo2Max: HKQuantityTypeIdentifier
```

#### Discussion

VO2max—the maximum amount of oxygen your body can consume during exercise— is a strong predictor of overall health. Clinical tests measure VO2max by having the patient exercise on a treadmill or bike, with an intensity that increases every few minutes until exhaustion.

On Apple Watch Series 3 or later, the system automatically saves [`vo2Max`](hkquantitytypeidentifier/vo2max.md) samples to HealthKit. The watch estimates the user’s VO2max based on data gathered while the user is walking or running outdoors. For more information, see [`Understand Estimated Test Results`](hkquantitytypeidentifier/vo2max#Understand-Estimated-Test-Results.md).

You can also create and save your own [`vo2Max`](hkquantitytypeidentifier/vo2max.md) samples—for example, when creating an app that records the results of tests performed in a clinic. When creating [`vo2Max`](hkquantitytypeidentifier/vo2max.md) samples, use the [`HKMetadataKeyVO2MaxTestType`](hkmetadatakeyvo2maxtesttype.md) metadata key to specify the type of test used to generate the sample.

[`vo2Max`](hkquantitytypeidentifier/vo2max.md) samples use volume/mass/time units (described in [`HKUnit`](hkunit.md)), measured in ml/kg /min. They measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

##### Understand Estimated Test Results

Apple Watch Series 3 and later estimates the user’s VO2max by measuring the user’s heart rate response to exercise. The system can generate VO2max samples after an outdoor walk, outdoor run, or hiking workout. During the outdoor activity, the user must cover relatively flat ground (a grade of less than 5% incline or decline) with adequate GPS, heart rate signal quality, and sufficient exertion. The user must maintain a heart rate approximately greater than or equal to 130% of their resting heart rate. The system can estimate VO2max ranges from 14-60 ml/kg/min

The user must wear their Apple Watch for at least one day before the system can generate the first [`vo2Max`](hkquantitytypeidentifier/vo2max.md) sample. Additionally, the system doesn’t generate a [`vo2Max`](hkquantitytypeidentifier/vo2max.md) sample on the user’s first workout.

Apple Watch estimates  based on sub-maximal predictions rather than . Users don’t need to achieve peak heart rate to receive an estimate; however, the system does need to estimate their peak heart rate. Users who take medications that may reduce their peak heart rate can toggle a medication switch in the Health app to enable more accurate VO2max estimates.

## Topics

### Metadata Keys
- [let HKMetadataKeyVO2MaxTestType: String](hkmetadatakeyvo2maxtesttype.md)
  The method used to calculate the user’s VO2 max rate.

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
- [static let basalEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalenergyburned.md)
  A quantity sample type that measures the resting energy burned by the user.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/vo2max)*