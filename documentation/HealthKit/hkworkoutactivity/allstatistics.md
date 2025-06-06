# allStatistics

**Framework**: HealthKit  
**Kind**: property

A dictionary that contains all the statistics for the activity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var allStatistics: [HKQuantityType : HKStatistics] { get }
```

#### Discussion

HealthKit calculates an [`HKStatistics`](hkstatistics.md) object for each [`HKQuantityType`](hkquantitytype.md), based on the [`HKQuantitySample`](hkquantitysample.md) objects associated with the containing workout, and falling within the workout activity’s time frame.

Furthermore, if a quantity sample extends beyond the activity’s time frame, HealthKit interpolates a quantity value to represent the portion within the time frame, and uses that value instead.

## See Also

- [var uuid: UUID](hkworkoutactivity/uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](hkworkoutactivity/startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](hkworkoutactivity/enddate.md)
  The activity’s end date and time.
- [var duration: TimeInterval](hkworkoutactivity/duration.md)
  The activity’s duration, measured in seconds.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutactivity/statistics(for:).md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](hkworkoutactivity/metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutactivity/workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](hkworkoutactivity/workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/allstatistics)*