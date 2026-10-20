# endDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The ending time and date for this workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var endDate: Date? { get }
```

```objc
@property (readonly, nullable) NSDate * endDate;
```

#### Discussion

This property is set to `nil` when the workout session is initialized. The system assigns an end date when the session’s state changes to [`HKWorkoutSessionState.ended`](../hkworkoutsessionstate/ended.md).

## See Also

### Accessing session data
- [var startDate: Date?](./startdate.md)
  The starting time and date for this workout session.
- [var state: HKWorkoutSessionState](./state.md)
  The workout session’s current state.
- [var type: HKWorkoutSessionType](./type.md)
  A value that indicates whether the session is a primary session or a mirrored session.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration object that describes this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/enddate)*