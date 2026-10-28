# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can create the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INCreateTaskListIntent, completion: @escaping @Sendable (INCreateTaskListIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INCreateTaskListIntent) async -> INCreateTaskListIntentResponse
```

```objc
- (void) confirmCreateTaskList:(INCreateTaskListIntent *) intent completion:(void (^)(INCreateTaskListIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that you can create the task list, but don’t create it yet. If creating the task list involves contacting a remote server, validate that your server is available and ready to handle requests. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to create the task list.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INCreateTaskListIntentResponse`](../increatetasklistintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintenthandling/confirm(intent:completion:))*