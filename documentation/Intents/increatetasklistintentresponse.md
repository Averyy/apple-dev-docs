# INCreateTaskListIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to create a task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INCreateTaskListIntentResponse
```

```objc
@interface INCreateTaskListIntentResponse : INIntentResponse
```

#### Overview

Use an [`INCreateTaskListIntentResponse`](./increatetasklistintentresponse.md) object to return information about the task list that your app created. Siri communicates the information from your response to the user at appropriate times.

You create an [`INCreateTaskListIntentResponse`](./increatetasklistintentresponse.md) object in the [`confirm(intent:completion:)`](./increatetasklistintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./increatetasklistintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INCreateTaskListIntentHandling`](./increatetasklistintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INCreateTaskListIntentResponseCode, userActivity: NSUserActivity?)](./increatetasklistintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INCreateTaskListIntentResponseCode](./increatetasklistintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.
- [enum INCreateTaskListIntentResponseCode](./increatetasklistintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Task List
- [var createdTaskList: INTaskList?](./increatetasklistintentresponse/createdtasklist.md)
  The details of the task list that your app created.

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

### Task List Creation
- [protocol INCreateTaskListIntentHandling](./increatetasklistintenthandling.md)
  The handler interface for creating task lists.
- [class INCreateTaskListIntent](./increatetasklistintent.md)
  A request to create a new task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponse)*