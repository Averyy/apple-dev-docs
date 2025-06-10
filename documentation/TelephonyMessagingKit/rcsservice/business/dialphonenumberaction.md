# RCSService.Business.DialPhoneNumberAction

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Suggested action to dial a phone number.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct DialPhoneNumberAction
```

## Topics

### Accessing action properties
- [let phoneNumber: String](rcsservice/business/dialphonenumberaction/phonenumber.md)
  The phone number to dial.
- [let fallbackURL: URL?](rcsservice/business/dialphonenumberaction/fallbackurl.md)
  Fallback URL to use when unable to perform operation.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/dialphonenumberaction/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/dialphonenumberaction/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing actions
- [static func == (RCSService.Business.DialPhoneNumberAction, RCSService.Business.DialPhoneNumberAction) -> Bool](rcsservice/business/dialphonenumberaction/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/dialphonenumberaction/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.Business.Card](rcsservice/business/card.md)
  Structure representing a standalone card.
- [RCSService.Business.CardCarousel](rcsservice/business/cardcarousel.md)
  Structure representing a card carousel.
- [RCSService.Business.ComposeRecordingAction](rcsservice/business/composerecordingaction.md)
  Compose a draft message with a media recording.
- [RCSService.Business.ComposeTextAction](rcsservice/business/composetextaction.md)
  Compose a draft text message.
- [RCSService.Business.CreateCalendarEventAction](rcsservice/business/createcalendareventaction.md)
  Structure representing an action to create a calendar event.
- [RCSService.Business.Media](rcsservice/business/media.md)
  Structure containing media information provided by a business.
- [RCSService.Business.OpenURLAction](rcsservice/business/openurlaction.md)
  Suggested action to open a URL.
- [RCSService.Business.ShowLocationAction](rcsservice/business/showlocationaction.md)
  Shows a location on a map.
- [RCSService.Business.SuggestedAction](rcsservice/business/suggestedaction.md)
  Suggested action sent by a business.
- [RCSService.Business.SuggestedReply](rcsservice/business/suggestedreply.md)
  Suggested reply in response to a business message.
- [RCSService.Business.TelephoneDetails](rcsservice/business/telephonedetails.md)
  Structure containing the telephone number details provided by a business.
- [RCSService.Business.URIEntry](rcsservice/business/urientry.md)
  Structure containing details of a URI provided by a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/dialphonenumberaction)*