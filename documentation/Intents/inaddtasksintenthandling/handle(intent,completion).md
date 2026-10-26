# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the creation of a task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
func handle(intent: INAddTasksIntent, completion: @escaping @Sendable (INAddTasksIntentResponse) -> Void)
```

```swift
func handle(intent: INAddTasksIntent) async -> INAddTasksIntentResponse
```

```objc
- (void) handleAddTasks:(INAddTasksIntent *) intent completion:(void (^)(INAddTasksIntentResponse *response)) completion;
```

#### Discussion

In your implementation of this method, create the tasks described by the `intent` parameter, create a response object with any relevant details, and call the provided completion handler.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INAddTasksIntentResponse`](../inaddtasksintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/handle(intent:completion:))*