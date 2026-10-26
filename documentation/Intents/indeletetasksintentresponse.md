# INDeleteTasksIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your response to a request to delete tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INDeleteTasksIntentResponse
```

```objc
@interface INDeleteTasksIntentResponse : INIntentResponse
```

#### Overview

Use an [`INDeleteTasksIntentResponse`](./indeletetasksintentresponse.md) object to return information about your attempt to delete an existing task. Siri communicates the information from your response to the user at appropriate times.

You create an [`INDeleteTasksIntentResponse`](./indeletetasksintentresponse.md) object in the [`confirm(intent:completion:)`](./indeletetasksintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./indeletetasksintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INDeleteTasksIntentHandling`](./indeletetasksintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INDeleteTasksIntentResponseCode, userActivity: NSUserActivity?)](./indeletetasksintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Accessing the Deleted Tasks
- [var deletedTasks: [INTask]?](./indeletetasksintentresponse/deletedtasks.md)
  An array of tasks to delete.
### Getting the Response Code
- [var code: INDeleteTasksIntentResponseCode](./indeletetasksintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INDeleteTasksIntentResponseCode](./indeletetasksintentresponsecode.md)
  Constants that indicate the response state.

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

### Task Deletion
- [protocol INDeleteTasksIntentHandling](./indeletetasksintenthandling.md)
  An interface that handles requests to delete tasks from a task list.
- [class INDeleteTasksIntent](./indeletetasksintent.md)
  A request to delete one or more tasks.
- [class INDeleteTasksTaskListResolutionResult](./indeletetaskstasklistresolutionresult.md)
  A resolution result for deleting task lists.
- [class INDeleteTasksTaskResolutionResult](./indeletetaskstaskresolutionresult.md)
  A resolution result for deleting tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintentresponse)*