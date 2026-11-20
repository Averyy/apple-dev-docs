# SubscriptionPriceChangeRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionPriceChangeRequestV1
```

## Properties

- `currency` (currency)
- `items` ([SubscriptionPriceChangeItemV1]) *(required)*
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)

## See Also

### Subscription price change from the server
- [Change Subscription Price](./change-subscription-price.md)
  Increase or decrease the price of an auto-renewable subscription at the next renewal.
- [object SubscriptionPriceChangeRequest](./subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](./subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.
- [object SubscriptionPriceChangeItemV1](./subscriptionpricechangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangerequestv1)*