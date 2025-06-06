# HKWorkoutEventType.lap

**Framework**: HealthKit  
**Kind**: case

A constant indicating a lap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case lap
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

#### Discussion

Lap events partition a workout into segments of equal distance (for example, laps around a track or laps in a pool). The lap’s [`dateInterval`](hkworkoutevent/dateinterval.md) property should mark the start and end of the lap. Lap events can’t overlap.

When you receive lap events from the HealthKit store, examine the event’s [`dateInterval`](hkworkoutevent/dateinterval.md) property to interpret the lap correctly:

 Older lap events (created before iOS 11 and watchOS 4) have a zero-duration date interval that marks the end of the lap. Each lap is assumed to start when the previous lap ends, and laps fill the entire workout completely.****

 Newer lap events use the date interval to mark the start and the duration of the lap. These events have a nonzero duration, and they do not need to fill the workout; however, you should ideally mark any rest periods between laps using [`HKWorkoutEventType.pause`](hkworkouteventtype/pause.md) and [`HKWorkoutEventType.resume`](hkworkouteventtype/resume.md) events.

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
- [HKWorkoutEventType.segment](hkworkouteventtype/segment.md)
  A constant indicating a period of time of interest during a workout.
- [HKWorkoutEventType.marker](hkworkouteventtype/marker.md)
  A constant indicating a point of interest during a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/lap)*