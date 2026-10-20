# requestToContinueInForeground(_:continuation:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

A method you call to ask a person to continue an action in the foreground.

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
@discardableResult
func requestToContinueInForeground<ResultValue>(_ dialog: IntentDialog? = nil, continuation: @MainActor () async throws -> ResultValue = { () }) async throws -> ResultValue where ResultValue : Sendable
```

#### Discussion

To update your app’s state after a person permits the action to continue execution in the foreground, provide an optional continuation closure that the system executes on the main thread. The system passes the result of the closure back to the function’s caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent/requesttocontinueinforeground(_:continuation:))*