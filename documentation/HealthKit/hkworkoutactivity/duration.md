# duration

**Framework**: HealthKit  
**Kind**: property

The activity’s duration, measured in seconds.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

HealthKit calculates the [`duration`](hkworkoutactivity/duration.md) as the elapsed time between the activity’s [`startDate`](hkworkoutactivity/startdate.md) and [`endDate`](hkworkoutactivity/enddate.md), ignoring any pause periods. If an activity is currently in progress, it has a `nil`-valued [`endDate`](hkworkoutactivity/enddate.md). In this case, HealthKit calculates the duration as the time between the [`startDate`](hkworkoutactivity/startdate.md) and the current time, ignoring any pause periods.

## See Also

- [var uuid: UUID](hkworkoutactivity/uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](hkworkoutactivity/startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](hkworkoutactivity/enddate.md)
  The activity’s end date and time.
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkoutactivity/allstatistics.md)
  A dictionary that contains all the statistics for the activity.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutactivity/statistics(for:).md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](hkworkoutactivity/metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutactivity/workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](hkworkoutactivity/workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/duration)*