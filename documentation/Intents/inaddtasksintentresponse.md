# INAddTasksIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your response to a request to add tasks to a task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INAddTasksIntentResponse
```

```objc
@interface INAddTasksIntentResponse : INIntentResponse
```

## Overview

Use an [`INAddTasksIntentResponse`](./inaddtasksintentresponse.md) object to return information about the task list that you created. Siri communicates the information from your response to the user at appropriate times.

You create an [`INAddTasksIntentResponse`](./inaddtasksintentresponse.md) object in the [`confirm(intent:completion:)`](./inaddtasksintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inaddtasksintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INAddTasksIntentHandling`](./inaddtasksintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INAddTasksIntentResponseCode, userActivity: NSUserActivity?)](./inaddtasksintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INAddTasksIntentResponseCode](./inaddtasksintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INAddTasksIntentResponseCode](./inaddtasksintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Task Information
- [var addedTasks: [INTask]?](./inaddtasksintentresponse/addedtasks.md)
  The tasks that you added to the task list.
- [var modifiedTaskList: INTaskList?](./inaddtasksintentresponse/modifiedtasklist.md)
  The task list that you modified.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Task Addition
- [protocol INAddTasksIntentHandling](./inaddtasksintenthandling.md)
  The handler interface for adding tasks to a task list.
- [class INAddTasksIntent](./inaddtasksintent.md)
  A request to add tasks to an existing task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponse)*