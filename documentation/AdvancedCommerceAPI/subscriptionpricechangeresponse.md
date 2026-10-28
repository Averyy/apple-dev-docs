# SubscriptionPriceChangeResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionPriceChangeResponse
```

## Discussion

This is the response body for the [`Change Subscription Price`](./change-subscription-price.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.

## See Also

### Subscription price change from the server
- [Change Subscription Price](./change-subscription-price.md)
  Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.
- [object SubscriptionPriceChangeRequest](./subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangeresponse)*