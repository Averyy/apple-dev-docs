# INSendMessageIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a send message intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSendMessageIntentResponse
```

```objc
@interface INSendMessageIntentResponse : INIntentResponse
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Overview

Use an [`INSendMessageIntentResponse`](./insendmessageintentresponse.md) object to specify the results of sending a message to another user. You create instances of this class when confirming or handling a send message intent. Use this object to communicate whether the message was successfully sent or whether an error occurred.

You create an [`INSendMessageIntentResponse`](./insendmessageintentresponse.md) object in the [`confirm(intent:completion:)`](./insendmessageintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insendmessageintenthandling/handle%28intent,completion%29.md) methods of your send message handler object. For more information about implementing your handler object, see [`INSendMessageIntentHandling`](./insendmessageintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSendMessageIntentResponseCode, userActivity: NSUserActivity?)](./insendmessageintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSendMessageIntentResponseCode](./insendmessageintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSendMessageIntentResponseCode](./insendmessageintentresponsecode.md)
  Constants that indicate the response state.
### Providing the Message
- [var sentMessage: INMessage?](./insendmessageintentresponse/sentmessage.md)
  The message sent by the intent.
### Instance Properties
- [var sentMessages: [INMessage]?](./insendmessageintentresponse/sentmessages.md)

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

### Sending a Message
- [protocol INSendMessageIntentHandling](./insendmessageintenthandling.md)
  An interface to handle sending messages to one or more designated users.
- [class INSendMessageIntent](./insendmessageintent.md)
  A request to send a message to the designated recipients.
- [enum INOutgoingMessageType](./inoutgoingmessagetype.md)
  The format of the message.
- [class INSendMessageAttachment](./insendmessageattachment.md)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](./insendmessageintentdonationmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponse)*