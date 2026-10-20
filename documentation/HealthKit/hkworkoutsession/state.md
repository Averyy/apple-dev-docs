# state

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout session’s current state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var state: HKWorkoutSessionState { get }
```

```objc
@property (readonly) HKWorkoutSessionState state;
```

#### Discussion

For a list of possible session states, see [`HKWorkoutSessionState`](../hkworkoutsessionstate.md).

## See Also

### Accessing session data
- [var endDate: Date?](./enddate.md)
  The ending time and date for this workout session.
- [var startDate: Date?](./startdate.md)
  The starting time and date for this workout session.
- [var type: HKWorkoutSessionType](./type.md)
  A value that indicates whether the session is a primary session or a mirrored session.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration object that describes this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/state)*