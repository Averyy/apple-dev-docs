# RCSService.Business.TelephoneDetails

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing the telephone number details provided by a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct TelephoneDetails
```

## Topics

### Accessing telephone details
- [let label: String](./telephonedetails/label.md)
  The label for the phone number.
- [let phoneNumber: String](./telephonedetails/phonenumber.md)
  Phone number provided by business.
- [let phoneNumberType: String](./telephonedetails/phonenumbertype.md)
  A string to represent the type of phone number; for example, “Work”.

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
- [RCSService.Business.URIEntry](./urientry.md)
  Structure containing details of a URI provided by a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/telephonedetails)*