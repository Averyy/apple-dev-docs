# continueInForeground(_:alwaysConfirm:)

**Framework**: App Intents  
**Kind**: method

A method you call to ask a person to continue an action in the foreground.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func continueInForeground(_ dialog: IntentDialog? = nil, alwaysConfirm: Bool = true) async throws
```

#### Discussion

To update your app’s state after a person permits the action to continue execution in the foreground, provide an optional continuation closure that the system executes on the main thread. The system passes the result of the closure back to the function’s caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/continueinforeground(_:alwaysconfirm:))*