# SubscriptionRevokeResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The response body for a successful revoke-subscription request.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object SubscriptionRevokeResponse
```

## Discussion

This is the response body for the [`Revoke Subscription`](./revoke-subscription.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.
- `transactions` ([BundleTransaction])

## See Also

### Subscription revocation from the server
- [Revoke Subscription](./revoke-subscription.md)
  Immediately cancel a subscription and all its items, or revoke unclaimed seats of a multiseat purchase, and request a full or prorated refund.
- [object SubscriptionRevokeRequest](./subscriptionrevokerequest.md)
  The request body you provide to terminate a subscription and all its items immediately, or to revoke unclaimed seats from a multiseat purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokeresponse)*