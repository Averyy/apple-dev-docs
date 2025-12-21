# RCSService.Business.Card

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing a standalone card.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Card
```

## Topics

### Accessing card properties
- [let content: RCSService.Business.Card.Content](rcsservice/business/card/content-swift.property.md)
  Content of card.
- [RCSService.Business.Card.Content](rcsservice/business/card/content-swift.struct.md)
  Structure containing the contents of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](rcsservice/business/card/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](rcsservice/business/card/fontstyle.md)
  Structure representing font style attributes in a card.
- [let imageAlignment: RCSService.Business.Card.ImageAlignment?](rcsservice/business/card/imagealignment-swift.property.md)
  Image alignment of card.
- [RCSService.Business.Card.ImageAlignment](rcsservice/business/card/imagealignment-swift.enum.md)
  Image alignment within a card.
- [let orientation: RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.property.md)
  The orientation to use when displaying the card.
- [RCSService.Business.Card.Orientation](rcsservice/business/card/orientation-swift.enum.md)
  Enumeration indicating the orientation of a card.
- [let styleSheetURL: URL?](rcsservice/business/card/stylesheeturl.md)
  A URL to a CSS for the rendering of the card.
### Supporting types
- [RCSService.Business.Card.Width](rcsservice/business/card/width.md)
  Enumeration specifying the width of a card.
- [RCSService.Business.Card.Media](rcsservice/business/card/media.md)
  Structure containing information about media in a card.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.Business.CardCarousel](rcsservice/business/cardcarousel.md)
  Structure representing a card carousel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card)*