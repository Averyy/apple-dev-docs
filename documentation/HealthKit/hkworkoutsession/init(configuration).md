# init(configuration:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Returns a newly instantiated workout session.

**Availability**:
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: Use [`init(healthStore:configuration:)`](./init%28healthstore,configuration%29.md) instead.

## Declaration

```swift
init(configuration workoutConfiguration: HKWorkoutConfiguration) throws
```

```objc
- (instancetype) initWithConfiguration:(HKWorkoutConfiguration *) workoutConfiguration error:(NSError **) error;
```

#### Return Value

A newly initialized workout session object, or `nil` if an error occurred.

#### Discussion

HealthKit uses the session’s configuration data to fine tune Apple Watch’s sensors for the selected activity. All workout sessions generate higher-frequency heart rate samples; however, an outdoor cycling activity generates more accurate location data, while an indoor cycling activity does not.

## Parameters

- `workoutConfiguration`: A workout configuration object containing the configuration data for this workout session.

## See Also

### Deprecated methods
- [init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)](./init%28activitytype,locationtype%29.md)
  Returns a newly instantiated workout session.
- [var activityType: HKWorkoutActivityType](./activitytype.md)
  The workout activity performed during this session.
- [var locationType: HKWorkoutSessionLocationType](./locationtype.md)
  A value that indicates whether the workout session occurred indoors or outdoors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/init(configuration:))*