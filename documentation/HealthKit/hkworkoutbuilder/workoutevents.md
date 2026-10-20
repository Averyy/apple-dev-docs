# workoutEvents

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The list of events added to the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var workoutEvents: [HKWorkoutEvent] { get }
```

```objc
@property (copy, readonly) NSArray<HKWorkoutEvent *> * workoutEvents;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

## See Also

### Adding events to the workout
- [func addWorkoutEvents([HKWorkoutEvent], completion: (Bool, (any Error)?) -> Void)](./addworkoutevents%28_,completion%29.md)
  Adds a workout event to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/workoutevents)*