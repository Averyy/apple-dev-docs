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

#### Discussion

This is the response body for the [`Revoke Subscription`](./revoke-subscription.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.

## See Also

### Subscription revocation from the server
- [Revoke Subscription](./revoke-subscription.md)
  Immediately cancel a customer’s subscription and all the items that are included in the subscription, and request a full or prorated refund.
- [object SubscriptionRevokeRequest](./subscriptionrevokerequest.md)
  The request body you provide to terminate a subscription and all its items immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokeresponse)*