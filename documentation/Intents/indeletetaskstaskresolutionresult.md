# INDeleteTasksTaskResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for deleting tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskResolutionResult is deprecated. There is no replacement.

## Declaration

```swift
class INDeleteTasksTaskResolutionResult
```

```objc
@interface INDeleteTasksTaskResolutionResult : INTaskResolutionResult
```

## Overview

You return an [`INDeleteTasksTaskResolutionResult`](./indeletetaskstaskresolutionresult.md) object when resolving parameters containing an [`INDeleteTasksTaskUnsupportedReason`](./indeletetaskstaskunsupportedreason.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(taskResolutionResult: INTaskResolutionResult)](./indeletetaskstaskresolutionresult/init%28taskresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task.
- [class func unsupported(forReason: INDeleteTasksTaskUnsupportedReason) -> Self](./indeletetaskstaskresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task before continuing.
- [enum INDeleteTasksTaskUnsupportedReason](./indeletetaskstaskunsupportedreason.md)
  Constants that indicate the reason the app can’t support the delete task request.

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

### Task Deletion
- [protocol INDeleteTasksIntentHandling](./indeletetasksintenthandling.md)
  An interface that handles requests to delete tasks from a task list.
- [class INDeleteTasksIntent](./indeletetasksintent.md)
  A request to delete one or more tasks.
- [class INDeleteTasksIntentResponse](./indeletetasksintentresponse.md)
  Your response to a request to delete tasks.
- [class INDeleteTasksTaskListResolutionResult](./indeletetaskstasklistresolutionresult.md)
  A resolution result for deleting task lists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstaskresolutionresult)*