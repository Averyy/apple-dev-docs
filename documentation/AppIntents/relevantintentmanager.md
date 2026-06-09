# RelevantIntentManager

**Framework**: App Intents  
**Kind**: class

A type you use to suggest app intents and their current relevance to a person.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final class RelevantIntentManager
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Overview

Use the shared `RelevantIntentManager` object to specify the actions your app wants to suggest and their current relevance. Register any relevant app intents at launch time and any time the set of actions changes later. You can register multiple actions at once, and the system uses the relevance factors for each one to determine when to suggest the action. If you don’t have any current actions to suggest, register an empty set to prevent the system from suggesting outdated actions.

You don’t create instances of this class yourself. Instead, use the object in the [`shared`](relevantintentmanager/shared.md) property to set the relevant intents for your entire app.

## Topics

### Instance Methods
- [func updateRelevantIntents([RelevantIntent]) async throws](relevantintentmanager/updaterelevantintents(_:).md)
  Sets the relevant app intents for the system to suggest.
### Type Properties
- [static let shared: RelevantIntentManager](relevantintentmanager/shared.md)
  The shared instance of this class.

## See Also

- [struct RelevantIntent](relevantintent.md)
  A type that stores an app intent and indicates its relevance to someone.
- [struct RelevantContext](../RelevanceKit/RelevantContext.md)
  Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintentmanager)*