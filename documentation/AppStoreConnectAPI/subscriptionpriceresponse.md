# SubscriptionPriceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create a single subscription price.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionPriceResponse
```

## Properties

- `data` (SubscriptionPrice) *(required)*
- `included` ([*])
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionPricePointResponse](subscriptionpricepointresponse.md)
  The response body for endpoints that read a single subscription price point.
- [object SubscriptionPricePoint](subscriptionpricepoint.md)
  A standard price tier for auto-renewable subscriptions, defining the customer price and developer proceeds.
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.
- [object SubscriptionPriceCreateRequest](subscriptionpricecreaterequest.md)
  The request body you use to create a subscription price.
- [object SubscriptionPriceInlineCreate](subscriptionpriceinlinecreate.md)
  An inline object for specifying a territory-specific subscription price within a price schedule.
- [object SubscriptionPricePointInlineCreate](subscriptionpricepointinlinecreate.md)
  An inline object for specifying a price point when creating a subscription pricing configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpriceresponse)*