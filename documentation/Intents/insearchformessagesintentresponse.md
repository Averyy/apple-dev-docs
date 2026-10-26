# INSearchForMessagesIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a search for messages intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSearchForMessagesIntentResponse
```

```objc
@interface INSearchForMessagesIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSearchForMessagesIntentResponse`](./insearchformessagesintentresponse.md) object to specify the results of searching the user’s messages. After performing a search using the criteria specified in the [`INSearchForMessagesIntent`](./insearchformessagesintent.md) object, create an instance of this class with the results of that search. Siri communicates the status from your response to the user at appropriate times.

You create an [`INSearchForMessagesIntentResponse`](./insearchformessagesintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchformessagesintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchformessagesintenthandling/handle%28intent,completion%29.md) methods of your search for messages handler object. For more information about implementing your handler object, see [`INSearchForMessagesIntentHandling`](./insearchformessagesintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForMessagesIntentResponseCode, userActivity: NSUserActivity?)](./insearchformessagesintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchForMessagesIntentResponseCode](./insearchformessagesintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSearchForMessagesIntentResponseCode](./insearchformessagesintentresponsecode.md)
  Constants that indicate the response state.
### Accessing the Response Details
- [var messages: [INMessage]?](./insearchformessagesintentresponse/messages.md)
  The array of messages matching the search parameters.

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

### Searching for Messages
- [protocol INSearchForMessagesIntentHandling](./insearchformessagesintenthandling.md)
  An interface that handles requests to search the current user’s messages.
- [class INSearchForMessagesIntent](./insearchformessagesintent.md)
  A request to list the messages that match the specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponse)*