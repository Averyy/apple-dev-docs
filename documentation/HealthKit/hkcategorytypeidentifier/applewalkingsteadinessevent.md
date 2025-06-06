# appleWalkingSteadinessEvent

**Framework**: HealthKit  
**Kind**: property

A category sample type that records an incident where the user showed a reduced score for their gait’s steadiness.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let appleWalkingSteadinessEvent: HKCategoryTypeIdentifier
```

#### Discussion

Samples of this type use values from the [`HKCategoryValueAppleWalkingSteadinessEvent`](hkcategoryvalueapplewalkingsteadinessevent.md) enumeration.

Walking Steadiness events are read-only. You can request permission to read the samples using this identifier, but you can’t request authorization to share them. This means you can’t save new Walking Steadiness events to the HealthKit store. To add test data in iOS Simulator, open the Health app and select Browse > Mobility > Walking Steadiness Notifications > Add Data.

## See Also

- [static let appleWalkingSteadiness: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applewalkingsteadiness.md)
  A quantity sample type that measures the steadiness of the user’s gait.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/applewalkingsteadinessevent)*