# workoutEvents

**Framework**: HealthKit  
**Kind**: property

An array of events associated with the containing workout and occurring during the activity’s duration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var workoutEvents: [HKWorkoutEvent] { get }
```

#### Discussion

HealthKit sorts the events in ascending order. These events are a subset of the containing workout’s events, that take place between the activity’s [`startDate`](hkworkoutactivity/startdate.md) and [`endDate`](hkworkoutactivity/enddate.md). This includes any event that partially overlaps the activity. As a result, these events may appear in more than one activity.

## See Also

- [var uuid: UUID](hkworkoutactivity/uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](hkworkoutactivity/startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](hkworkoutactivity/enddate.md)
  The activity’s end date and time.
- [var duration: TimeInterval](hkworkoutactivity/duration.md)
  The activity’s duration, measured in seconds.
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkoutactivity/allstatistics.md)
  A dictionary that contains all the statistics for the activity.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutactivity/statistics(for:).md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](hkworkoutactivity/metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutactivity/workoutconfiguration.md)
  The configuration information for this part of the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/workoutevents)*