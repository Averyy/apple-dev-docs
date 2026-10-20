# RCSMessage.Content

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the RCS message content types supported by the system.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Content
```

#### Overview

The types that are associated values in this enumeration’s cases contain properties unique to their respective content types. For example, [`RCSMessage.Text`](./text.md) content contains a [`body`](./text/body.md) string, while [`RCSMessage.GeolocationPush`](./geolocationpush.md) content has a [`latitude`](./geolocationpush/latitude.md) and [`longitude`](./geolocationpush/longitude.md).

## Topics

### Working with text content
- [RCSMessage.Content.text(_:)](./content-swift.enum/text%28_%29.md)
  A content type for text content.
- [RCSMessage.Text](./text.md)
  A structure that represents text content in an RCS message.
### Working with file transfers
- [case fileTransfer(RCSMessage.FileTransfer)](./content-swift.enum/filetransfer%28_%29.md)
  A content type for file transfer content.
- [RCSMessage.FileTransfer](./filetransfer.md)
  A structure that represents file transfer content in an RCS message.
### Working with geolocation pushes
- [case geolocationPush(RCSMessage.GeolocationPush)](./content-swift.enum/geolocationpush%28_%29.md)
  A content type for geolocation push content.
- [RCSMessage.GeolocationPush](./geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
### Working with composing indicators
- [case composingIndicator(RCSMessage.ComposingIndicator)](./content-swift.enum/composingindicator%28_%29.md)
  A content type for composing indicator content.
- [RCSMessage.ComposingIndicator](./composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
### Working with disposition notifications
- [case dispositionNotification(RCSMessage.DispositionNotification)](./content-swift.enum/dispositionnotification%28_%29.md)
  A content type for disposition notification content.
- [RCSMessage.DispositionNotification](./dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
### Working with business messages
- [case businessCard(RCSService.Business.Card)](./content-swift.enum/businesscard%28_%29.md)
  A content type for business card content.
- [RCSService.Business.Card](../rcsservice/business/card.md)
  Structure representing a standalone card.
- [case businessCardCarousel(RCSService.Business.CardCarousel)](./content-swift.enum/businesscardcarousel%28_%29.md)
  A content type for business card carousel content.
- [RCSService.Business.CardCarousel](../rcsservice/business/cardcarousel.md)
  Structure representing a card carousel.
### Enumeration Cases
- [case customReaction(RCSMessage.CustomReaction)](./content-swift.enum/customreaction%28_%29.md)
  A content type for custom reaction content.
- [case reaction(RCSMessage.Reaction)](./content-swift.enum/reaction%28_%29.md)
  A content type for reaction content.
- [RCSMessage.Content.reply(_:)](./content-swift.enum/reply%28_%29.md)
  A content type for reply content.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing message content
- [let content: RCSMessage.Content](./content-swift.property.md)
  The content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/content-swift.enum)*