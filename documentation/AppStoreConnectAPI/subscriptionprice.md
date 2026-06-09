# SubscriptionPrice

**Framework**: App Store Connect API  
**Kind**: dictionary

A configured price for an auto-renewable subscription in a specific App Store territory.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionPrice
```

## Topics

### Objects
- [object SubscriptionPrice.Attributes](subscriptionprice/attributes-data.dictionary.md)
  Attributes that describe a subscription price resource.
- [object SubscriptionPrice.Relationships](subscriptionprice/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionPrice.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionPrice.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionCreateRequest](subscriptioncreaterequest.md)
  The request body you use to create a subscription.
- [object SubscriptionUpdateRequest](subscriptionupdaterequest.md)
  The request body you use to update a subscription update request.
- [object SubscriptionResponse](subscriptionresponse.md)
  The response body for endpoints that create, read, or modify a single auto-renewable subscription.
- [object SubscriptionsResponse](subscriptionsresponse.md)
  The response body for endpoints that list auto-renewable subscriptions in a subscription group.
- [object Subscription](subscription.md)
  An auto-renewable subscription product offered within an app, with configurable pricing, duration, and promotional offers.
- [object SubscriptionIntroductoryOffersResponse](subscriptionintroductoryoffersresponse.md)
  The response body for endpoints that list introductory offers for a subscription.
- [object SubscriptionIntroductoryOffer](subscriptionintroductoryoffer.md)
  A discounted price or free trial period offered to new subscribers of an auto-renewable subscription.
- [object SubscriptionIntroductoryOffersLinkagesRequest](subscriptionintroductoryofferslinkagesrequest.md)
  The request body for updating the list of introductory offers linked to a subscription.
- [object SubscriptionIntroductoryOffersLinkagesResponse](subscriptionintroductoryofferslinkagesresponse.md)
  A response containing the resource identifiers of introductory offers linked to a subscription.
- [object SubscriptionOfferCodeResponse](subscriptionoffercoderesponse.md)
  The response body for endpoints that create, read, or modify a single subscription offer code.
- [object SubscriptionOfferCodesResponse](subscriptionoffercodesresponse.md)
  The response body for endpoints that list offer codes for a subscription.
- [object SubscriptionOfferCode](subscriptionoffercode.md)
  A promotional code that gives customers a discounted or free subscription for a specified duration and eligibility group.
- [object PromotedPurchaseResponse](promotedpurchaseresponse.md)
  The response body for endpoints that read or modify a promoted in-app purchase or subscription.
- [object PromotedPurchase](promotedpurchase.md)
  An in-app purchase or subscription configured to appear on the app’s App Store product page.
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionprice)*