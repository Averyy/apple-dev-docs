# Retention offers

**Framework**: App Store Connect API  
**Role**: API Collection

Create and manage the discounted offers you present to people who start to cancel an auto-renewable subscription.

## Overview

The `retentionOffers` resource represents a discounted offer for an auto-renewable subscription that you present alongside a retention message. You configure the offer’s duration, payment mode, eligibility rules, and a price for each territory. Use it to:

- Read retention offer information, including its prices.
- Create a retention offer for a subscription.
- Update an offer’s customer eligibility rules.
- Delete a retention offer you no longer need.
- Choose which offers to present with a subscription’s retention message.

Each retention offer has an offer identifier that you define, which identifies the offer in StoreKit. To create the message that accompanies an offer, see [Retention messages](./retention-messages.md). For information about choosing retention messages and offers in real time from your server, see [Retention Messaging API](../RetentionMessaging/RetentionMessaging.md).

> **Note**:  Creating a retention offer doesn’t present it to people. To present an offer with a subscription’s retention message, add the offer to the subscription’s retention message offers.

## Topics

### Getting retention offers
- [Read a retention offer](./get-v1-retentionoffers-_id_.md)
  Read details about a specific retention offer.
- [List prices for a retention offer](./get-v1-retentionoffers-_id_-prices.md)
  Get a list of territory-specific prices for a specific retention offer.
- [List price IDs for a retention offer](./get-v1-retentionoffers-_id_-relationships-prices.md)
  Get a list of price IDs for a specific retention offer.
- [List retention offers for a subscription](./get-v1-subscriptions-_id_-retentionoffers.md)
  Get a list of all retention offers for a specific auto-renewable subscription.
- [List retention offer IDs for a subscription](./get-v1-subscriptions-_id_-relationships-retentionoffers.md)
  Get a list of retention offer IDs for a specific auto-renewable subscription.
### Managing retention offers
- [Create a retention offer](./post-v1-retentionoffers.md)
  Create a retention offer for an auto-renewable subscription.
- [Modify a retention offer](./patch-v1-retentionoffers-_id_.md)
  Update the customer eligibility rules of a specific retention offer.
- [Delete a retention offer](./delete-v1-retentionoffers-_id_.md)
  Delete a specific retention offer.
### Choosing offers for a retention message
- [List retention message offers for a subscription](./get-v1-subscriptions-_id_-retentionmessageoffers.md)
  Get a list of the retention offers that appear with the retention message for a specific auto-renewable subscription.
- [List retention message offer IDs for a subscription](./get-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)
  Get a list of the offer IDs that appear with the retention message for a specific auto-renewable subscription.
- [Add retention message offers to a subscription](./post-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)
  Add retention offers to the retention message for a specific auto-renewable subscription.
- [Remove retention message offers from a subscription](./delete-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)
  Remove retention offers from the retention message for a specific auto-renewable subscription.
### Objects and types
- [object RetentionOffer](./retentionoffer.md)
  A discounted offer for an auto-renewable subscription that you present to people who start to cancel it.
- [object RetentionOfferCreateRequest](./retentionoffercreaterequest.md)
  The request body you use to create a retention offer.
- [object RetentionOfferUpdateRequest](./retentionofferupdaterequest.md)
  The request body you use to update a retention offer.
- [object RetentionOfferResponse](./retentionofferresponse.md)
  The response body for endpoints that create, read, or modify a single retention offer.
- [object RetentionOffersResponse](./retentionoffersresponse.md)
  The response body for endpoints that list retention offers.
- [object RetentionOfferPrice](./retentionofferprice.md)
  The territory-specific price point for a retention offer.
- [object RetentionOfferPriceInlineCreate](./retentionofferpriceinlinecreate.md)
  An inline object for specifying territory pricing when creating a retention offer.
- [object RetentionOfferPricesResponse](./retentionofferpricesresponse.md)
  The response body for endpoints that list retention offer prices.
- [object RetentionOfferPricesLinkagesResponse](./retentionofferpriceslinkagesresponse.md)
  A response containing the resource identifiers of prices for a retention offer.
- [object SubscriptionRetentionOffersLinkagesResponse](./subscriptionretentionofferslinkagesresponse.md)
  A response containing the resource identifiers of all retention offers for a subscription.
- [object SubscriptionRetentionMessageOffersLinkagesRequest](./subscriptionretentionmessageofferslinkagesrequest.md)
  The request body you use to add or remove retention offers from a subscription’s retention message.
- [object SubscriptionRetentionMessageOffersLinkagesResponse](./subscriptionretentionmessageofferslinkagesresponse.md)
  A response containing the resource identifiers of retention offers that appear with a subscription’s retention message.

## See Also

### Managing retention messaging
- [Retention messages](./retention-messages.md)
  Create and manage the messages people see when they start to cancel an auto-renewable subscription.
- [Retention message versions](./retention-message-versions.md)
  Create versions of a retention message’s content and track their progress through App Review.
- [Retention message localizations](./retention-message-localizations.md)
  Create and manage the localized header and body text of a retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retention-offers)*