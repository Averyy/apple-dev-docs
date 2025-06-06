# addWorkoutActivity(_:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds a workout activity to the workout builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func addWorkoutActivity(_ workoutActivity: HKWorkoutActivity) async throws
```

#### Discussion

You can call this method repeatedly to incrementally add activities to the builder. Calling this method after calling [`finishWorkout(completion:)`](hkworkoutbuilder/finishworkout(completion:).md) fails with an error.

If you add an [`HKWorkoutActivity`](hkworkoutactivity.md) object that doesn’t have an [`endDate`](hkworkoutactivity/enddate.md), you can set the end date by calling [`updateActivity(uuid:end:completion:)`](hkworkoutbuilder/updateactivity(uuid:end:completion:).md).

## Parameters

- `workoutActivity`: The workout activity to add.
- `completion`: The callback handler takes the following parameters:

## See Also

- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:adding:completion:).md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:end:completion:).md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](hkworkoutbuilder/workoutactivities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/addworkoutactivity(_:completion:))*