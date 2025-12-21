# RCSMessage.Content

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration of the RCS message content types supported by the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Content
```

#### Overview

The types that are associated values in this enumeration’s cases contain properties unique to their respective content types. For example, [`RCSMessage.Text`](rcsmessage/text.md) content contains a [`body`](rcsmessage/text/body.md) string, while [`RCSMessage.GeolocationPush`](rcsmessage/geolocationpush.md) content has a [`latitude`](rcsmessage/geolocationpush/latitude.md) and [`longitude`](rcsmessage/geolocationpush/longitude.md).

## Topics

### Working with text content
- [RCSMessage.Content.text(_:)](rcsmessage/content-swift.enum/text(_:).md)
  A content type for text content.
- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
### Working with file transfers
- [case fileTransfer(RCSMessage.FileTransfer)](rcsmessage/content-swift.enum/filetransfer(_:).md)
  A content type for file transfer content.
- [RCSMessage.FileTransfer](rcsmessage/filetransfer.md)
  A structure that represents file transfer content in an RCS message.
### Working with geolocation pushes
- [case geolocationPush(RCSMessage.GeolocationPush)](rcsmessage/content-swift.enum/geolocationpush(_:).md)
  A content type for geolocation push content.
- [RCSMessage.GeolocationPush](rcsmessage/geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
### Working with composing indicators
- [case composingIndicator(RCSMessage.ComposingIndicator)](rcsmessage/content-swift.enum/composingindicator(_:).md)
  A content type for composing indicator content.
- [RCSMessage.ComposingIndicator](rcsmessage/composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
### Working with disposition notifications
- [case dispositionNotification(RCSMessage.DispositionNotification)](rcsmessage/content-swift.enum/dispositionnotification(_:).md)
  A content type for disposition notification content.
- [RCSMessage.DispositionNotification](rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
### Working with business messages
- [case businessCard(RCSService.Business.Card)](rcsmessage/content-swift.enum/businesscard(_:).md)
  A content type for business card content.
- [RCSService.Business.Card](rcsservice/business/card.md)
  Structure representing a standalone card.
- [case businessCardCarousel(RCSService.Business.CardCarousel)](rcsmessage/content-swift.enum/businesscardcarousel(_:).md)
  A content type for business card carousel content.
- [RCSService.Business.CardCarousel](rcsservice/business/cardcarousel.md)
  Structure representing a card carousel.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: RCSMessage.Content](rcsmessage/content-swift.property.md)
  The content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/content-swift.enum)*