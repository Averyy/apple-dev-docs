# SubscriptionPromotionalOffer

**Framework**: App Store Connect API  
**Kind**: dictionary

A discounted or free trial offer for an auto-renewable subscription, available to eligible existing or former subscribers.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionPromotionalOffer
```

## Topics

### Objects
- [object SubscriptionPromotionalOffer.Attributes](subscriptionpromotionaloffer/attributes-data.dictionary.md)
  Attributes that describe a subscription promotional offer resource.
- [object SubscriptionPromotionalOffer.Relationships](subscriptionpromotionaloffer/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionPromotionalOffer.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionPromotionalOffer.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionPromotionalOfferCreateRequest](subscriptionpromotionaloffercreaterequest.md)
  The request body you use to create a subscription promotional offer.
- [object SubscriptionPromotionalOfferInlineCreate](subscriptionpromotionalofferinlinecreate.md)
  An inline object for specifying a promotional offer when creating or updating a subscription.
- [object SubscriptionPromotionalOfferPrice](subscriptionpromotionalofferprice.md)
  The territory-specific customer price and duration for a subscription promotional offer.
- [object SubscriptionPromotionalOfferPriceInlineCreate](subscriptionpromotionalofferpriceinlinecreate.md)
  An inline object for specifying territory pricing when creating a subscription promotional offer.
- [object SubscriptionPromotionalOfferPricesResponse](subscriptionpromotionalofferpricesresponse.md)
  A response containing a list of territory-specific prices for a subscription promotional offer.
- [object SubscriptionPromotionalOfferResponse](subscriptionpromotionalofferresponse.md)
  The response body for endpoints that create, read, or modify a single subscription promotional offer.
- [object SubscriptionPromotionalOfferUpdateRequest](subscriptionpromotionalofferupdaterequest.md)
  The request body you use to update a subscription promotional offer update request.
- [object SubscriptionPromotionalOffersResponse](subscriptionpromotionaloffersresponse.md)
  The response body for endpoints that list promotional offers for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpromotionaloffer)*