# RCSService.Business.Card

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing a standalone card.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Card
```

## Topics

### Accessing card properties
- [let content: RCSService.Business.Card.Content](./card/content-swift.property.md)
  Content of card.
- [RCSService.Business.Card.Content](./card/content-swift.struct.md)
  Structure containing the contents of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](./card/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](./card/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](./card/fontstyle.md)
  Structure representing font style attributes in a card.
- [let imageAlignment: RCSService.Business.Card.ImageAlignment?](./card/imagealignment-swift.property.md)
  Image alignment of card.
- [RCSService.Business.Card.ImageAlignment](./card/imagealignment-swift.enum.md)
  Image alignment within a card.
- [let orientation: RCSService.Business.Card.Orientation](./card/orientation-swift.property.md)
  The orientation to use when displaying the card.
- [RCSService.Business.Card.Orientation](./card/orientation-swift.enum.md)
  Enumeration indicating the orientation of a card.
- [let styleSheetURL: URL?](./card/stylesheeturl.md)
  A URL to a CSS for the rendering of the card.
### Supporting types
- [RCSService.Business.Card.Width](./card/width.md)
  Enumeration specifying the width of a card.
- [RCSService.Business.Card.Media](./card/media.md)
  Structure containing information about media in a card.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.Business.CardCarousel](./cardcarousel.md)
  Structure representing a card carousel.
- [RCSService.Business.ComposeRecordingAction](./composerecordingaction.md)
  Compose a draft message with a media recording.
- [RCSService.Business.ComposeTextAction](./composetextaction.md)
  Compose a draft text message.
- [RCSService.Business.CreateCalendarEventAction](./createcalendareventaction.md)
  Structure representing an action to create a calendar event.
- [RCSService.Business.DialPhoneNumberAction](./dialphonenumberaction.md)
  Suggested action to dial a phone number.
- [RCSService.Business.Media](./media.md)
  Structure containing media information provided by a business.
- [RCSService.Business.OpenURLAction](./openurlaction.md)
  Suggested action to open a URL.
- [RCSService.Business.ShowLocationAction](./showlocationaction.md)
  Shows a location on a map.
- [RCSService.Business.SuggestedAction](./suggestedaction.md)
  Suggested action sent by a business.
- [RCSService.Business.SuggestedReply](./suggestedreply.md)
  Suggested reply in response to a business message.
- [RCSService.Business.TelephoneDetails](./telephonedetails.md)
  Structure containing the telephone number details provided by a business.
- [RCSService.Business.URIEntry](./urientry.md)
  Structure containing details of a URI provided by a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card)*