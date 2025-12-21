# RCSService.Business

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure containing details about a business.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Business
```

#### Overview

This structure and its supporting types correspond to the “chatbot” JSON schemas defined by the RCS specification.

To get information about a business, use the [`CellularServiceID`](cellularserviceid.md) and [`RCSHandle`](rcshandle.md) from an [`RCSMessage`](rcsmessage.md) you receive in the RCS service’s [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md), then call [`businessInformation(for:)`](rcsservice/businessinformation(for:).md) on the RCS service, which returns an instance of the `Business` type.

Your app receives [`RCSService.Business.Card`](rcsservice/business/card.md) and [`RCSService.Business.CardCarousel`](rcsservice/business/cardcarousel.md) instances as cases of the [`RCSMessage.Content`](rcsmessage/content-swift.enum.md) enumeration in messages received from the RCS service’s [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md) asynchronous sequence. Use the properties of the received cards to display content sent from the business to the person using your app.

An [`RCSService.IncomingMessageNotification`](rcsservice/incomingmessagenotification.md) instance may contain [`RCSService.Business.Suggestion`](rcsservice/business/suggestion.md) instances in its [`suggestions`](rcsservice/incomingmessagenotification/suggestions.md) array. These suggestions can include a [`RCSService.Business.SuggestedAction`](rcsservice/business/suggestedaction.md) or a [`RCSService.Business.SuggestedReply`](rcsservice/business/suggestedreply.md). Act on these, then call [`sendSuggestionResponse(_:)`](rcsservice/sendsuggestionresponse(_:).md) on the RCS service.

## Topics

### Accessing business identity information
- [let description: String?](rcsservice/business/description.md)
  Description for business.
- [let providerName: String?](rcsservice/business/providername.md)
  Name of business provider.
- [let organizationNames: [RCSService.Business.OrganizationName]](rcsservice/business/organizationnames.md)
  Array of names specified by business.
- [RCSService.Business.OrganizationName](rcsservice/business/organizationname.md)
  Structure containing details about a business’ name.
- [let categoryNames: [String]](rcsservice/business/categorynames.md)
  Array of category names which can be used to filter a list of businesses.
### Accessing business contact information
- [let communicationAddress: RCSService.Business.CommunicationAddress?](rcsservice/business/communicationaddress-swift.property.md)
  Communication details of business.
- [RCSService.Business.CommunicationAddress](rcsservice/business/communicationaddress-swift.struct.md)
  Structure containing a business’ communication details.
- [let addressEntries: [RCSService.Business.AddressEntry]](rcsservice/business/addressentries.md)
  Array of business’ address locations.
- [RCSService.Business.AddressEntry](rcsservice/business/addressentry.md)
  Structure containing address details provided by a business.
- [let emailAddress: String?](rcsservice/business/emailaddress.md)
  Service email address.
- [let websiteURL: URL?](rcsservice/business/websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](rcsservice/business/verificationdetails-swift.property.md)
  Verification information about business.
- [RCSService.Business.VerificationDetails](rcsservice/business/verificationdetails-swift.struct.md)
  Structure containing verification details of a business.
### Accessing terms and conditions
- [let termsAndConditionsURL: URL?](rcsservice/business/termsandconditionsurl.md)
  URL for business’ terms and conditions.
### Accessing display information
- [var themeColor: CGColor?](rcsservice/business/themecolor.md)
  Theme color to apply to conversation view.
- [let backgroundImageURL: URL?](rcsservice/business/backgroundimageurl.md)
  Background image to apply to business information page.
- [let styleSheetTemplateURL: URL?](rcsservice/business/stylesheettemplateurl.md)
  URL referring to a CSS template to be used in rich cards sent by business.
- [let persistentMenu: RCSService.Business.Menu?](rcsservice/business/persistentmenu.md)
  Persistent menu with a nested collection of suggested replies and suggested actions.
- [RCSService.Business.Menu](rcsservice/business/menu.md)
  A menu provided by business.
### Accessing media entries
- [let mediaEntries: [RCSService.Business.MediaEntry]](rcsservice/business/mediaentries.md)
  Media entries provided by business.
- [RCSService.Business.MediaEntry](rcsservice/business/mediaentry.md)
  Structure containing media details provided by a business.
### Accessing version information
- [let version: String?](rcsservice/business/version.md)
  Version of contents.
### Supporting types
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
### Enumerations
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func businessInformation(for: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?](rcsservice/businessinformation(for:).md)
  Requests business information for a specified handle.
- [RCSService.BusinessInformationRequest](rcsservice/businessinformationrequest.md)
  A structure representing a request to retrieve information about a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business)*