# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can add the tasks to the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func confirm(intent: INAddTasksIntent, completion: @escaping @Sendable (INAddTasksIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INAddTasksIntent) async -> INAddTasksIntentResponse
```

```objc
- (void) confirmAddTasks:(INAddTasksIntent *) intent completion:(void (^)(INAddTasksIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can add the tasks to the specified task list, but do not do so yet. If adding the tasks involves contacting a remote server, validate that your server is available and ready to handle requests. In your implementation, execute the provided completion block with a response object indicating your app’s readiness to add the tasks to the task list.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INAddTasksIntentResponse`](../inaddtasksintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/confirm(intent:completion:))*