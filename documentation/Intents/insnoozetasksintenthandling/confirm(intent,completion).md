# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can snooze the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func confirm(intent: INSnoozeTasksIntent, completion: @escaping @Sendable (INSnoozeTasksIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSnoozeTasksIntent) async -> INSnoozeTasksIntentResponse
```

```objc
- (void) confirmSnoozeTasks:(INSnoozeTasksIntent *) intent completion:(void (^)(INSnoozeTasksIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can snooze the tasks, but don’t do so yet. If snoozing tasks involves contacting a remote server, first validate that your server is available and ready to handle the requests, then in your implementation, execute the provided completion block with a response object that indicates your app’s readiness to snooze the tasks.

## Parameters

- `intent`: The intent object that contains details about the user’s request. This object’s information has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INSnoozeTasksIntentResponse`](../insnoozetasksintentresponse.md) object that contains the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintenthandling/confirm(intent:completion:))*