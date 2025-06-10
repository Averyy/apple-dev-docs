# RCSService.Business.CardCarousel

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing a card carousel.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CardCarousel
```

## Topics

### Accessing card carousel properties
- [let width: RCSService.Business.Card.Width](rcsservice/business/cardcarousel/width.md)
  Width of cards.
- [RCSService.Business.Card.Width](rcsservice/business/card/width.md)
  Enumeration specifying the width of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/cardcarousel/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/cardcarousel/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle.md)
  Structure representing font style attributes in a card.
- [let styleSheetURL: URL?](rcsservice/business/cardcarousel/stylesheeturl.md)
  A URL to a CSS for the rendering of the cards
- [let contents: [RCSService.Business.Card.Content]](rcsservice/business/cardcarousel/contents.md)
  Contents of card carousel.
- [RCSService.Business.Card.Content](rcsservice/business/card/content-swift.struct.md)
  Structure containing the contents of a card.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/cardcarousel/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/cardcarousel/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing card carousels
- [static func == (RCSService.Business.CardCarousel, RCSService.Business.CardCarousel) -> Bool](rcsservice/business/cardcarousel/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/cardcarousel/equatable-implementations.md)

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
- [RCSService.Business.ComposeRecordingAction](rcsservice/business/composerecordingaction.md)
  Compose a draft message with a media recording.
- [RCSService.Business.ComposeTextAction](rcsservice/business/composetextaction.md)
  Compose a draft text message.
- [RCSService.Business.CreateCalendarEventAction](rcsservice/business/createcalendareventaction.md)
  Structure representing an action to create a calendar event.
- [RCSService.Business.DialPhoneNumberAction](rcsservice/business/dialphonenumberaction.md)
  Suggested action to dial a phone number.
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/cardcarousel)*