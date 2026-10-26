# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles snoozing a task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
func handle(intent: INSnoozeTasksIntent, completion: @escaping @Sendable (INSnoozeTasksIntentResponse) -> Void)
```

```swift
func handle(intent: INSnoozeTasksIntent) async -> INSnoozeTasksIntentResponse
```

```objc
- (void) handleSnoozeTasks:(INSnoozeTasksIntent *) intent completion:(void (^)(INSnoozeTasksIntentResponse *response)) completion;
```

#### Discussion

Implement this method to snooze the task based on the information in the intent parameter, create a response object with the relevant details, and call the provided completion handler.

## Parameters

- `intent`: The intent object containing details about the user’s request. This object’s information has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSnoozeTasksIntentResponse`](../insnoozetasksintentresponse.md) object that contains the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintenthandling/handle(intent:completion:))*