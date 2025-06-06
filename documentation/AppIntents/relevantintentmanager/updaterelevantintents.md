# updateRelevantIntents(_:)

**Framework**: App Intents  
**Kind**: method

Give the system the list of relevant intents for your app. To replace the list, call this method again, passing in a new list of relevant intents.  To remove all relevant intents associated with your app, call this method with an empty array.

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
final func updateRelevantIntents(_ relevantIntents: [RelevantIntent]) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintentmanager/updaterelevantintents(_:))*