# INSnoozeTasksTaskResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for snoozing a task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class INSnoozeTasksTaskResolutionResult
```

```objc
@interface INSnoozeTasksTaskResolutionResult : INTaskResolutionResult
```

## Overview

You return an [`INSnoozeTasksTaskResolutionResult`](./insnoozetaskstaskresolutionresult.md) object when resolving parameters containing an [`INSnoozeTasksTaskUnsupportedReason`](./insnoozetaskstaskunsupportedreason.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(taskResolutionResult: INTaskResolutionResult)](./insnoozetaskstaskresolutionresult/init%28taskresolutionresult%29.md)
  Creates an object whose resolution involves successfully snoozing a task.
- [class func unsupported(forReason: INSnoozeTasksTaskUnsupportedReason) -> Self](./insnoozetaskstaskresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task to be snoozed before continuing.
- [enum INSnoozeTasksTaskUnsupportedReason](./insnoozetaskstaskunsupportedreason.md)
  Constants that indicates the reason the app can’t support the snooze task request.

## Relationships

### Inherits From
- [INTaskResolutionResult](./intaskresolutionresult.md)
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
- [class INAddTasksTemporalEventTriggerResolutionResult](./inaddtaskstemporaleventtriggerresolutionresult.md)
  A resolution result for a temporal event trigger.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetaskstaskresolutionresult)*