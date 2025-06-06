# resumeWorkoutSession(_:)

**Framework**: HealthKit  
**Kind**: method

Resumes the provided workout session.

**Availability**:
- macOS ?+
- watchOS 3.0+

## Declaration

```swift
func resumeWorkoutSession(_ workoutSession: HKWorkoutSession)
```

#### Discussion

This method resumes the provided session if it is currently paused. The workout session’s state transitions to [`HKWorkoutSessionState.running`](hkworkoutsessionstate/running.md), and the system generates an [`HKWorkoutEventType.resume`](hkworkouteventtype/resume.md) event and passes it to the workout session delegate’s `workoutSession:didGenerateEvent:` method.

## Parameters

- `workoutSession`: The workout session to resume.

## See Also

- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](hkhealthstore/workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/startwatchapp(with:completion:).md)
  Launches or wakes the companion watchOS app to create a new workout session.
- [func pause(HKWorkoutSession)](hkhealthstore/pause(_:).md)
  Pauses the provided workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/resumeworkoutsession(_:))*