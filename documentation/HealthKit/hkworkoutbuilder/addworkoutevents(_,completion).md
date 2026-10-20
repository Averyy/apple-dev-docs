# addWorkoutEvents(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Adds a workout event to the builder.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func addWorkoutEvents(_ workoutEvents: [HKWorkoutEvent], completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func addWorkoutEvents(_ workoutEvents: [HKWorkoutEvent]) async throws
```

```objc
- (void) addWorkoutEvents:(NSArray<HKWorkoutEvent *> *) workoutEvents completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

## See Also

### Adding events to the workout
- [var workoutEvents: [HKWorkoutEvent]](./workoutevents.md)
  The list of events added to the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/addworkoutevents(_:completion:))*