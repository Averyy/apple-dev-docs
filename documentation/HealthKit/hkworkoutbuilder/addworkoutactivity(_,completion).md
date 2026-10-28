# addWorkoutActivity(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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
func addWorkoutActivity(_ workoutActivity: HKWorkoutActivity, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func addWorkoutActivity(_ workoutActivity: HKWorkoutActivity) async throws
```

```objc
- (void) addWorkoutActivity:(HKWorkoutActivity *) workoutActivity completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

You can call this method repeatedly to incrementally add activities to the builder. Calling this method after calling [`finishWorkout(completion:)`](./finishworkout%28completion%29.md) fails with an error.

If you add an [`HKWorkoutActivity`](../hkworkoutactivity.md) object that doesn’t have an [`endDate`](../hkworkoutactivity/enddate.md), you can set the end date by calling [`updateActivity(uuid:end:completion:)`](./updateactivity%28uuid,end,completion%29.md).

## Parameters

- `workoutActivity`: The workout activity to add.
- `completion`: A callback handler that the system calls after adding the workout activity. The system calls the callback handler on an anonymous background queue.

  The callback handler takes the following parameters:

  - **success**: Contains [`true`](../../Swift/true.md) if the builder successfully added the activity.
  - **error**: If the `success` parameter is [`false`](../../Swift/false.md), this parameter contains information about the error; otherwise, it’s `nil`.

## See Also

### Managing workout activities
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,adding,completion%29.md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,end,completion%29.md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/addworkoutactivity(_:completion:))*