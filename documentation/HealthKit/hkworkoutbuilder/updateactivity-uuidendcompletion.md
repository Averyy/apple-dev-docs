# updateActivity(uuid:end:completion:)

**Framework**: HealthKit  
**Kind**: method

Sets the end date for a workout activity that you’ve already added to the workout builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func updateActivity(uuid UUID: UUID, end endDate: Date) async throws
```

#### Discussion

Calling this method after calling [`finishWorkout(completion:)`](hkworkoutbuilder/finishworkout(completion:).md) fails with an error.

## Parameters

- `UUID`: The workout activity’s universally unique identifier (UUID).
- `endDate`: The end date and time for the workout activity.
- `completion`: The callback handler takes the following parameters:

## See Also

- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/addworkoutactivity(_:completion:).md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:adding:completion:).md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](hkworkoutbuilder/workoutactivities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/updateactivity(uuid:end:completion:))*