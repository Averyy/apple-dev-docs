# stairAscentSpeed

**Framework**: HealthKit  
**Kind**: property

A quantity sample type measuring the user’s speed while climbing a flight of stairs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let stairAscentSpeed: HKQuantityTypeIdentifier
```

#### Discussion

This is a measurement of how fast the user walks up stairs. The system automatically records stair ascent samples on Apple Watch Series 5 or later. The user must climb a 10-foot (3-meter) flight of steps while wearing the watch. The system records 20 samples on a typical day; however, some days may go over 100 samples, for example if the user goes on a long hike. The watch doesn’t record stair ascent speed samples if the user’s wheelchair status is on.

These samples use distance/time units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). For example, the following code shows two ways to create a meters/second unit. The first uses explicit constructors, while the second initializes the unit from a string.

```swift
let mps = HKUnit.meter().unitDivided(by: HKUnit.second())
let mpsFromString = HKUnit(from: "m/s")
```

The sample’s [`quantity`](hkquantitysample/quantity.md) property represents the average ascent speed between the sample’s [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) properties.

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
- [static let walkingAsymmetryPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingasymmetrypercentage.md)
  A quantity sample type that measures the percentage of steps in which one foot moves at a different speed than the other when walking on flat ground.
- [static let walkingDoubleSupportPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingdoublesupportpercentage.md)
  A quantity sample type that measures the percentage of time when both of the user’s feet touch the ground while walking steadily over flat ground.
- [static let stairDescentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairdescentspeed.md)
  A quantity sample type measuring the user’s speed while descending a flight of stairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/stairascentspeed)*