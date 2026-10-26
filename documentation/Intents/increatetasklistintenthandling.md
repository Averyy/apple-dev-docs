# INCreateTaskListIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for creating task lists.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INCreateTaskListIntentHandling : NSObjectProtocol
```

```objc
@protocol INCreateTaskListIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INCreateTaskListIntentHandling`](./increatetasklistintenthandling.md) protocol to resolve, confirm, and handle requests to create task lists. Adopt this protocol in an object of your Intents extension that’s capable of forwarding the task list information to your app or task management service.

Siri delivers an [`INCreateTaskListIntent`](./increatetasklistintent.md) object to your handler when the user asks to create a task list using your app. The provided intent object contains the details for the task list, including any initial tasks. Use the methods of this protocol to resolve the parameters and create the task list.

## Topics

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateTaskListIntent, with: (INSpeakableStringResolutionResult) -> Void)](./increatetasklistintenthandling/resolvetitle%28for,with%29.md)
  Resolves the title of the task list.
- [func resolveTaskTitles(for: INCreateTaskListIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./increatetasklistintenthandling/resolvetasktitles%28for,with%29.md)
  Resolves the tasks in a task list.
- [func resolveGroupName(for: INCreateTaskListIntent, with: (INSpeakableStringResolutionResult) -> Void)](./increatetasklistintenthandling/resolvegroupname%28for,with%29.md)
  Resolves the intended group for the task list.
### Confirming the Response
- [func confirm(intent: INCreateTaskListIntent, completion: (INCreateTaskListIntentResponse) -> Void)](./increatetasklistintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can create the task list.
### Handling the Intent
- [func handle(intent: INCreateTaskListIntent, completion: (INCreateTaskListIntentResponse) -> Void)](./increatetasklistintenthandling/handle%28intent,completion%29.md)
  Handles the creation of a task list.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Task List Creation
- [class INCreateTaskListIntent](./increatetasklistintent.md)
  A request to create a new task list.
- [class INCreateTaskListIntentResponse](./increatetasklistintentresponse.md)
  Your app’s response to a request to create a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintenthandling)*