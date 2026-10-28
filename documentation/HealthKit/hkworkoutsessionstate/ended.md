# HKWorkoutSessionState.ended

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

The workout session has ended.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case ended
```

```c
HKWorkoutSessionStateEnded
```

## Discussion

The watch can no longer run in the background. Its sensors return to normal, and it no longer generates workout data. You can’t restart or reuse the workout session.

## See Also

### Related Documentation
- [func end()](../hkworkoutsession/end%28%29.md)
  Ends the workout session.
### Session states
- [HKWorkoutSessionState.notStarted](./notstarted.md)
  The workout session has not started.
- [HKWorkoutSessionState.prepared](./prepared.md)
  The session is ready but not yet running.
- [HKWorkoutSessionState.running](./running.md)
  The workout session is running.
- [HKWorkoutSessionState.paused](./paused.md)
  The workout session has paused.
- [HKWorkoutSessionState.stopped](./stopped.md)
  The session has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate/ended)*