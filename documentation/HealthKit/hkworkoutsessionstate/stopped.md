# HKWorkoutSessionState.stopped

**Framework**: HealthKit  
**Kind**: case

The session has stopped.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case stopped
```

#### Discussion

As soon as the session stops, the watch’s sensors return to normal, and it no longer generates workout data; however, the app can continue to run in the background, even after the user lowers their wrist.

You can’t restart or reuse the workout session.

## See Also

- [HKWorkoutSessionState.notStarted](hkworkoutsessionstate/notstarted.md)
  The workout session has not started.
- [HKWorkoutSessionState.prepared](hkworkoutsessionstate/prepared.md)
  The session is ready but not yet running.
- [HKWorkoutSessionState.running](hkworkoutsessionstate/running.md)
  The workout session is running.
- [HKWorkoutSessionState.paused](hkworkoutsessionstate/paused.md)
  The workout session has paused.
- [HKWorkoutSessionState.ended](hkworkoutsessionstate/ended.md)
  The workout session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate/stopped)*