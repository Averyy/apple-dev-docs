# INSendMessageIntentDonationMetadata

**Framework**: Intents  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class INSendMessageIntentDonationMetadata
```

```objc
@interface INSendMessageIntentDonationMetadata : INIntentDonationMetadata
```

## Topics

### Initializers
- [init()](./insendmessageintentdonationmetadata/init%28%29.md)
### Instance Properties
- [var isReplyToCurrentUser: Bool](./insendmessageintentdonationmetadata/isreplytocurrentuser.md)
- [var mentionsCurrentUser: Bool](./insendmessageintentdonationmetadata/mentionscurrentuser.md)
- [var notifyRecipientAnyway: Bool](./insendmessageintentdonationmetadata/notifyrecipientanyway.md)
- [var recipientCount: Int](./insendmessageintentdonationmetadata/recipientcount.md)

## Relationships

### Inherits From
- [INIntentDonationMetadata](./inintentdonationmetadata.md)
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
- [class INSendMessageIntentResponse](./insendmessageintentresponse.md)
  Your app’s response to a send message intent.
- [enum INOutgoingMessageType](./inoutgoingmessagetype.md)
  The format of the message.
- [class INSendMessageAttachment](./insendmessageattachment.md)
  A file to include in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentdonationmetadata)*