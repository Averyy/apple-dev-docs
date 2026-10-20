# end(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Ends a workout session for the current app.

**Availability**:
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use HKWorkoutSession's end method

## Declaration

```swift
func end(_ workoutSession: HKWorkoutSession)
```

```objc
- (void) endWorkoutSession:(HKWorkoutSession *) workoutSession;
```

#### Discussion

This method returns immediately; however, the work is performed asynchronously on an anonymous serial background queue. If successful, the session’s state transitions to [`HKWorkoutSessionState.ended`](../hkworkoutsessionstate/ended.md), and the system calls the session delegate’s [`workoutSession(_:didChangeTo:from:date:)`](../hkworkoutsessiondelegate/workoutsession%28_,didchangeto,from,date%29.md) method.

## Parameters

- `workoutSession`: A currently running workout session. If the session is not running,  the system returns an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Deprecated symbols
- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](./add%28_,to,completion%29.md)
  Associates the provided samples with the specified workout.
- [func start(HKWorkoutSession)](./start%28_%29.md)
  Starts a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/end(_:))*