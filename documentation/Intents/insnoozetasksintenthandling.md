# INSnoozeTasksIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface that snoozes tasks in a task list.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
protocol INSnoozeTasksIntentHandling : NSObjectProtocol
```

```objc
@protocol INSnoozeTasksIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSnoozeTasksIntentHandling`](./insnoozetasksintenthandling.md) protocol to resolve, confirm, and handle requests to snooze tasks in a task list. Adopt this protocol in an object of your Intents extension capable of handling the request directly or forwarding the request to your app or task management service.

Siri delivers an [`INSnoozeTasksIntent`](./insnoozetasksintent.md) object to your handler when the user asks to snooze tasks in a task list in your app. The provided intent object contains descriptions of the tasks and any triggers to associate with each task. Use the methods of this protocol to resolve the parameters and snooze the tasks.

## Topics

### Resolving Details of the Intent
- [func resolveNextTriggerTime(for: INSnoozeTasksIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insnoozetasksintenthandling/resolvenexttriggertime%28for,with%29.md)
  Resolves the trigger of when to snooze tasks.
- [func resolveTasks(for: INSnoozeTasksIntent, with: ([INSnoozeTasksTaskResolutionResult]) -> Void)](./insnoozetasksintenthandling/resolvetasks%28for,with%29.md)
  Resolves the tasks to snooze.
### Confirming the Response
- [func confirm(intent: INSnoozeTasksIntent, completion: (INSnoozeTasksIntentResponse) -> Void)](./insnoozetasksintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can snooze the task.
### Handling the Intent
- [func handle(intent: INSnoozeTasksIntent, completion: (INSnoozeTasksIntentResponse) -> Void)](./insnoozetasksintenthandling/handle%28intent,completion%29.md)
  Handles snoozing a task.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Task Deferral
- [class INSnoozeTasksIntent](./insnoozetasksintent.md)
  A request to snooze one or more tasks.
- [class INSnoozeTasksIntentResponse](./insnoozetasksintentresponse.md)
  Your response to a delete tasks request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintenthandling)*