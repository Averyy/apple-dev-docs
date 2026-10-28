# metadata

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,id> * metadata;
```

## Discussion

The metadata dictionary contains extra information describing this activity. The dictionary’s keys are all [`NSString`](../../Foundation/nsstring.md) objects. The values can be [`NSString`](../../Foundation/nsstring.md) objects, [`NSNumber`](../../Foundation/nsnumber.md) objects or [`NSDate`](../../Foundation/nsdate.md) objects. For a complete list of predefined metadata keys, see [Metadata Keys](../metadata-keys.md).

Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the workout activity’s capabilities.

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
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](./workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/metadata)*