# workoutActivities

**Framework**: HealthKit  
**Kind**: property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var workoutActivities: [HKWorkoutActivity] { get }
```

## See Also

- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/addworkoutactivity(_:completion:).md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:adding:completion:).md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:end:completion:).md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/workoutactivities)*