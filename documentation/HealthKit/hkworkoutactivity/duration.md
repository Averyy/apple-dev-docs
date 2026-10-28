# duration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (assign, readonly) NSTimeInterval duration;
```

## Discussion

HealthKit calculates the [`duration`](./duration.md) as the elapsed time between the activity’s [`startDate`](./startdate.md) and [`endDate`](./enddate.md), ignoring any pause periods. If an activity is currently in progress, it has a `nil`-valued [`endDate`](./enddate.md). In this case, HealthKit calculates the duration as the time between the [`startDate`](./startdate.md) and the current time, ignoring any pause periods.

## See Also

### Accessing workout data
- [var uuid: UUID](./uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](./startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](./enddate.md)
  The activity’s end date and time.
- [var allStatistics: [HKQuantityType : HKStatistics]](./allstatistics.md)
  A dictionary that contains all the statistics for the activity.
- [func statistics(for: HKQuantityType) -> HKStatistics?](./statistics%28for%29.md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](./metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](./workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/duration)*