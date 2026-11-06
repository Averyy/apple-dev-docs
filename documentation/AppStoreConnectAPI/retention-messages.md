# Retention messages

**Framework**: App Store Connect API  
**Role**: API Collection

Create and manage the messages people see when they start to cancel an auto-renewable subscription.

## Overview

The `retentionMessages` resource represents a message that gives people a reason to stay subscribed when they start to cancel an auto-renewable subscription. Each retention message belongs to an app, and you assign it to one or more of the app’s subscriptions. Use it to:

- Read retention message information, including its versions and the subscriptions that use it.
- Create a retention message for an app.
- Assign a retention message to a subscription.
- Delete a retention message you no longer need.

A retention message holds its content in versions that you submit to App Review. To write the message content, see [Retention message versions](./retention-message-versions.md) and [Retention message localizations](./retention-message-localizations.md). To present a discount alongside the message, see [Retention offers](./retention-offers.md). To choose which message people see in real time from your server, see [Retention Messaging API](../RetentionMessaging/RetentionMessaging.md).

> **Note**:  A subscription has at most one retention message. Assigning a retention message to a subscription replaces the subscription’s existing retention message.

## Topics

### Essentials
- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)
  Create a retention message, write its localized content, and assign it and any retention offers to a subscription.
### Getting retention messages
- [Read a retention message](./get-v1-retentionmessages-_id_.md)
  Read details about a specific retention message.
- [List versions for a retention message](./get-v1-retentionmessages-_id_-versions.md)
  Get a list of versions for a specific retention message.
- [List version IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-versions.md)
  Get a list of version IDs for a specific retention message.
- [List subscriptions for a retention message](./get-v1-retentionmessages-_id_-subscriptions.md)
  Get a list of the auto-renewable subscriptions that use a specific retention message.
- [List subscription IDs for a retention message](./get-v1-retentionmessages-_id_-relationships-subscriptions.md)
  Get a list of the subscription IDs that use a specific retention message.
- [List retention messages for an app](./get-v1-apps-_id_-retentionmessages.md)
  Get a list of retention messages for a specific app.
- [List retention message IDs for an app](./get-v1-apps-_id_-relationships-retentionmessages.md)
  Get a list of retention message IDs for a specific app.
### Managing retention messages
- [Create a retention message](./post-v1-retentionmessages.md)
  Create a retention message for an app.
- [Delete a retention message](./delete-v1-retentionmessages-_id_.md)
  Delete a specific retention message.
### Assigning retention messages to subscriptions
- [Read the retention message for a subscription](./get-v1-subscriptions-_id_-retentionmessage.md)
  Get the retention message for a specific auto-renewable subscription.
- [Read the retention message ID for a subscription](./get-v1-subscriptions-_id_-relationships-retentionmessage.md)
  Get the retention message ID for a specific auto-renewable subscription.
- [Replace the retention message for a subscription](./patch-v1-subscriptions-_id_-relationships-retentionmessage.md)
  Assign a retention message to a specific auto-renewable subscription.
### Objects and types
- [object RetentionMessage](./retentionmessage.md)
  A message shown to people who start to cancel an auto-renewable subscription.
- [object RetentionMessageCreateRequest](./retentionmessagecreaterequest.md)
  The request body you use to create a retention message.
- [object RetentionMessageResponse](./retentionmessageresponse.md)
  The response body for endpoints that create or read a single retention message.
- [object RetentionMessagesResponse](./retentionmessagesresponse.md)
  The response body for endpoints that list retention messages.
- [object RetentionMessageVersionsResponse](./retentionmessageversionsresponse.md)
  The response body for endpoints that list retention message versions.
- [object RetentionMessageVersionsLinkagesResponse](./retentionmessageversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a retention message.
- [object RetentionMessageSubscriptionsLinkagesResponse](./retentionmessagesubscriptionslinkagesresponse.md)
  A response containing the resource identifiers of subscriptions that use a retention message.
- [object AppRetentionMessagesLinkagesResponse](./appretentionmessageslinkagesresponse.md)
  A response containing the resource identifiers of retention messages for an app.
- [object SubscriptionRetentionMessageLinkageRequest](./subscriptionretentionmessagelinkagerequest.md)
  The request body you use to assign a retention message to an auto-renewable subscription.
- [object SubscriptionRetentionMessageLinkageResponse](./subscriptionretentionmessagelinkageresponse.md)
  A response containing the resource identifier of the retention message for a subscription.

## See Also

### Managing retention messaging
- [Retention message versions](./retention-message-versions.md)
  Create versions of a retention message’s content and track their progress through App Review.
- [Retention message localizations](./retention-message-localizations.md)
  Create and manage the localized header and body text of a retention message version.
- [Retention offers](./retention-offers.md)
  Create and manage the discounted offers you present to people who start to cancel an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retention-messages)*