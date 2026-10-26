# INSendMessageIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface to handle sending messages to one or more designated users.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INSendMessageIntentHandling : NSObjectProtocol
```

```objc
@protocol INSendMessageIntentHandling <NSObject>
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)

#### Overview

Use the methods of the [`INSendMessageIntentHandling`](./insendmessageintenthandling.md) protocol to resolve, confirm, and handle requests to send text or audio messages to the designated users. Adopt this protocol in an object of your Intents extension that is capable of sending the messages.

Siri delivers an [`INSendMessageIntent`](./insendmessageintent.md) object to your handler when the user asks to send a message using your app. The provided intent object contains the recipients and content of the message. Use the methods of this protocol to resolve the parameters and to validate that sending the message is possible.

## Topics

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSendMessageIntent, with: ([INSendMessageRecipientResolutionResult]) -> Void)](./insendmessageintenthandling/resolverecipients%28for,with%29-609yw.md)
  Resolves the user’s input when it isn’t clear who the recipients of the message are.
- [func resolveOutgoingMessageType(for: INSendMessageIntent, with: (INOutgoingMessageTypeResolutionResult) -> Void)](./insendmessageintenthandling/resolveoutgoingmessagetype%28for,with%29.md)
  Determines what type of message to send.
- [func resolveContent(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./insendmessageintenthandling/resolvecontent%28for,with%29.md)
  Resolves the contents of the message.
- [func resolveSpeakableGroupName(for: INSendMessageIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insendmessageintenthandling/resolvespeakablegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.
### Confirming the Response
- [func confirm(intent: INSendMessageIntent, completion: (INSendMessageIntentResponse) -> Void)](./insendmessageintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can send the message.
### Handling the Intent
- [func handle(intent: INSendMessageIntent, completion: (INSendMessageIntentResponse) -> Void)](./insendmessageintenthandling/handle%28intent,completion%29.md)
  Sends the message to the specified recipients.
### Deprecated Methods
- [func resolveRecipients(for: INSendMessageIntent, with: ([INPersonResolutionResult]) -> Void)](./insendmessageintenthandling/resolverecipients%28for,with%29-2yejx.md)
  Resolves the recipients of the message.
- [func resolveGroupName(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./insendmessageintenthandling/resolvegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INMessagesDomainHandling](./inmessagesdomainhandling.md)

## See Also

### Sending a Message
- [class INSendMessageIntent](./insendmessageintent.md)
  A request to send a message to the designated recipients.
- [class INSendMessageIntentResponse](./insendmessageintentresponse.md)
  Your app’s response to a send message intent.
- [enum INOutgoingMessageType](./inoutgoingmessagetype.md)
  The format of the message.
- [class INSendMessageAttachment](./insendmessageattachment.md)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](./insendmessageintentdonationmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling)*