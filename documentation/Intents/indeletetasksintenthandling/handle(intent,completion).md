# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles deleting a task.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INDeleteTasksIntent, completion: @escaping @Sendable (INDeleteTasksIntentResponse) -> Void)
```

```swift
func handle(intent: INDeleteTasksIntent) async -> INDeleteTasksIntentResponse
```

```objc
- (void) handleDeleteTasks:(INDeleteTasksIntent *) intent completion:(void (^)(INDeleteTasksIntentResponse *response)) completion;
```

#### Discussion

Use this method to transfer control of deleting the task to your app. Delete the task based on the information in the intent parameter, create a response object with the relevant details, and call the provided completion handler.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Your handler object has already resolved and confirmed this object’s information.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INDeleteTasksIntentResponse`](../indeletetasksintentresponse.md) object that contains the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintenthandling/handle(intent:completion:))*