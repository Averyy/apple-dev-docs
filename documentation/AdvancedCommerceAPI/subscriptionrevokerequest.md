# SubscriptionRevokeRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request body you provide to terminate a subscription and all its items immediately, or to revoke unclaimed seats from a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object SubscriptionRevokeRequest
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

This is the request body for the [`Revoke Subscription`](./revoke-subscription.md) endpoint.

The `refundType` of a revoke request is `FULL` or `PRORATED`.

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

For a subscription that a customer buys as a multiseat purchase, provide a [`revokeSeatQuantity`](./subscriptionrevokerequest/revokeseatquantity.md) to revoke only some of its unclaimed seats. The subscription’s transaction remains valid for its remaining seats, and its automatic renewal status doesn’t change. For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).

## Properties

- `refundReason` (refundReason) *(required)*
- `refundRiskingPreference` (refundRiskingPreference) *(required)*
- `refundType` (string) *(required)*: **Allowed Values**: `FULL`, `PRORATED`
- `requestInfo` (RequestInfo) *(required)*
- `revokeSeatQuantity` (revokeSeatQuantity): The number of unclaimed seats to revoke from a subscription that a customer buys as a multiseat purchase. Omit this value to revoke the entire subscription.

  **Minimum**: `1`
- `storefront` (storefront)

## See Also

### Subscription revocation from the server
- [Revoke Subscription](./revoke-subscription.md)
  Immediately cancel a subscription and all its items, or revoke unclaimed seats of a multiseat purchase, and request a full or prorated refund.
- [object SubscriptionRevokeResponse](./subscriptionrevokeresponse.md)
  The response body for a successful revoke-subscription request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokerequest)*