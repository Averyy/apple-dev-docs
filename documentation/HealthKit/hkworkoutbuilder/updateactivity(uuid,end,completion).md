# updateActivity(uuid:end:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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
func updateActivity(uuid UUID: UUID, end endDate: Date, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func updateActivity(uuid UUID: UUID, end endDate: Date) async throws
```

```objc
- (void) updateActivityWithUUID:(NSUUID *) UUID endDate:(NSDate *) endDate completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

Calling this method after calling [`finishWorkout(completion:)`](./finishworkout%28completion%29.md) fails with an error.

## Parameters

- `UUID`: The workout activity’s universally unique identifier (UUID).
- `endDate`: The end date and time for the workout activity.
- `completion`: A callback handler that the system calls after updating the workout activity. The system calls the callback handler on an anonymous background queue.

  The callback handler takes the following parameters:

  - **success**: Contains [`true`](../../Swift/true.md) if the builder successfully updates the activity.
  - **error**: If the `success` parameter is [`false`](../../Swift/false.md), this parameter contains information about the error; otherwise, it’s `nil`.

## See Also

### Managing workout activities
- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](./addworkoutactivity%28_,completion%29.md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,adding,completion%29.md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/updateactivity(uuid:end:completion:))*