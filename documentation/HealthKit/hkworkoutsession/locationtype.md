# locationType

**Framework**: HealthKit  
**Kind**: property

A value that indicates whether the workout session occurred indoors or outdoors.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var locationType: HKWorkoutSessionLocationType { get }
```

#### Discussion

For a list of possible location values, see [`HKWorkoutSessionLocationType`](hkworkoutsessionlocationtype.md).

## See Also

- [init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)](hkworkoutsession/init(activitytype:locationtype:).md)
  Returns a newly instantiated workout session.
- [init(configuration: HKWorkoutConfiguration) throws](hkworkoutsession/init(configuration:).md)
  Returns a newly instantiated workout session.
- [var activityType: HKWorkoutActivityType](hkworkoutsession/activitytype.md)
  The workout activity performed during this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/locationtype)*