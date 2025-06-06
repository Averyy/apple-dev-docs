# RelevantIntentManager

**Framework**: App Intents  
**Kind**: class

A type that saves relevant intents.

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
final class RelevantIntentManager
```

## Topics

### Instance Methods
- [func updateRelevantIntents([RelevantIntent]) async throws](relevantintentmanager/updaterelevantintents(_:).md)
  Give the system the list of relevant intents for your app. To replace the list, call this method again, passing in a new list of relevant intents.  To remove all relevant intents associated with your app, call this method with an empty array.
### Type Properties
- [static let shared: RelevantIntentManager](relevantintentmanager/shared.md)
  Get the singleton shared instance of this class.

## See Also

- [struct RelevantIntent](relevantintent.md)
  A type that specifies an intent and its relevance to the user.
- [struct RelevantContext](relevantcontext.md)
  A type that specifies conditions for relevance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintentmanager)*