# HKWorkoutEventType.pauseOrResumeRequest

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

A constant indicating that the user has requested a pause or resume.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case pauseOrResumeRequest
```

```c
HKWorkoutEventTypePauseOrResumeRequest
```

## Discussion

During a workout session, the user can request a pause or resume by pressing both watch buttons. When you receive this event, pause or resume your app’s current workout session.

## See Also

### Events
- [HKWorkoutEventType.pause](./pause.md)
  A constant indicating that the workout has paused.
- [HKWorkoutEventType.resume](./resume.md)
  A constant indicating that the workout has resumed.
- [HKWorkoutEventType.motionPaused](./motionpaused.md)
  A constant indicating that the system has automatically paused a workout session.
- [HKWorkoutEventType.motionResumed](./motionresumed.md)
  A constant indicating that the system has automatically resumed a workout session.
- [HKWorkoutEventType.lap](./lap.md)
  A constant indicating a lap.
- [HKWorkoutEventType.segment](./segment.md)
  A constant indicating a period of time of interest during a workout.
- [HKWorkoutEventType.marker](./marker.md)
  A constant indicating a point of interest during a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/pauseorresumerequest)*