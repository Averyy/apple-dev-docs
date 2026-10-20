# statistics(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the activity’s statistics for the provided quantity type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func statistics(for quantityType: HKQuantityType) -> HKStatistics?
```

```objc
- (HKStatistics *) statisticsForType:(HKQuantityType *) quantityType;
```

#### Discussion

HealthKit calculates an [`HKStatistics`](../hkstatistics.md) object based on the [`HKQuantitySample`](../hkquantitysample.md) objects that meet the following requirements:

- Match the specified [`HKQuantityType`](../hkquantitytype.md).
- Are associated with the containing workout.
- Fall within the activity’s time frame.

Furthermore, if a quantity sample extends beyond the activity’s time frame, HealthKit interpolates a quantity value to represent the portion within the time frame, and uses that value instead.

If there are no matching quantity values, this method returns `nil`.

## Parameters

- `quantityType`: The type of [`HKQuantitySample`](../hkquantitysample.md) objects used to calculate the statistics.

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
- [var metadata: [String : Any]?](./metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](./workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/statistics(for:))*