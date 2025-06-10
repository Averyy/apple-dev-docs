# fitness(_:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant because of a person’s fitness activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func fitness(_ condition: RelevantContext.FitnessCondition) -> RelevantContext
```

#### Return Value

A contextual clue the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

To indicate relevance based on a fitness condition, request permission to access HealthKit data:

- The [`workoutActive`](relevantcontext/fitnesscondition/workoutactive.md) condition requires usage of [`HKWorkoutType`](https://developer.apple.com/documentation/HealthKit/HKWorkoutType)
- The [`activityRingsIncomplete`](relevantcontext/fitnesscondition/activityringsincomplete.md) condition requires usage of [`appleExerciseTime`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/appleExerciseTime), [`appleMoveTime`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/appleMoveTime), and [`appleStandTime`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/appleStandTime).

If contextual fitness information isn’t available to the system, fitness clues to signal relevance don’t have an effect. For more information about requesting HealthKit permissions, refer to [`Authorizing access to health data`](https://developer.apple.com/documentation/HealthKit/authorizing-access-to-health-data).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `condition`: A value that describes whether a person is working out or has incomplete activity rings.

## See Also

- [RelevantContext.FitnessCondition](relevantcontext/fitnesscondition.md)
  Values that represent a person’s fitness activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/fitness(_:))*