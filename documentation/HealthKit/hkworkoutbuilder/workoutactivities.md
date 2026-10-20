# workoutActivities

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<HKWorkoutActivity *> * workoutActivities;
```

## See Also

### Managing workout activities
- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](./addworkoutactivity%28_,completion%29.md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,adding,completion%29.md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,end,completion%29.md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/workoutactivities)*