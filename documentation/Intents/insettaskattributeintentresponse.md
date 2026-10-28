# INSetTaskAttributeIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your response to a request to modify the attributes of an existing task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSetTaskAttributeIntentResponse
```

```objc
@interface INSetTaskAttributeIntentResponse : INIntentResponse
```

## Overview

Use an [`INSetTaskAttributeIntentResponse`](./insettaskattributeintentresponse.md) object to return information about your attempt to update an existing task. Siri communicates the information from your response to the user at appropriate times.

You create an [`INSetTaskAttributeIntentResponse`](./insettaskattributeintentresponse.md) object in the [`confirm(intent:completion:)`](./insettaskattributeintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insettaskattributeintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSetTaskAttributeIntentHandling`](./insettaskattributeintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetTaskAttributeIntentResponseCode, userActivity: NSUserActivity?)](./insettaskattributeintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetTaskAttributeIntentResponseCode](./insettaskattributeintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetTaskAttributeIntentResponseCode](./insettaskattributeintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Task Details
- [var modifiedTask: INTask?](./insettaskattributeintentresponse/modifiedtask.md)
  The modified task.

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

### Task Attributes
- [protocol INSetTaskAttributeIntentHandling](./insettaskattributeintenthandling.md)
  The handler interface for updating the attributes of an existing task.
- [class INSetTaskAttributeIntent](./insettaskattributeintent.md)
  A request to modify the attributes of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponse)*