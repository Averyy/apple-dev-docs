# metadata

**Framework**: HealthKit  
**Kind**: property

Metadata that describes the activity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

#### Discussion

The metadata dictionary contains extra information describing this activity. The dictionary’s keys are all [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. The values can be [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) objects. For a complete list of predefined metadata keys, see [`Metadata Keys`](metadata-keys.md).

Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the workout activity’s capabilities.

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
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutactivity/workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](hkworkoutactivity/workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/metadata)*