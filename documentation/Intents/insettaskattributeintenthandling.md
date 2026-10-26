# INSetTaskAttributeIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for updating the attributes of an existing task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
protocol INSetTaskAttributeIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetTaskAttributeIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSetTaskAttributeIntentHandling`](./insettaskattributeintenthandling.md) protocol to resolve, confirm, and handle requests to modify the attributes of a task. SiriKit supports changing the task’s completion status and changing the location- or time-based triggers that you use to generate reminders. Adopt this protocol in an object of your Intents extension that is capable of handling the request directly or forwarding the request to your app or task management service.

Siri delivers an [`INSetTaskAttributeIntent`](./insettaskattributeintent.md) object to your handler when the user asks to modify an existing task. The provided intent object contains descriptions of the tasks and the new values to apply. If a value is not provided for a given attribute, do not modify that attribute. Use the methods of this protocol to resolve the parameters and update the task.

## Topics

### Resolving the Intent Parameters
- [func resolveTargetTask(for: INSetTaskAttributeIntent, with: (INTaskResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvetargettask%28for,with%29.md)
  Resolves which task the user wants to modify.
- [func resolveStatus(for: INSetTaskAttributeIntent, with: (INTaskStatusResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvestatus%28for,with%29.md)
  Resolves the intended status of the task.
- [func resolveSpatialEventTrigger(for: INSetTaskAttributeIntent, with: (INSpatialEventTriggerResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvespatialeventtrigger%28for,with%29.md)
  Resolves the location-based trigger to apply to the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INSetTaskAttributeTemporalEventTriggerResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvetemporaleventtrigger%28for,with%29-9bfly.md)
  Resolves the time-based trigger to apply to the task.
- [func resolvePriority(for: INSetTaskAttributeIntent, with: (INTaskPriorityResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvepriority%28for,with%29.md)
  Resolves the intended priority of the task.
- [func resolveTaskTitle(for: INSetTaskAttributeIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvetasktitle%28for,with%29.md)
  Resolves the intended title of the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./insettaskattributeintenthandling/resolvetemporaleventtrigger%28for,with%29-1wr3f.md)
  Resolves the time-based trigger to apply to the task.
### Confirming the Response
- [func confirm(intent: INSetTaskAttributeIntent, completion: (INSetTaskAttributeIntentResponse) -> Void)](./insettaskattributeintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can modify the task’s attributes.
### Handling the Intent
- [func handle(intent: INSetTaskAttributeIntent, completion: (INSetTaskAttributeIntentResponse) -> Void)](./insettaskattributeintenthandling/handle%28intent,completion%29.md)
  Handles the modification of the attributes of a task.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Task Attributes
- [class INSetTaskAttributeIntent](./insettaskattributeintent.md)
  A request to modify the attributes of a task.
- [class INSetTaskAttributeIntentResponse](./insettaskattributeintentresponse.md)
  Your response to a request to modify the attributes of an existing task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling)*