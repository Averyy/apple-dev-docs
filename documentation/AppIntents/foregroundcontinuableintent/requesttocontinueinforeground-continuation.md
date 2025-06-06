# requestToContinueInForeground(_:continuation:)

**Framework**: App Intents  
**Kind**: method

A method you call to ask a person to continue an action in the foreground.

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
@discardableResult
func requestToContinueInForeground<ResultValue>(_ dialog: IntentDialog? = nil, continuation: @MainActor () async throws -> ResultValue = { () }) async throws -> ResultValue where ResultValue : Sendable
```

#### Discussion

To update your app’s state after a person permits the action to continue execution in the foreground, provide an optional continuation closure that the system executes on the main thread. The system passes the result of the closure back to the function’s caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent/requesttocontinueinforeground(_:continuation:))*