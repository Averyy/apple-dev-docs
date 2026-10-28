# INAddTasksIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for adding tasks to a task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
protocol INAddTasksIntentHandling : NSObjectProtocol
```

```objc
@protocol INAddTasksIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INAddTasksIntentHandling`](./inaddtasksintenthandling.md) protocol to resolve, confirm, and handle requests to add tasks to a task list. Adopt this protocol in an object of your Intents extension that’s capable of handling the request directly or forwarding the request to your app or task management service.

Siri delivers an [`INAddTasksIntent`](./inaddtasksintent.md) object to your handler when the user asks to add tasks to a task list in your app. The provided intent object contains descriptions of the tasks and any triggers to associate with each task. Use the methods of this protocol to resolve the parameters and add the tasks.

## Topics

### Resolving the Intent Parameters
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INAddTasksTargetTaskListResolutionResult) -> Void)](./inaddtasksintenthandling/resolvetargettasklist%28for,with%29-2er0u.md)
  Resolves the task list to receive the new tasks.
- [func resolveTaskTitles(for: INAddTasksIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./inaddtasksintenthandling/resolvetasktitles%28for,with%29.md)
  Resolves the titles for the tasks.
- [func resolveSpatialEventTrigger(for: INAddTasksIntent, with: (INSpatialEventTriggerResolutionResult) -> Void)](./inaddtasksintenthandling/resolvespatialeventtrigger%28for,with%29.md)
  Resolves the location-based trigger associated with the new tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INAddTasksTemporalEventTriggerResolutionResult) -> Void)](./inaddtasksintenthandling/resolvetemporaleventtrigger%28for,with%29-7yrz3.md)
  Resolves the time-based trigger associated with the new tasks.
- [func resolvePriority(for: INAddTasksIntent, with: (INTaskPriorityResolutionResult) -> Void)](./inaddtasksintenthandling/resolvepriority%28for,with%29.md)
  Resolves the priority associated with the new tasks.
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INTaskListResolutionResult) -> Void)](./inaddtasksintenthandling/resolvetargettasklist%28for,with%29-2uevx.md)
  Called when it is time for you to resolve the task list to receive the new tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./inaddtasksintenthandling/resolvetemporaleventtrigger%28for,with%29-2h9ff.md)
  Resolves the time-based trigger associated with the new tasks.
### Confirming the Response
- [func confirm(intent: INAddTasksIntent, completion: (INAddTasksIntentResponse) -> Void)](./inaddtasksintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can add the tasks to the task list.
### Handling the Intent
- [func handle(intent: INAddTasksIntent, completion: (INAddTasksIntentResponse) -> Void)](./inaddtasksintenthandling/handle%28intent,completion%29.md)
  Handles the creation of a task list.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Task Addition
- [class INAddTasksIntent](./inaddtasksintent.md)
  A request to add tasks to an existing task list.
- [class INAddTasksIntentResponse](./inaddtasksintentresponse.md)
  Your response to a request to add tasks to a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling)*