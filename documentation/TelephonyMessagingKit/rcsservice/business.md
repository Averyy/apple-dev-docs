# RCSService.Business

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure containing details about a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct Business
```

## Overview

This structure and its supporting types correspond to the “chatbot” JSON schemas defined by the RCS specification.

To get information about a business, use the [`CellularServiceID`](../cellularserviceid.md) and [`RCSHandle`](../rcshandle.md) from an [`RCSMessage`](../rcsmessage.md) you receive in the RCS service’s [`incomingMessageNotifications`](./incomingmessagenotifications.md), then call [`businessInformation(for:)`](./businessinformation%28for%29.md) on the RCS service, which returns an instance of the `Business` type.

Your app receives [`RCSService.Business.Card`](./business/card.md) and [`RCSService.Business.CardCarousel`](./business/cardcarousel.md) instances as cases of the [`RCSMessage.Content`](../rcsmessage/content-swift.enum.md) enumeration in messages received from the RCS service’s [`incomingMessageNotifications`](./incomingmessagenotifications.md) asynchronous sequence. Use the properties of the received cards to display content sent from the business to the person using your app.

An [`RCSService.IncomingMessageNotification`](./incomingmessagenotification.md) instance may contain [`RCSService.Business.Suggestion`](./business/suggestion.md) instances in its [`suggestions`](./incomingmessagenotification/suggestions.md) array. These suggestions can include a [`RCSService.Business.SuggestedAction`](./business/suggestedaction.md) or a [`RCSService.Business.SuggestedReply`](./business/suggestedreply.md). Act on these, then call [`sendSuggestionResponse(_:)`](./sendsuggestionresponse%28_%29.md) on the RCS service.

## Topics

### Accessing business identity information
- [let description: String?](./business/description.md)
  Description for business.
- [let providerName: String?](./business/providername.md)
  Name of business provider.
- [let organizationNames: [RCSService.Business.OrganizationName]](./business/organizationnames.md)
  Array of names specified by business.
- [RCSService.Business.OrganizationName](./business/organizationname.md)
  Structure containing details about a business’ name.
- [let categoryNames: [String]](./business/categorynames.md)
  Array of category names which can be used to filter a list of businesses.
### Accessing business contact information
- [let communicationAddress: RCSService.Business.CommunicationAddress?](./business/communicationaddress-swift.property.md)
  Communication details of business.
- [RCSService.Business.CommunicationAddress](./business/communicationaddress-swift.struct.md)
  Structure containing a business’ communication details.
- [let addressEntries: [RCSService.Business.AddressEntry]](./business/addressentries.md)
  Array of business’ address locations.
- [RCSService.Business.AddressEntry](./business/addressentry.md)
  Structure containing address details provided by a business.
- [let emailAddress: String?](./business/emailaddress.md)
  Service email address.
- [let websiteURL: URL?](./business/websiteurl.md)
  URL for business’ website.
- [let verificationDetails: RCSService.Business.VerificationDetails?](./business/verificationdetails-swift.property.md)
  Verification information about business.
- [RCSService.Business.VerificationDetails](./business/verificationdetails-swift.struct.md)
  Structure containing verification details of a business.
### Accessing terms and conditions
- [let termsAndConditionsURL: URL?](./business/termsandconditionsurl.md)
  URL for business’ terms and conditions.
### Accessing display information
- [var themeColor: CGColor?](./business/themecolor.md)
  Theme color to apply to conversation view.
- [let backgroundImageURL: URL?](./business/backgroundimageurl.md)
  Background image to apply to business information page.
- [let styleSheetTemplateURL: URL?](./business/stylesheettemplateurl.md)
  URL referring to a CSS template to be used in rich cards sent by business.
- [let persistentMenu: RCSService.Business.Menu?](./business/persistentmenu.md)
  Persistent menu with a nested collection of suggested replies and suggested actions.
- [RCSService.Business.Menu](./business/menu.md)
  A menu provided by business.
### Accessing media entries
- [let mediaEntries: [RCSService.Business.MediaEntry]](./business/mediaentries.md)
  Media entries provided by business.
- [RCSService.Business.MediaEntry](./business/mediaentry.md)
  Structure containing media details provided by a business.
### Accessing version information
- [let version: String?](./business/version.md)
  Version of contents.
### Supporting types
- [RCSService.Business.Card](./business/card.md)
  Structure representing a standalone card.
- [RCSService.Business.CardCarousel](./business/cardcarousel.md)
  Structure representing a card carousel.
- [RCSService.Business.ComposeRecordingAction](./business/composerecordingaction.md)
  Compose a draft message with a media recording.
- [RCSService.Business.ComposeTextAction](./business/composetextaction.md)
  Compose a draft text message.
- [RCSService.Business.CreateCalendarEventAction](./business/createcalendareventaction.md)
  Structure representing an action to create a calendar event.
- [RCSService.Business.DialPhoneNumberAction](./business/dialphonenumberaction.md)
  Suggested action to dial a phone number.
- [RCSService.Business.Media](./business/media.md)
  Structure containing media information provided by a business.
- [RCSService.Business.OpenURLAction](./business/openurlaction.md)
  Suggested action to open a URL.
- [RCSService.Business.ShowLocationAction](./business/showlocationaction.md)
  Shows a location on a map.
- [RCSService.Business.SuggestedAction](./business/suggestedaction.md)
  Suggested action sent by a business.
- [RCSService.Business.SuggestedReply](./business/suggestedreply.md)
  Suggested reply in response to a business message.
- [RCSService.Business.TelephoneDetails](./business/telephonedetails.md)
  Structure containing the telephone number details provided by a business.
- [RCSService.Business.URIEntry](./business/urientry.md)
  Structure containing details of a URI provided by a business.
### Structures
- [RCSService.Business.Capabilities](./business/capabilities-swift.struct.md)
  Structure containing details about a business’ capabilities.
- [RCSService.Business.WelcomeMessage](./business/welcomemessage-swift.struct.md)
  Structure containing details about a business’ welcome message.
### Instance Properties
- [let capabilities: RCSService.Business.Capabilities?](./business/capabilities-swift.property.md)
- [let welcomeMessage: RCSService.Business.WelcomeMessage?](./business/welcomemessage-swift.property.md)
### Enumerations
- [RCSService.Business.Feature](./business/feature.md)
  Enumeration representing an RCS service feature supported by a business.
- [RCSService.Business.Suggestion](./business/suggestion.md)
  Enumeration representing a suggestion from a business.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving business information
- [func businessInformation(for: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?](./businessinformation%28for%29.md)
  Requests business information for a specified handle.
- [RCSService.BusinessInformationRequest](./businessinformationrequest.md)
  A structure representing a request to retrieve information about a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business)*