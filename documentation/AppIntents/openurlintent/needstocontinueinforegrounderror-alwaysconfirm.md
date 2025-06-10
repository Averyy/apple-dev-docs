# needsToContinueInForegroundError(_:alwaysConfirm:)

**Framework**: App Intents  
**Kind**: method

A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func needsToContinueInForegroundError(_ dialog: IntentDialog? = nil, alwaysConfirm: Bool = true) -> AppIntentError
```

#### Discussion

Call this method when you need to stop performing the app intent and ask a person to continue execution in the foreground. Provide an optional continuation closure that runs on the main thread to update your app’s state after the person permits the action to continue in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/needstocontinueinforegrounderror(_:alwaysconfirm:))*