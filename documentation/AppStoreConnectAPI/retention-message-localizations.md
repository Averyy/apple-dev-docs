# Retention message localizations

**Framework**: App Store Connect API  
**Role**: API Collection

Create and manage the localized header and body text of a retention message version.

## Overview

The `retentionMessageLocalizations` resource represents the header and body text of a retention message version for a single locale. Use it to:

- Read the localized text of a retention message version.
- Create a localization for a new locale.
- Update a localization’s header and body text.
- Delete a localization you no longer need.

Each localization belongs to a retention message version. To create a version, see [Retention message versions](./retention-message-versions.md). For information about choosing retention messages in real time from your server, see [Retention Messaging API](../RetentionMessaging/RetentionMessaging.md).

> **Note**:  You can’t change a localization’s locale after you create it. To provide text for a different locale, create a new localization.

## Topics

### Getting retention message localizations
- [Read a retention message localization](./get-v1-retentionmessagelocalizations-_id_.md)
  Read details about a specific retention message localization.
### Managing retention message localizations
- [Create a retention message localization](./post-v1-retentionmessagelocalizations.md)
  Create a localization of the header and body text for a retention message version.
- [Modify a retention message localization](./patch-v1-retentionmessagelocalizations-_id_.md)
  Update the header and body text of a specific retention message localization.
- [Delete a retention message localization](./delete-v1-retentionmessagelocalizations-_id_.md)
  Delete a specific retention message localization.
### Objects and types
- [object RetentionMessageLocalization](./retentionmessagelocalization.md)
  The header and body text of a retention message version for a single locale.
- [object RetentionMessageLocalizationCreateRequest](./retentionmessagelocalizationcreaterequest.md)
  The request body you use to create a retention message localization.
- [object RetentionMessageLocalizationUpdateRequest](./retentionmessagelocalizationupdaterequest.md)
  The request body you use to update a retention message localization.
- [object RetentionMessageLocalizationResponse](./retentionmessagelocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single retention message localization.

## See Also

### Managing retention messaging
- [Retention messages](./retention-messages.md)
  Create and manage the messages people see when they start to cancel an auto-renewable subscription.
- [Retention message versions](./retention-message-versions.md)
  Create versions of a retention message’s content and track their progress through App Review.
- [Retention offers](./retention-offers.md)
  Create and manage the discounted offers you present to people who start to cancel an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retention-message-localizations)*