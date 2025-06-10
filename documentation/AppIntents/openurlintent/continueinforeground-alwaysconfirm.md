# continueInForeground(_:alwaysConfirm:)

**Framework**: App Intents  
**Kind**: method

A method you call to ask a person to continue an action in the foreground.

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
func continueInForeground(_ dialog: IntentDialog? = nil, alwaysConfirm: Bool = true) async throws
```

#### Discussion

To update your app’s state after a person permits the action to continue execution in the foreground, provide an optional continuation closure that the system executes on the main thread. The system passes the result of the closure back to the function’s caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/continueinforeground(_:alwaysconfirm:))*