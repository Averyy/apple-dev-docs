# SubscriptionPriceChangeItemV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionPriceChangeItemV1
```

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `dependentSKUs` ([dependentSKU])
- `price` (price)

## See Also

### Subscription price change from the server
- [Change Subscription Price](./change-subscription-price.md)
  Increase or decrease the price of an auto-renewable subscription at the next renewal.
- [object SubscriptionPriceChangeRequest](./subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](./subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.
- [object SubscriptionPriceChangeRequestV1](./subscriptionpricechangerequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangeitemv1)*