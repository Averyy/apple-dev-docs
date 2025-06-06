# init(workoutConfiguration:start:end:metadata:)

**Framework**: HealthKit  
**Kind**: init

Creates a workout activity using the provided configuration, start date, end date, and metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(workoutConfiguration: HKWorkoutConfiguration, start startDate: Date, end endDate: Date?, metadata: [String : Any]?)
```

#### Discussion

## Parameters

- `workoutConfiguration`: The configuration information for this part of the workout. For   workouts, the activity’s configuration must use the  ,  , or   activity types. For interval training, the activity’s configuration must use the same activity type as the containing workout.
- `startDate`: The activity’s start date and time.
- `endDate`: The activity’s end date and time. Set this value to   if the activity is still in progress. When set to a non-  value, the end date must be equal to or later than its start date. A workout can’t have overlapping activities.
- `metadata`: Metadata that provides additional information about the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/init(workoutconfiguration:start:end:metadata:))*