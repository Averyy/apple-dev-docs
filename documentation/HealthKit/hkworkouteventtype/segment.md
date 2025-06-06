# HKWorkoutEventType.segment

**Framework**: HealthKit  
**Kind**: case

A constant indicating a period of time of interest during a workout.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case segment
```

#### Discussion

Use segments to highlight important time periods during a workout. For example, you could use different segments to mark when a runner is going up or downhill. Similarly, when swimming, you can use segments to group consecutive laps with the same style of stroke.

Unlike laps, segments can freely overlap.

## See Also

- [HKWorkoutEventType.pause](hkworkouteventtype/pause.md)
  A constant indicating that the workout has paused.
- [HKWorkoutEventType.resume](hkworkouteventtype/resume.md)
  A constant indicating that the workout has resumed.
- [HKWorkoutEventType.motionPaused](hkworkouteventtype/motionpaused.md)
  A constant indicating that the system has automatically paused a workout session.
- [HKWorkoutEventType.motionResumed](hkworkouteventtype/motionresumed.md)
  A constant indicating that the system has automatically resumed a workout session.
- [HKWorkoutEventType.pauseOrResumeRequest](hkworkouteventtype/pauseorresumerequest.md)
  A constant indicating that the user has requested a pause or resume.
- [HKWorkoutEventType.lap](hkworkouteventtype/lap.md)
  A constant indicating a lap.
- [HKWorkoutEventType.marker](hkworkouteventtype/marker.md)
  A constant indicating a point of interest during a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/segment)*