# INOutgoingMessageType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

The format of the message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum INOutgoingMessageType
```

```c
enum INOutgoingMessageType : NSInteger;
```

## Topics

### Message Types
- [INOutgoingMessageType.outgoingMessageText](./inoutgoingmessagetype/outgoingmessagetext.md)
  Plain text.
- [INOutgoingMessageType.outgoingMessageAudio](./inoutgoingmessagetype/outgoingmessageaudio.md)
  An audio recording.
- [INOutgoingMessageType.unknown](./inoutgoingmessagetype/unknown.md)
  An unspecified message format.
### Initializers
- [init?(rawValue: Int)](./inoutgoingmessagetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sending a Message
- [protocol INSendMessageIntentHandling](./insendmessageintenthandling.md)
  An interface to handle sending messages to one or more designated users.
- [class INSendMessageIntent](./insendmessageintent.md)
  A request to send a message to the designated recipients.
- [class INSendMessageIntentResponse](./insendmessageintentresponse.md)
  Your app’s response to a send message intent.
- [class INSendMessageAttachment](./insendmessageattachment.md)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](./insendmessageintentdonationmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inoutgoingmessagetype)*