# sleep(_:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant because of a person’s sleep schedule.

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
static func sleep(_ condition: RelevantContext.SleepCondition) -> RelevantContext
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

To indicate relevance based on a sleep condition, request the [`sleepAnalysis`](https://developer.apple.com/documentation/HealthKit/HKCategoryTypeIdentifier/sleepAnalysis) permission. If contextual sleep information isn’t available to the system, sleep clues to signal relevance don’t have an effect. For more information about requesting HealthKit permissions, refer to [`Authorizing access to health data`](https://developer.apple.com/documentation/HealthKit/authorizing-access-to-health-data).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `condition`: A value that describes a person’s typical bedtime or wakeup time.

## See Also

- [RelevantContext.SleepCondition](relevantcontext/sleepcondition.md)
  Values that represent a person’s typical bedtime or wakeup time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/sleep(_:))*