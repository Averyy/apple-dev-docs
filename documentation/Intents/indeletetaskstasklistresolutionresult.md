# INDeleteTasksTaskListResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for deleting task lists.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskListResolutionResult is deprecated. There is no replacement.

## Declaration

```swift
class INDeleteTasksTaskListResolutionResult
```

```objc
@interface INDeleteTasksTaskListResolutionResult : INTaskListResolutionResult
```

## Overview

You return an [`INDeleteTasksTaskListResolutionResult`](./indeletetaskstasklistresolutionresult.md) object when resolving parameters containing an [`INDeleteTasksTaskListUnsupportedReason`](./indeletetaskstasklistunsupportedreason.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(taskListResolutionResult: INTaskListResolutionResult)](./indeletetaskstasklistresolutionresult/init%28tasklistresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task from a task list.
- [class func unsupported(forReason: INDeleteTasksTaskListUnsupportedReason) -> Self](./indeletetaskstasklistresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task list before continuing.
- [enum INDeleteTasksTaskListUnsupportedReason](./indeletetaskstasklistunsupportedreason.md)
  Constants that indicate the reason an app can’t support the delete task request.

## Relationships

### Inherits From
- [INTaskListResolutionResult](./intasklistresolutionresult.md)
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
- [class INDeleteTasksTaskResolutionResult](./indeletetaskstaskresolutionresult.md)
  A resolution result for deleting tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstasklistresolutionresult)*