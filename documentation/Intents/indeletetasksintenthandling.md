# INDeleteTasksIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to delete tasks from a task list.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INDeleteTasksIntentHandling : NSObjectProtocol
```

```objc
@protocol INDeleteTasksIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INDeleteTasksIntentHandling`](./indeletetasksintenthandling.md) protocol to resolve, confirm, and handle requests to delete tasks from a task list. Adopt this protocol in an object of your Intents extension capable of handling the request directly or forwarding the request to your app or task management service.

Siri delivers an [`INDeleteTasksIntent`](./indeletetasksintent.md) object to your handler when the user asks to delete tasks from a task list in your app. The provided intent object contains descriptions of the tasks and any triggers to associate with each task. Use the methods of this protocol to resolve the parameters and delete the tasks.

## Topics

### Resolving Details of the Intent
- [func resolveTaskList(for: INDeleteTasksIntent, with: (INDeleteTasksTaskListResolutionResult) -> Void)](./indeletetasksintenthandling/resolvetasklist%28for,with%29.md)
  Resolves the task list from which to delete tasks.
- [func resolveTasks(for: INDeleteTasksIntent, with: ([INDeleteTasksTaskResolutionResult]) -> Void)](./indeletetasksintenthandling/resolvetasks%28for,with%29.md)
  Resolves the tasks to delete.
### Confirming the Response
- [func confirm(intent: INDeleteTasksIntent, completion: (INDeleteTasksIntentResponse) -> Void)](./indeletetasksintenthandling/confirm%28intent,completion%29.md)
  Validates whether you can delete the task.
### Handling the Intent
- [func handle(intent: INDeleteTasksIntent, completion: (INDeleteTasksIntentResponse) -> Void)](./indeletetasksintenthandling/handle%28intent,completion%29.md)
  Handles deleting a task.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Task Deletion
- [class INDeleteTasksIntent](./indeletetasksintent.md)
  A request to delete one or more tasks.
- [class INDeleteTasksIntentResponse](./indeletetasksintentresponse.md)
  Your response to a request to delete tasks.
- [class INDeleteTasksTaskListResolutionResult](./indeletetaskstasklistresolutionresult.md)
  A resolution result for deleting task lists.
- [class INDeleteTasksTaskResolutionResult](./indeletetaskstaskresolutionresult.md)
  A resolution result for deleting tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintenthandling)*