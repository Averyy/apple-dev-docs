# workoutEvents

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<HKWorkoutEvent *> * workoutEvents;
```

## Discussion

HealthKit sorts the events in ascending order. These events are a subset of the containing workout’s events, that take place between the activity’s [`startDate`](./startdate.md) and [`endDate`](./enddate.md). This includes any event that partially overlaps the activity. As a result, these events may appear in more than one activity.

## See Also

### Accessing workout data
- [var uuid: UUID](./uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](./startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](./enddate.md)
  The activity’s end date and time.
- [var duration: TimeInterval](./duration.md)
  The activity’s duration, measured in seconds.
- [var allStatistics: [HKQuantityType : HKStatistics]](./allstatistics.md)
  A dictionary that contains all the statistics for the activity.
- [func statistics(for: HKQuantityType) -> HKStatistics?](./statistics%28for%29.md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](./metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for this part of the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/workoutevents)*