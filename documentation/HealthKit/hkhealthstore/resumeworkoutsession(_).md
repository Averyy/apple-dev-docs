# resumeWorkoutSession(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Resumes the provided workout session.

**Availability**:
- macOS
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: Use HKWorkoutSession's resume method

## Declaration

```swift
func resumeWorkoutSession(_ workoutSession: HKWorkoutSession)
```

```objc
- (void) resumeWorkoutSession:(HKWorkoutSession *) workoutSession;
```

#### Discussion

This method resumes the provided session if it is currently paused. The workout session’s state transitions to [`HKWorkoutSessionState.running`](../hkworkoutsessionstate/running.md), and the system generates an [`HKWorkoutEventType.resume`](../hkworkouteventtype/resume.md) event and passes it to the workout session delegate’s `workoutSession:didGenerateEvent:` method.

## Parameters

- `workoutSession`: The workout session to resume.

## See Also

### Managing workout sessions
- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](./workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, (any Error)?) -> Void)](./startwatchapp%28with,completion%29.md)
  Launches or wakes the companion watchOS app to create a new workout session.
- [func pause(HKWorkoutSession)](./pause%28_%29.md)
  Pauses the provided workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/resumeworkoutsession(_:))*