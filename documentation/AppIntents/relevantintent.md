# RelevantIntent

**Framework**: App Intents  
**Kind**: struct

A type that stores an app intent and indicates its relevance to someone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct RelevantIntent
```

#### Overview

Use a `RelevantIntent` structure to specify an action someone might want to take and the conditions when the system might want to suggest that action. For example, a sports app might create an action to start playback of a game shortly before that game starts. Specify the action using a [`WidgetConfigurationIntent`](widgetconfigurationintent.md) structure, and register the relevant intent with the system using the [`RelevantIntentManager`](relevantintentmanager.md) type.

## Topics

### Initializers
- [init<IntentType>(IntentType, widgetKind: String, relevance: RelevantContext)](relevantintent/init(_:widgetkind:relevance:).md)
  Creates an instance of this type using the specified app intent and relevance information.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Escapable](../Swift/Escapable.md)

## See Also

- [class RelevantIntentManager](relevantintentmanager.md)
  A type you use to suggest app intents and their current relevance to a person.
- [struct RelevantContext](../RelevanceKit/RelevantContext.md)
  Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintent)*