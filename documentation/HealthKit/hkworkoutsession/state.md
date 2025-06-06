# state

**Framework**: HealthKit  
**Kind**: property

The workout session’s current state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var state: HKWorkoutSessionState { get }
```

#### Discussion

For a list of possible session states, see [`HKWorkoutSessionState`](hkworkoutsessionstate.md).

## See Also

- [var endDate: Date?](hkworkoutsession/enddate.md)
  The ending time and date for this workout session.
- [var startDate: Date?](hkworkoutsession/startdate.md)
  The starting time and date for this workout session.
- [var type: HKWorkoutSessionType](hkworkoutsession/type.md)
  A value that indicates whether the session is a primary session or a mirrored session.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutsession/workoutconfiguration.md)
  The configuration object that describes this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/state)*