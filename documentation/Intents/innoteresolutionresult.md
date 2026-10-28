# INNoteResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for notes.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNoteResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INNoteResolutionResult
```

```objc
@interface INNoteResolutionResult : INIntentResolutionResult
```

## Overview

You return an [`INNoteResolutionResult`](./innoteresolutionresult.md) object when resolving parameters containing an [`INNote`](./innote.md) object. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INNote) -> Self](./innoteresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INNote?) -> Self](./innoteresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.
- [class func disambiguation(with: [INNote]) -> Self](./innoteresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innoteresolutionresult)*