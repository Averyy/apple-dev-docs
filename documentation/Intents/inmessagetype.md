# INMessageType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the kinds of content a message can contain.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INMessageType
```

```c
enum INMessageType : NSInteger;
```

## Topics

### General Types
- [INMessageType.unspecified](./inmessagetype/unspecified.md)
  The message content isn’t specified.
- [INMessageType.text](./inmessagetype/text.md)
  The message content is text-based.
- [INMessageType.animoji](./inmessagetype/animoji.md)
  The message content is an animoji.
- [INMessageType.audio](./inmessagetype/audio.md)
  The message contains audio content.
- [INMessageType.digitalTouch](./inmessagetype/digitaltouch.md)
  The message contains digital touch content.
- [INMessageType.handwriting](./inmessagetype/handwriting.md)
  The message contains handwritten content.
- [INMessageType.sticker](./inmessagetype/sticker.md)
  The message contains sticker content.
- [INMessageType.link](./inmessagetype/link.md)
  The message contains link content.
- [INMessageType.file](./inmessagetype/file.md)
  The message contains a file.
- [INMessageType.activitySnippet](./inmessagetype/activitysnippet.md)
  The message contains an activity snippet.
### Media Types
- [INMessageType.mediaCalendar](./inmessagetype/mediacalendar.md)
  Media content containing calendar data.
- [INMessageType.mediaLocation](./inmessagetype/medialocation.md)
  Media content containing location data.
- [INMessageType.mediaAddressCard](./inmessagetype/mediaaddresscard.md)
  Media content containing an address card.
- [INMessageType.mediaImage](./inmessagetype/mediaimage.md)
  Media content containing an image.
- [INMessageType.mediaVideo](./inmessagetype/mediavideo.md)
  Media content containing video.
- [INMessageType.mediaPass](./inmessagetype/mediapass.md)
  Media content containing PassKit data.
- [INMessageType.mediaAudio](./inmessagetype/mediaaudio.md)
  Media content containing audio.
### Payment Types
- [INMessageType.paymentNote](./inmessagetype/paymentnote.md)
  Content indicating the message contains notes about a payment.
- [INMessageType.paymentRequest](./inmessagetype/paymentrequest.md)
  Content indicating the message contains payment request information.
- [INMessageType.paymentSent](./inmessagetype/paymentsent.md)
  Content indicating the message contains sent payment information.
### Tapback Types
- [INMessageType.tapbackLiked](./inmessagetype/tapbackliked.md)
  Content indicating that the user liked something.
- [INMessageType.tapbackDisliked](./inmessagetype/tapbackdisliked.md)
  Content indicating that the user disliked something.
- [INMessageType.tapbackEmphasized](./inmessagetype/tapbackemphasized.md)
  Content indicating that the user emphasized something.
- [INMessageType.tapbackLoved](./inmessagetype/tapbackloved.md)
  Content indicating that the user loved something.
- [INMessageType.tapbackQuestioned](./inmessagetype/tapbackquestioned.md)
  Content indicating that the user questioned something.
- [INMessageType.tapbackLaughed](./inmessagetype/tapbacklaughed.md)
  Content indicating that the user laughed at something.
### Enumeration Cases
- [INMessageType.mediaAnimatedImage](./inmessagetype/mediaanimatedimage.md)
- [INMessageType.reaction](./inmessagetype/reaction.md)
- [INMessageType.thirdPartyAttachment](./inmessagetype/thirdpartyattachment.md)
### Initializers
- [init?(rawValue: Int)](./inmessagetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Supplementary Attributes
- [var dateSent: Date?](./inmessage/datesent.md)
  The date and time the app sent the message to each recipient.
- [var groupName: INSpeakableString?](./inmessage/groupname.md)
  The name of the grouped conversation.
- [var messageType: INMessageType](./inmessage/messagetype.md)
  The type of content the message contains.
- [var serviceName: String?](./inmessage/servicename.md)
  The name of the service that delivers the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessagetype)*