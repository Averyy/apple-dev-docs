# activityType

**Framework**: HealthKit  
**Kind**: property

The workout activity performed during this session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var activityType: HKWorkoutActivityType { get }
```

#### Discussion

For a list of possible activity types, see [`HKWorkoutActivityType`](hkworkoutactivitytype.md).

## See Also

- [init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)](hkworkoutsession/init(activitytype:locationtype:).md)
  Returns a newly instantiated workout session.
- [init(configuration: HKWorkoutConfiguration) throws](hkworkoutsession/init(configuration:).md)
  Returns a newly instantiated workout session.
- [var locationType: HKWorkoutSessionLocationType](hkworkoutsession/locationtype.md)
  A value that indicates whether the workout session occurred indoors or outdoors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/activitytype)*