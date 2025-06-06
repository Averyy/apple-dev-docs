# HKWorkoutEventType

**Framework**: HealthKit  
**Kind**: enum

Constants that represent events occurring during a workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKWorkoutEventType
```

## Topics

### Events
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
- [HKWorkoutEventType.segment](hkworkouteventtype/segment.md)
  A constant indicating a period of time of interest during a workout.
- [HKWorkoutEventType.marker](hkworkouteventtype/marker.md)
  A constant indicating a point of interest during a workout session.
### Initializers
- [init?(rawValue: Int)](hkworkouteventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteventtype)*