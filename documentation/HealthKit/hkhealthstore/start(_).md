# start(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Starts a workout session for the current app.

**Availability**:
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use HKWorkoutSession's start method

## Declaration

```swift
func start(_ workoutSession: HKWorkoutSession)
```

```objc
- (void) startWorkoutSession:(HKWorkoutSession *) workoutSession;
```

#### Discussion

Workout sessions allow apps to run in the foreground. The current Foreground App appears when the user wakes the watch. Additionally, Apple Watch sets its sensors based on the workout activity and location types for more accurate measurements and better performance.

Apple Watch can only run one workout session at a time. If a second workout is started while your workout is running, your [`HKWorkoutSessionDelegate`](../hkworkoutsessiondelegate.md) object receives an HKErrorAnotherWorkoutSession error, and your session ends.

This method returns immediately, however the work is performed asynchronously on an anonymous serial background queue. If successful, the session’s state transitions to [`HKWorkoutSessionState.running`](../hkworkoutsessionstate/running.md), and the system calls the session delegate’s [`workoutSession(_:didChangeTo:from:date:)`](../hkworkoutsessiondelegate/workoutsession%28_,didchangeto,from,date%29.md) method.

## Parameters

- `workoutSession`: The workout session to start. You cannot restart a workout session that has stopped. If you pass in a session that is running or has stopped, the system returns an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Deprecated symbols
- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](./add%28_,to,completion%29.md)
  Associates the provided samples with the specified workout.
- [func end(HKWorkoutSession)](./end%28_%29.md)
  Ends a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/start(_:))*