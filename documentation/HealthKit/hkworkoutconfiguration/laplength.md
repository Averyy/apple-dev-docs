# lapLength

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The length of the lap for a workout session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var lapLength: HKQuantity? { get set }
```

```objc
@property (copy, nullable) HKQuantity * lapLength;
```

## See Also

### Session settings
- [var activityType: HKWorkoutActivityType](./activitytype.md)
  The workout session’s activity type.
- [var locationType: HKWorkoutSessionLocationType](./locationtype.md)
  The workout session’s location.
- [enum HKWorkoutSessionLocationType](../hkworkoutsessionlocationtype.md)
  A constant indicating whether the workout session takes place indoors or outdoors.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](./swimminglocationtype.md)
  The workout session’s swimming location.
- [enum HKWorkoutSwimmingLocationType](../hkworkoutswimminglocationtype.md)
  The possible locations for swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/laplength)*