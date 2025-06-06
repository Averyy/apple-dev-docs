# needsToContinueInForegroundError(_:continuation:)

**Framework**: App Intents  
**Kind**: method

A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func needsToContinueInForegroundError(_ dialog: IntentDialog? = nil, continuation: (@MainActor () async throws -> Void)? = nil) -> AppIntentError
```

#### Discussion

Call this method when you need to stop performing the app intent and ask a person to continue execution in the foreground. Provide an optional continuation closure that runs on the main thread to update your app’s state after the person permits the action to continue in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent/needstocontinueinforegrounderror(_:continuation:))*