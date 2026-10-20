# add(_:to:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Associates the provided samples with the specified workout.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 10.0

> **Deprecated**: Use HKWorkoutBuilder

## Declaration

```swift
func add(_ samples: [HKSample], to workout: HKWorkout, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func addSamples(_ samples: [HKSample], to workout: HKWorkout) async throws
```

```objc
- (void) addSamples:(NSArray<HKSample *> *) samples toWorkout:(HKWorkout *) workout completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Mentions

- [Adding samples to a workout](../adding-samples-to-a-workout.md)

#### Discussion

This method operates asynchronously. As soon as the add-samples operation is finished, this method calls the completion block on a background queue. You must save the workout to the HealthKit store before you can add any samples to it. You can save the samples before calling this method, but doing so is not required. This method automatically saves any unsaved samples when it successfully adds them to the workout.

To query for all the samples associated with a workout, add the workout to the query’s predicate. For example, the query’s [`predicateForObjects(from:)`](../hkquery/predicateforobjects%28from%29-5irg9.md) method creates a predicate object that matches only samples associated with the provided workout.

For more information on workouts and associated samples, see [`HKWorkout`](../hkworkout.md).

## Parameters

- `samples`: An array containing [`HKCategorySample`](../hkcategorysample.md) or [`HKQuantitySample`](../hkquantitysample.md) objects.
- `workout`: The workout object you are adding samples to.
- `completion`: A block that this method calls as soon as the add-samples operation is complete. This block is passed the following parameters:

  - **success**: A Boolean value. This parameter contains [`true`](../../Swift/true.md) if the samples were successfully added to workout; otherwise, [`false`](../../Swift/false.md).
  - **error**: An error object. If an error occurred, this object contains information about the error; otherwise, it is set to `nil`.

## See Also

### Deprecated symbols
- [func start(HKWorkoutSession)](./start%28_%29.md)
  Starts a workout session for the current app.
- [func end(HKWorkoutSession)](./end%28_%29.md)
  Ends a workout session for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/add(_:to:completion:))*