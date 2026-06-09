# Win-back offers

**Framework**: App Store Connect API

Create and manage win-back offers for your auto-renewable subscriptions.

#### Overview

Win-back offers are offers you create for your apps to re-acquire churned subscribers of an auto-renewable subscription. To learn more, see [`Creating and configuring win-back offers`](creating-and-configuring-win-back-offers.md).

## Topics

### Endpoints
- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List Win-Back Offers](get-v1-subscriptions-_id_-winbackoffers.md)
  The data structure that represents a get-v1-subscriptions-{id}-win back offers resource.
- [List win-back offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read Win-Back Offer Information](get-v1-winbackoffers-_id_.md)
  The data structure that represents a get-v1-win back offers-{id} resource.
- [List Win-Back Offer Prices](get-v1-winbackoffers-_id_-prices.md)
  The data structure that represents a get-v1-win back offers-{id}-prices resource.
- [List price IDs for a win-back offer](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a Win-Back Offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a Win-Back Offer](patch-v1-winbackoffers-_id_.md)
  The data structure that represents a patch-v1-win back offers-{id} resource.
- [Delete a Win-Back Offer](delete-v1-winbackoffers-_id_.md)
  The data structure that represents a delete-v1-win back offers-{id} resource.
### Objects
- [object WinBackOffer](winbackoffer.md)
  A promotional offer targeting lapsed subscribers, providing a discount or free trial to encourage them to resubscribe.
- [object WinBackOfferCreateRequest](winbackoffercreaterequest.md)
  The request body you use to create a winback offer.
- [object WinBackOfferPrice](winbackofferprice.md)
  The territory-specific customer price and duration for a win-back subscription offer.
- [object WinBackOfferPriceInlineCreate](winbackofferpriceinlinecreate.md)
  An inline object for specifying territory-specific pricing when creating or updating a win-back offer.
- [object WinBackOfferPricesResponse](winbackofferpricesresponse.md)
  The response body for endpoints that list prices for a win-back offer.
- [object WinBackOfferResponse](winbackofferresponse.md)
  The response body for endpoints that create, read, or modify a single win-back offer for a subscription.
- [object WinBackOfferUpdateRequest](winbackofferupdaterequest.md)
  The request body you use to update a win-back offer.
- [object WinBackOffersResponse](winbackoffersresponse.md)
  The response body for endpoints that list win-back offers for a subscription.
- [object IntegerRange](integerrange.md)
  Describe the upper and lower integer bound of the attribute.
- [object WinBackOfferPricesLinkagesResponse](winbackofferpriceslinkagesresponse.md)
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)

## See Also

- [In-App Purchase](in-app-purchase.md)
  Create and manage in-app purchases, including localizations, price schedules, and submissions for review.
- [Auto-Renewable Subscriptions](auto-renewable-subscriptions.md)
  Create and manage auto-renewable subscriptions, including managing subscription groups and submissions for review.
- [Promoted Purchases](promoted-purchases-top.md)
  Manage promoted in-app purchases and auto-renewable subscriptions, including their visibility and images.
- [In-App Purchase and Subscription App Store Review Submissions](in-app-purchase-and-subscription-app-store-review-submissions.md)
  Manage submissions for App Store Review for in-app purchases and auto-renewable subscriptions, including their screenshots.
- [Testing In-App Purchase and Subscriptions](testing-in-app-purchase-and-subscriptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/win-back-offers)*