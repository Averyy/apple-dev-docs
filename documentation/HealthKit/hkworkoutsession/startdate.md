# startDate

**Framework**: HealthKit  
**Kind**: property

The starting time and date for this workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var startDate: Date? { get }
```

#### Discussion

This property is set to `nil` when the workout session is initialized. The system assigns a start date when the session’s state changes to [`HKWorkoutSessionState.running`](hkworkoutsessionstate/running.md).

## See Also

- [var endDate: Date?](hkworkoutsession/enddate.md)
  The ending time and date for this workout session.
- [var state: HKWorkoutSessionState](hkworkoutsession/state.md)
  The workout session’s current state.
- [var type: HKWorkoutSessionType](hkworkoutsession/type.md)
  A value that indicates whether the session is a primary session or a mirrored session.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutsession/workoutconfiguration.md)
  The configuration object that describes this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/startdate)*