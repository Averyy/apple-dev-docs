# activityType

**Framework**: HealthKit  
**Kind**: property

The workout session’s activity type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var activityType: HKWorkoutActivityType { get set }
```

#### Discussion

For a list of possible values, see [`HKWorkoutActivityType`](hkworkoutactivitytype.md).

## See Also

- [var locationType: HKWorkoutSessionLocationType](hkworkoutconfiguration/locationtype.md)
  The workout session’s location.
- [enum HKWorkoutSessionLocationType](hkworkoutsessionlocationtype.md)
  A constant indicating whether the workout session takes place indoors or outdoors.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](hkworkoutconfiguration/swimminglocationtype.md)
  The workout session’s swimming location.
- [enum HKWorkoutSwimmingLocationType](hkworkoutswimminglocationtype.md)
  The possible locations for swimming.
- [var lapLength: HKQuantity?](hkworkoutconfiguration/laplength.md)
  The length of the lap for a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/activitytype)*