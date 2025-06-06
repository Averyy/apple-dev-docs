# walkingAsymmetryPercentage

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the percentage of steps in which one foot moves at a different speed than the other when walking on flat ground.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let walkingAsymmetryPercentage: HKQuantityTypeIdentifier
```

#### Discussion

Walking asymmetry is the percent of time that a user’s steps with one foot are faster or slower than the other foot. The system automatically records walking asymmetry samples on iPhone 8 or later. The user must carry their phone near their waist—such as in a pocket—and walk steadily on flat ground. The system records the phone’s location using the [`HKMetadataKeyDevicePlacementSide`](hkmetadatakeydeviceplacementside.md) metadata key. The system records 10 to 30 walking asymmetry samples on a typical day. iPhone doesn’t record walking asymmetry samples if the user’s wheelchair status is on.

These samples use percentage units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). For example, the following code creates a percentage unit.

```swift
let percentage = HKUnit.percent()
```

The sample’s [`quantity`](hkquantitysample/quantity.md) property represents the percent of asymmetrical steps between the sample’s [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) properties.

## See Also

- [enum HKDevicePlacementSide](hkdeviceplacementside.md)
  Values that indicate the placement of the device that measured a sample.
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
- [static let walkingDoubleSupportPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingdoublesupportpercentage.md)
  A quantity sample type that measures the percentage of time when both of the user’s feet touch the ground while walking steadily over flat ground.
- [static let stairAscentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairascentspeed.md)
  A quantity sample type measuring the user’s speed while climbing a flight of stairs.
- [static let stairDescentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairdescentspeed.md)
  A quantity sample type measuring the user’s speed while descending a flight of stairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/walkingasymmetrypercentage)*