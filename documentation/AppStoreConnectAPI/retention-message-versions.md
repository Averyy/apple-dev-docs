# Retention message versions

**Framework**: App Store Connect API  
**Role**: API Collection

Create versions of a retention message’s content and track their progress through App Review.

## Overview

The `retentionMessageVersions` resource represents a version of a retention message’s content that you submit to App Review. A version contains localized header and body text, and can include an image from your app’s asset library. Use it to:

- Read a retention message version, including its review state, localizations, and image placement.
- Create a new version of a retention message.

To add localized text to a version, see [Retention message localizations](./retention-message-localizations.md). To submit a version for review, add it to a review submission as a review submission item. For more information, see [Review submission items](./review-submission-items.md). The `state` attribute of [`RetentionMessageVersion`](./retentionmessageversion.md) tracks its progress through review.

For information about choosing retention messages in real time from your server, see [Retention Messaging API](../RetentionMessaging/RetentionMessaging.md).

> **Note**:  You can’t modify or delete a retention message version after you create it.

## Topics

### Getting retention message versions
- [Read a retention message version](./get-v1-retentionmessageversions-_id_.md)
  Read details about a specific retention message version, including its review state.
- [List localizations for a retention message version](./get-v1-retentionmessageversions-_id_-localizations.md)
  Get a list of localizations for a specific retention message version.
- [List localization IDs for a retention message version](./get-v1-retentionmessageversions-_id_-relationships-localizations.md)
  Get a list of localization IDs for a specific retention message version.
- [Read the placement for a retention message version](./get-v1-retentionmessageversions-_id_-placement.md)
  Get the image placement for a specific retention message version.
- [Read the placement ID for a retention message version](./get-v1-retentionmessageversions-_id_-relationships-placement.md)
  Get the image placement ID for a specific retention message version.
### Creating retention message versions
- [Create a retention message version](./post-v1-retentionmessageversions.md)
  Create a version of a retention message to submit to App Review.
### Objects and types
- [object RetentionMessageVersion](./retentionmessageversion.md)
  A version of a retention message’s content that you submit to App Review.
- [object RetentionMessageVersionCreateRequest](./retentionmessageversioncreaterequest.md)
  The request body you use to create a retention message version.
- [object RetentionMessageVersionResponse](./retentionmessageversionresponse.md)
  The response body for endpoints that create or read a single retention message version.
- [object RetentionMessageLocalizationsResponse](./retentionmessagelocalizationsresponse.md)
  The response body for endpoints that list retention message localizations.
- [object RetentionMessageVersionLocalizationsLinkagesResponse](./retentionmessageversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of localizations for a retention message version.
- [object RetentionMessageVersionPlacementLinkageResponse](./retentionmessageversionplacementlinkageresponse.md)
  A response containing the resource identifier of the image placement for a retention message version.

## See Also

### Managing retention messaging
- [Retention messages](./retention-messages.md)
  Create and manage the messages people see when they start to cancel an auto-renewable subscription.
- [Retention message localizations](./retention-message-localizations.md)
  Create and manage the localized header and body text of a retention message version.
- [Retention offers](./retention-offers.md)
  Create and manage the discounted offers you present to people who start to cancel an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retention-message-versions)*