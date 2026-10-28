# INSendMessageAttachment

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A file to include in a message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INSendMessageAttachment
```

```objc
@interface INSendMessageAttachment : NSObject
```

## Overview

When the type of a message is [`INOutgoingMessageType.outgoingMessageAudio`](./inoutgoingmessagetype/outgoingmessageaudio.md), the intent includes the audio recording as an [`INSendMessageAttachment`](./insendmessageattachment.md).

## Topics

### Creating an Audio Attachment
- [init(audioMessageFile: INFile)](./insendmessageattachment/init%28audiomessagefile%29.md)
  Creates a message attachment with an audio file.
### Accessing the Message File
- [var audioMessageFile: INFile?](./insendmessageattachment/audiomessagefile.md)
  The attachment’s recorded message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [class INSendMessageIntentDonationMetadata](./insendmessageintentdonationmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageattachment)*