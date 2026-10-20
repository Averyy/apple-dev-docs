# HKWorkoutEventType.segment

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

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

```c
HKWorkoutEventTypeSegment
```

#### Discussion

Use segments to highlight important time periods during a workout. For example, you could use different segments to mark when a runner is going up or downhill. Similarly, when swimming, you can use segments to group consecutive laps with the same style of stroke.

Unlike laps, segments can freely overlap.

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
- [HKWorkoutEventType.pauseOrResumeRequest](./pauseorresumerequest.md)
  A constant indicating that the user has requested a pause or resume.
- [HKWorkoutEventType.lap](./lap.md)
  A constant indicating a lap.
- [HKWorkoutEventType.marker](./marker.md)
  A constant indicating a point of interest during a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/segment)*