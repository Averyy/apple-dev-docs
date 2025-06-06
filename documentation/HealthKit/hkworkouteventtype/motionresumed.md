# HKWorkoutEventType.motionResumed

**Framework**: HealthKit  
**Kind**: case

A constant indicating that the system has automatically resumed a workout session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case motionResumed
```

## Mentions

- [Receiving Downhill Skiing and Snowboarding Data](receiving-downhill-skiing-and-snowboarding-data.md)

#### Discussion

If the system has automatically paused a running workout session, it also generates a motion resumed event when the user starts moving again.

## See Also

- [HKWorkoutEventType.pause](hkworkouteventtype/pause.md)
  A constant indicating that the workout has paused.
- [HKWorkoutEventType.resume](hkworkouteventtype/resume.md)
  A constant indicating that the workout has resumed.
- [HKWorkoutEventType.motionPaused](hkworkouteventtype/motionpaused.md)
  A constant indicating that the system has automatically paused a workout session.
- [HKWorkoutEventType.pauseOrResumeRequest](hkworkouteventtype/pauseorresumerequest.md)
  A constant indicating that the user has requested a pause or resume.
- [HKWorkoutEventType.lap](hkworkouteventtype/lap.md)
  A constant indicating a lap.
- [HKWorkoutEventType.segment](hkworkouteventtype/segment.md)
  A constant indicating a period of time of interest during a workout.
- [HKWorkoutEventType.marker](hkworkouteventtype/marker.md)
  A constant indicating a point of interest during a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/motionresumed)*