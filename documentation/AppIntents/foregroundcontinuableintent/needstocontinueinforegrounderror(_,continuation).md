# needsToContinueInForegroundError(_:continuation:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.

**Availability**:
- iOS 16.4+ - Deprecated in 26.0
- iPadOS 16.4+ - Deprecated in 26.0
- Mac Catalyst 16.4+ - Deprecated in 26.0
- macOS 13.3+ - Deprecated in 26.0
- tvOS 16.4+ - Deprecated in 26.0
- visionOS
- watchOS 9.4+ - Deprecated in 26.0

> **Deprecated**: Please include '.foreground(.dynamic)' in the 'supportedModes' of your app intent instead

## Declaration

```swift
func needsToContinueInForegroundError(_ dialog: IntentDialog? = nil, continuation: (@MainActor () async throws -> Void)? = nil) -> AppIntentError
```

#### Discussion

Call this method when you need to stop performing the app intent and ask a person to continue execution in the foreground. Provide an optional continuation closure that runs on the main thread to update your app’s state after the person permits the action to continue in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent/needstocontinueinforegrounderror(_:continuation:))*