# INSnoozeTasksIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your response to a delete tasks request.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSnoozeTasksIntentResponse
```

```objc
@interface INSnoozeTasksIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSnoozeTasksIntentResponse`](./insnoozetasksintentresponse.md) object to return information about your attempt to delete an existing task. Siri communicates your response information to the user at appropriate times.

You create an [`INSnoozeTasksIntentResponse`](./insnoozetasksintentresponse.md) object in the [`confirm(intent:completion:)`](./insnoozetasksintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insnoozetasksintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSnoozeTasksIntentHandling`](./insnoozetasksintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSnoozeTasksIntentResponseCode, userActivity: NSUserActivity?)](./insnoozetasksintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSnoozeTasksIntentResponseCode](./insnoozetasksintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INSnoozeTasksIntentResponseCode](./insnoozetasksintentresponsecode.md)
  Constants that indicate the response state.
### Accessing the Response Details
- [var snoozedTasks: [INTask]?](./insnoozetasksintentresponse/snoozedtasks.md)
  An array of tasks to snooze.

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

### Task Deferral
- [protocol INSnoozeTasksIntentHandling](./insnoozetasksintenthandling.md)
  The handler interface that snoozes tasks in a task list.
- [class INSnoozeTasksIntent](./insnoozetasksintent.md)
  A request to snooze one or more tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponse)*