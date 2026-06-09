# SubscriptionPricePoint

**Framework**: App Store Connect API  
**Kind**: dictionary

A standard price tier for auto-renewable subscriptions, defining the customer price and developer proceeds.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionPricePoint
```

## Topics

### Objects
- [object SubscriptionPricePoint.Attributes](subscriptionpricepoint/attributes-data.dictionary.md)
  Attributes that describe a subscription price point resource.
- [object SubscriptionPricePoint.Relationships](subscriptionpricepoint/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionPricePoint.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionPricePoint.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionPricePointResponse](subscriptionpricepointresponse.md)
  The response body for endpoints that read a single subscription price point.
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.
- [object SubscriptionPriceCreateRequest](subscriptionpricecreaterequest.md)
  The request body you use to create a subscription price.
- [object SubscriptionPriceInlineCreate](subscriptionpriceinlinecreate.md)
  An inline object for specifying a territory-specific subscription price within a price schedule.
- [object SubscriptionPriceResponse](subscriptionpriceresponse.md)
  The response body for endpoints that create a single subscription price.
- [object SubscriptionPricePointInlineCreate](subscriptionpricepointinlinecreate.md)
  An inline object for specifying a price point when creating a subscription pricing configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricepoint)*