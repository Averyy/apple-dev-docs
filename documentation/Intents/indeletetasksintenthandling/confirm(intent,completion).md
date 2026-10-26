# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Validates whether you can delete the task.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INDeleteTasksIntent, completion: @escaping @Sendable (INDeleteTasksIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INDeleteTasksIntent) async -> INDeleteTasksIntentResponse
```

```objc
- (void) confirmDeleteTasks:(INDeleteTasksIntent *) intent completion:(void (^)(INDeleteTasksIntentResponse *response)) completion;
```

#### Discussion

This method validates that you can delete the task, but doesn’t delete it yet. If deleting tasks involves contacting a remote server, validate that your server is available and ready to handle requests. In your implementation, execute the provided completion block with a response object that indicates your app’s readiness to delete the task.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Your handler object has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INDeleteTasksIntentResponse`](../indeletetasksintentresponse.md) object that contains the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintenthandling/confirm(intent:completion:))*