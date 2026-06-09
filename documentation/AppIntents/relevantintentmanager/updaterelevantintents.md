# updateRelevantIntents(_:)

**Framework**: App Intents  
**Kind**: method

Sets the relevant app intents for the system to suggest.

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
final func updateRelevantIntents(_ relevantIntents: [RelevantIntent]) async throws
```

#### Discussion

- Parameter - relevantIntents: The array of relevant intents that currently apply to your app. Specify an empty array if your app doesn’t have any intents to suggest.

Use this method to specify the complete set of relevant app intents for the system to consider. The system uses the relevance information in the [`RelevantIntent`](relevantintent.md) structure to determine when to suggest the action. This method runs asynchronously and throws an error if it’s unable to update the current set of intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintentmanager/updaterelevantintents(_:))*