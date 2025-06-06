# Win-back offers

**Framework**: App Store Connect API

Create and manage win-back offers for your auto-renewable subscriptions.

#### Overview

Win-back offers are offers you create for your apps to re-acquire churned subscribers of an auto-renewable subscription. To learn more, see [`Creating and configuring win-back offers`](creating-and-configuring-win-back-offers.md).

## Topics

### Endpoints
- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List win-back offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [Read win-back offer information](get-v1-winbackoffers-_id_.md)
  Read details about a specific win-back offer.
- [List win-back offer prices](get-v1-winbackoffers-_id_-prices.md)
  List all prices for specific win-back offers.
- [Create a win-back offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a win-back offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.
- [Delete a win-back offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.
### Objects
- [object WinBackOffer](winbackoffer.md)
  The data structure that represents a win-back offer resource.
- [object WinBackOfferCreateRequest](winbackoffercreaterequest.md)
  The request body you use to create a winback offer.
- [object WinBackOfferPrice](winbackofferprice.md)
  The data structure that represents a winback offer price resource.
- [object WinBackOfferPriceInlineCreate](winbackofferpriceinlinecreate.md)
  The data structure that represents a win-back offer price inline create resource.
- [object WinBackOfferPricesResponse](winbackofferpricesresponse.md)
  A response that contains a list of win-back offer price resources.
- [object WinBackOfferResponse](winbackofferresponse.md)
  A response that contains a single win-back offer resource.
- [object WinBackOfferUpdateRequest](winbackofferupdaterequest.md)
  The request body you use to update a win-back offer.
- [object WinBackOffersResponse](winbackoffersresponse.md)
  A response that contains a list of win-back offer resources.
- [object IntegerRange](integerrange.md)
  Describe the upper and lower integer bound of the attribute.

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