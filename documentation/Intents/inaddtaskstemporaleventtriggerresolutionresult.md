# INAddTasksTemporalEventTriggerResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for a temporal event trigger.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class INAddTasksTemporalEventTriggerResolutionResult
```

```objc
@interface INAddTasksTemporalEventTriggerResolutionResult : INTemporalEventTriggerResolutionResult
```

#### Overview

You return an [`INAddTasksTemporalEventTriggerResolutionResult`](./inaddtaskstemporaleventtriggerresolutionresult.md) object when resolving parameters that contain an [`INTemporalEventTrigger`](./intemporaleventtrigger.md) value for an [`INAddTasksIntent`](./inaddtasksintent.md). Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution operators, see [`INTemporalEventTriggerResolutionResult`](./intemporaleventtriggerresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)](./inaddtaskstemporaleventtriggerresolutionresult/init%28temporaleventtriggerresolutionresult%29.md)
  Creates an object whose resolution successfully matches the specified temporal event.
- [class func unsupported(forReason: INAddTasksTemporalEventTriggerUnsupportedReason) -> Self](./inaddtaskstemporaleventtriggerresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution provides a reason why the temporal event trigger cannot be applied to the task the user intends to create.
- [enum INAddTasksTemporalEventTriggerUnsupportedReason](./inaddtaskstemporaleventtriggerunsupportedreason.md)
  Reasons the app can’t create a task with a particular temporal event trigger.

## Relationships

### Inherits From
- [INTemporalEventTriggerResolutionResult](./intemporaleventtriggerresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INAddTasksTargetTaskListResolutionResult](./inaddtaskstargettasklistresolutionresult.md)
  A resolution result that adds tasks to a target task list.
- [class INDateSearchTypeResolutionResult](./indatesearchtyperesolutionresult.md)
  A resolution result for the types of dates supported by a search.
- [class INLocationSearchTypeResolutionResult](./inlocationsearchtyperesolutionresult.md)
  A resolution result for location-based searches.
- [class INNoteResolutionResult](./innoteresolutionresult.md)
  A resolution result for notes.
- [class INNoteContentResolutionResult](./innotecontentresolutionresult.md)
  A resolution result for the content of notes.
- [class INNotebookItemTypeResolutionResult](./innotebookitemtyperesolutionresult.md)
  A resolution result for the type of items to look for during a search of notes and tasks.
- [class INSetTaskAttributeTemporalEventTriggerResolutionResult](./insettaskattributetemporaleventtriggerresolutionresult.md)
  A resolution result for a temporal event trigger.
- [class INSnoozeTasksTaskResolutionResult](./insnoozetaskstaskresolutionresult.md)
  A resolution result for snoozing a task.
- [class INSpatialEventTriggerResolutionResult](./inspatialeventtriggerresolutionresult.md)
  A resolution result for the location-based trigger associated with a task.
- [class INTaskListResolutionResult](./intasklistresolutionresult.md)
  A resolution result for a list of tasks.
- [class INTaskResolutionResult](./intaskresolutionresult.md)
  A resolution result for a single task within a task list.
- [class INTaskStatusResolutionResult](./intaskstatusresolutionresult.md)
  A resolution result for the status of a task.
- [class INTemporalEventTriggerResolutionResult](./intemporaleventtriggerresolutionresult.md)
  A resolution result for the time-based trigger associated with a task.
- [class INTaskPriorityResolutionResult](./intaskpriorityresolutionresult.md)
  A resolution result for the priority associated with a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstemporaleventtriggerresolutionresult)*