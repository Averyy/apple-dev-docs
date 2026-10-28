# locationType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout session’s location.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var locationType: HKWorkoutSessionLocationType { get set }
```

```objc
@property (assign) HKWorkoutSessionLocationType locationType;
```

## Discussion

For a list of possible values, see [`HKWorkoutSessionLocationType`](../hkworkoutsessionlocationtype.md).

## See Also

### Session settings
- [var activityType: HKWorkoutActivityType](./activitytype.md)
  The workout session’s activity type.
- [enum HKWorkoutSessionLocationType](../hkworkoutsessionlocationtype.md)
  A constant indicating whether the workout session takes place indoors or outdoors.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](./swimminglocationtype.md)
  The workout session’s swimming location.
- [enum HKWorkoutSwimmingLocationType](../hkworkoutswimminglocationtype.md)
  The possible locations for swimming.
- [var lapLength: HKQuantity?](./laplength.md)
  The length of the lap for a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/locationtype)*