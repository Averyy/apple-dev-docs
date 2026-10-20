# HKWorkoutSessionState.prepared

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

The session is ready but not yet running.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case prepared
```

```c
HKWorkoutSessionStatePrepared
```

#### Discussion

The app can continue to run in the background, even after the user lowers their wrist, but it doesn’t yet generate workout data.

## See Also

### Related Documentation
- [func prepare()](../hkworkoutsession/prepare%28%29.md)
  Prepares the workout session.
### Session states
- [HKWorkoutSessionState.notStarted](./notstarted.md)
  The workout session has not started.
- [HKWorkoutSessionState.running](./running.md)
  The workout session is running.
- [HKWorkoutSessionState.paused](./paused.md)
  The workout session has paused.
- [HKWorkoutSessionState.stopped](./stopped.md)
  The session has stopped.
- [HKWorkoutSessionState.ended](./ended.md)
  The workout session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate/prepared)*