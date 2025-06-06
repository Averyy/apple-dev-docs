# add(_:to:completion:)

**Framework**: HealthKit  
**Kind**: method

Associates the provided samples with the specified workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addSamples(_ samples: [HKSample], to workout: HKWorkout) async throws
```

## Mentions

- [Adding samples to a workout](adding-samples-to-a-workout.md)

#### Discussion

This method operates asynchronously. As soon as the add-samples operation is finished, this method calls the completion block on a background queue. You must save the workout to the HealthKit store before you can add any samples to it. You can save the samples before calling this method, but doing so is not required. This method automatically saves any unsaved samples when it successfully adds them to the workout.

To query for all the samples associated with a workout, add the workout to the query’s predicate. For example, the query’s [`predicateForObjects(from:)`](hkquery/predicateforobjects(from:)-5irg9.md) method creates a predicate object that matches only samples associated with the provided workout.

For more information on workouts and associated samples, see [`HKWorkout`](hkworkout.md).

## Parameters

- `samples`: An array containing   or   objects.
- `workout`: The workout object you are adding samples to.
- `completion`: A block that this method calls as soon as the add-samples operation is complete. This block is passed the following parameters:

## See Also

- [func start(HKWorkoutSession)](hkhealthstore/start(_:).md)
  Starts a workout session for the current app.
- [func end(HKWorkoutSession)](hkhealthstore/end(_:).md)
  Ends a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/add(_:to:completion:))*