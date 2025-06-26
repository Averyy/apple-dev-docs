# RelevantContext

**Framework**: RelevanceKit  
**Kind**: struct

Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.

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
struct RelevantContext
```

#### Overview

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information about widgets in Smart Stacks, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Topics

### Fitness clues
- [static func fitness(RelevantContext.FitnessCondition) -> RelevantContext](relevantcontext/fitness(_:).md)
  Tells the system a widget is relevant because of a person’s fitness activity.
- [RelevantContext.FitnessCondition](relevantcontext/fitnesscondition.md)
  Values that represent a person’s fitness activity.
### Hardware clues
- [static func hardware(headphones: RelevantContext.HeadphonesCondition) -> RelevantContext](relevantcontext/hardware(headphones:).md)
  Tells the system a widget is relevant when a person’s headphones are connected.
- [RelevantContext.HeadphonesCondition](relevantcontext/headphonescondition.md)
  A structure that indicates whether a person’s headphones are connected.
### Location clues
- [static func location(category: MKPointOfInterestCategory) -> RelevantContext?](relevantcontext/location(category:).md)
  Tells the system a widget is relevant close to points of interest of a specific category.
- [static func location(CLRegion) -> RelevantContext](relevantcontext/location(_:).md)
  Tells the system a widget is relevant at a specific location.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](relevantcontext/location(inferred:).md)
  Tells the system a widget is relevant at a person’s inferred location.
- [RelevantContext.InferredLocation](relevantcontext/inferredlocation.md)
  A structure with values for a person’s inferred home, work, school, and commute locations.
### Sleep clues
- [static func sleep(RelevantContext.SleepCondition) -> RelevantContext](relevantcontext/sleep(_:).md)
  Tells the system a widget is relevant because of a person’s sleep schedule.
- [RelevantContext.SleepCondition](relevantcontext/sleepcondition.md)
  Values that represent a person’s typical bedtime or wakeup time.
### Time clues
- [static func date(Date) -> RelevantContext](relevantcontext/date(_:).md)
  Tells the system a widget is relevant at a specific date.
- [static func date(Date, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(_:kind:).md)
  Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- [static func date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(interval:kind:).md)
  Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- [static func date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext](relevantcontext/date(range:kind:).md)
  Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- [RelevantContext.DateKind](relevantcontext/datekind.md)
  Values the system uses as additional context for time-based relevance clues.
- [static func date(from: Date, to: Date) -> RelevantContext](relevantcontext/date(from:to:).md)
  Tells the system a widget is relevant between two dates.

## See Also

- [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/Widget-Suggestions-In-Smart-Stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext)*