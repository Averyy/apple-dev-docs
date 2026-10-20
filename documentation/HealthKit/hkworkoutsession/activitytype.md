# activityType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout activity performed during this session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`workoutConfiguration`](./workoutconfiguration.md) instead.

## Declaration

```swift
var activityType: HKWorkoutActivityType { get }
```

```objc
@property (readonly) HKWorkoutActivityType activityType;
```

#### Discussion

For a list of possible activity types, see [`HKWorkoutActivityType`](../hkworkoutactivitytype.md).

## See Also

### Deprecated methods
- [init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)](./init%28activitytype,locationtype%29.md)
  Returns a newly instantiated workout session.
- [init(configuration: HKWorkoutConfiguration) throws](./init%28configuration%29.md)
  Returns a newly instantiated workout session.
- [var locationType: HKWorkoutSessionLocationType](./locationtype.md)
  A value that indicates whether the workout session occurred indoors or outdoors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/activitytype)*