# pause(_:)

**Framework**: HealthKit  
**Kind**: method

Pauses the provided workout session.

**Availability**:
- macOS ?+
- watchOS 3.0+

## Declaration

```swift
func pause(_ workoutSession: HKWorkoutSession)
```

#### Discussion

This method pauses the provided session if it is currently running. The workout session’s state transitions to `HKWorkoutSessionStatePaused`, and the system generates an [`HKWorkoutEventType.pause`](hkworkouteventtype/pause.md) event and passes it to the workout session delegate’s `workoutSession:didGenerateEvent:` method.

## Parameters

- `workoutSession`: The workout session to pause.

## See Also

- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](hkhealthstore/workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, (any Error)?) -> Void)](hkhealthstore/startwatchapp(with:completion:).md)
  Launches or wakes the companion watchOS app to create a new workout session.
- [func resumeWorkoutSession(HKWorkoutSession)](hkhealthstore/resumeworkoutsession(_:).md)
  Resumes the provided workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/pause(_:))*