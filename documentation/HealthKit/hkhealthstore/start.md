# start(_:)

**Framework**: HealthKit  
**Kind**: method

Starts a workout session for the current app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func start(_ workoutSession: HKWorkoutSession)
```

#### Discussion

Workout sessions allow apps to run in the foreground. The current Foreground App appears when the user wakes the watch. Additionally, Apple Watch sets its sensors based on the workout activity and location types for more accurate measurements and better performance.

Apple Watch can only run one workout session at a time. If a second workout is started while your workout is running, your [`HKWorkoutSessionDelegate`](hkworkoutsessiondelegate.md) object receives an HKErrorAnotherWorkoutSession error, and your session ends.

This method returns immediately, however the work is performed asynchronously on an anonymous serial background queue. If successful, the session’s state transitions to [`HKWorkoutSessionState.running`](hkworkoutsessionstate/running.md), and the system calls the session delegate’s [`workoutSession(_:didChangeTo:from:date:)`](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md) method.

## Parameters

- `workoutSession`: The workout session to start. You cannot restart a workout session that has stopped. If you pass in a session that is running or has stopped, the system returns an   exception.

## See Also

- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/add(_:to:completion:).md)
  Associates the provided samples with the specified workout.
- [func end(HKWorkoutSession)](hkhealthstore/end(_:).md)
  Ends a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/start(_:))*