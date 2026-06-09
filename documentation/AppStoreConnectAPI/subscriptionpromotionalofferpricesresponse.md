# SubscriptionPromotionalOfferPricesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of territory-specific prices for a subscription promotional offer.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionPromotionalOfferPricesResponse
```

## Properties

- `data` ([SubscriptionPromotionalOfferPrice]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object SubscriptionPromotionalOffer](subscriptionpromotionaloffer.md)
  A discounted or free trial offer for an auto-renewable subscription, available to eligible existing or former subscribers.
- [object SubscriptionPromotionalOfferCreateRequest](subscriptionpromotionaloffercreaterequest.md)
  The request body you use to create a subscription promotional offer.
- [object SubscriptionPromotionalOfferInlineCreate](subscriptionpromotionalofferinlinecreate.md)
  An inline object for specifying a promotional offer when creating or updating a subscription.
- [object SubscriptionPromotionalOfferPrice](subscriptionpromotionalofferprice.md)
  The territory-specific customer price and duration for a subscription promotional offer.
- [object SubscriptionPromotionalOfferPriceInlineCreate](subscriptionpromotionalofferpriceinlinecreate.md)
  An inline object for specifying territory pricing when creating a subscription promotional offer.
- [object SubscriptionPromotionalOfferResponse](subscriptionpromotionalofferresponse.md)
  The response body for endpoints that create, read, or modify a single subscription promotional offer.
- [object SubscriptionPromotionalOfferUpdateRequest](subscriptionpromotionalofferupdaterequest.md)
  The request body you use to update a subscription promotional offer update request.
- [object SubscriptionPromotionalOffersResponse](subscriptionpromotionaloffersresponse.md)
  The response body for endpoints that list promotional offers for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpromotionalofferpricesresponse)*