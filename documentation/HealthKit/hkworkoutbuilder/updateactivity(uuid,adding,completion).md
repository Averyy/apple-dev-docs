# updateActivity(uuid:adding:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Adds metadata to a workout activity that you’ve already added to the workout builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func updateActivity(uuid UUID: UUID, adding metadata: [String : Any], completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func updateActivity(uuid UUID: UUID, adding metadata: [String : Any]) async throws
```

```objc
- (void) updateActivityWithUUID:(NSUUID *) UUID addMedatata:(NSDictionary<NSString *,id> *) metadata completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

You can call this method multiple times to incrementally add metadata to the workout activity. The system merges the new metadata with any existing metadata using [`addEntries(from:)`](../../Foundation/nsmutabledictionary/addentries%28from%29.md). Calling this method after calling [`finishWorkout(completion:)`](./finishworkout%28completion%29.md) fails with an error.

## Parameters

- `UUID`: The workout activity’s universally unique identifier (UUID).
- `metadata`: A dictionary containing the metadata keys and values to add to the workout activity.
- `completion`: A callback handler that the system calls after updating the workout activity. The system calls the callback handler on an anonymous background queue.

  The callback handler takes the following parameters:

  - **success**: Contains [`true`](../../Swift/true.md) if the builder successfully updates the activity.
  - **error**: If the `success` parameter is [`false`](../../Swift/false.md), this parameter contains information about the error; otherwise, it’s `nil`.

## See Also

### Managing workout activities
- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](./addworkoutactivity%28_,completion%29.md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](./updateactivity%28uuid,end,completion%29.md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/updateactivity(uuid:adding:completion:))*