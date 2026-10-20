# pause(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Pauses the provided workout session.

**Availability**:
- macOS
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: Use HKWorkoutSession's pause method

## Declaration

```swift
func pause(_ workoutSession: HKWorkoutSession)
```

```objc
- (void) pauseWorkoutSession:(HKWorkoutSession *) workoutSession;
```

#### Discussion

This method pauses the provided session if it is currently running. The workout session’s state transitions to `HKWorkoutSessionStatePaused`, and the system generates an [`HKWorkoutEventType.pause`](../hkworkouteventtype/pause.md) event and passes it to the workout session delegate’s `workoutSession:didGenerateEvent:` method.

## Parameters

- `workoutSession`: The workout session to pause.

## See Also

### Managing workout sessions
- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](./workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, (any Error)?) -> Void)](./startwatchapp%28with,completion%29.md)
  Launches or wakes the companion watchOS app to create a new workout session.
- [func resumeWorkoutSession(HKWorkoutSession)](./resumeworkoutsession%28_%29.md)
  Resumes the provided workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/pause(_:))*