# end(_:)

**Framework**: HealthKit  
**Kind**: method

Ends a workout session for the current app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func end(_ workoutSession: HKWorkoutSession)
```

#### Discussion

This method returns immediately; however, the work is performed asynchronously on an anonymous serial background queue. If successful, the session’s state transitions to [`HKWorkoutSessionState.ended`](hkworkoutsessionstate/ended.md), and the system calls the session delegate’s [`workoutSession(_:didChangeTo:from:date:)`](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md) method.

## Parameters

- `workoutSession`: A currently running workout session. If the session is not running,  the system returns an   exception.

## See Also

- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/add(_:to:completion:).md)
  Associates the provided samples with the specified workout.
- [func start(HKWorkoutSession)](hkhealthstore/start(_:).md)
  Starts a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/end(_:))*