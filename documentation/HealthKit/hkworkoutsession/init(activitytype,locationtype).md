# init(activityType:locationType:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Returns a newly instantiated workout session.

**Availability**:
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`init(healthStore:configuration:)`](./init%28healthstore,configuration%29.md) instead.

## Declaration

```swift
init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)
```

```objc
- (instancetype) initWithActivityType:(HKWorkoutActivityType) activityType locationType:(HKWorkoutSessionLocationType) locationType;
```

## Return Value

A newly initialized workout session object for the specified activity type and location.

## Discussion

HealthKit uses the session’s workout activity and location type to fine tune Apple Watch’s sensors for the selected activity. All workout sessions generate higher-frequency heart rate samples; however, an outdoor cycling activity generates more accurate location data, while an indoor cycling activity does not.

## Parameters

- `activityType`: The type of activity being performed in the workout. For a list of possible activities, see [`HKWorkoutActivityType`](../hkworkoutactivitytype.md).
- `locationType`: A value indicating whether the workout was performed indoors or outdoors. For a list of possible location values, see [`HKWorkoutSessionLocationType`](../hkworkoutsessionlocationtype.md).

## See Also

### Deprecated methods
- [init(configuration: HKWorkoutConfiguration) throws](./init%28configuration%29.md)
  Returns a newly instantiated workout session.
- [var activityType: HKWorkoutActivityType](./activitytype.md)
  The workout activity performed during this session.
- [var locationType: HKWorkoutSessionLocationType](./locationtype.md)
  A value that indicates whether the workout session occurred indoors or outdoors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/init(activitytype:locationtype:))*