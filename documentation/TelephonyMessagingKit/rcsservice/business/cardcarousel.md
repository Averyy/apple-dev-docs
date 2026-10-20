# RCSService.Business.CardCarousel

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing a card carousel.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct CardCarousel
```

## Topics

### Accessing card carousel properties
- [let width: RCSService.Business.Card.Width](./cardcarousel/width.md)
  Width of cards.
- [RCSService.Business.Card.Width](./card/width.md)
  Enumeration specifying the width of a card.
- [let titleFontStyle: RCSService.Business.Card.FontStyle](./cardcarousel/titlefontstyle.md)
  Style to use for title.
- [let descriptionFontStyle: RCSService.Business.Card.FontStyle](./cardcarousel/descriptionfontstyle.md)
  Style to use for description.
- [RCSService.Business.Card.FontStyle](./card/fontstyle.md)
  Structure representing font style attributes in a card.
- [let styleSheetURL: URL?](./cardcarousel/stylesheeturl.md)
  A URL to a CSS for the rendering of the cards
- [let contents: [RCSService.Business.Card.Content]](./cardcarousel/contents.md)
  Contents of card carousel.
- [RCSService.Business.Card.Content](./card/content-swift.struct.md)
  Structure containing the contents of a card.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.Business.Card](./card.md)
  Structure representing a standalone card.
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/cardcarousel)*