# SubscriptionPriceChangeRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request body you use to change the price of an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionPriceChangeRequest
```

### Discussion

This is the request body for the [`Change Subscription Price`](./change-subscription-price.md) endpoint.

The items array contains [`SubscriptionPriceChangeItem`](./subscriptionpricechangeitem.md). Include one entry for each SKU within the subscription that has a price change.

## Properties

- `currency` (currency): The currency of the prices.
- `items` ([SubscriptionPriceChangeItem]) *(required)*: An array that contains one or more SKUs and the changed price for each SKU.
- `requestInfo` (RequestInfo) *(required)*: Metadata that identifies the request.
- `storefront` (storefront): The App Store storefront of the subscription.

## See Also

### Subscription price change from the server
- [Change Subscription Price](./change-subscription-price.md)
  Increase or decrease the price of an auto-renewable subscription at the next renewal.
- [object SubscriptionPriceChangeResponse](./subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.
- [object SubscriptionPriceChangeRequestV1](./subscriptionpricechangerequestv1.md)
- [object SubscriptionPriceChangeItemV1](./subscriptionpricechangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangerequest)*