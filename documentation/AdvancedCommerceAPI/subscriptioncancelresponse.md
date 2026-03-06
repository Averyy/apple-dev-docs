# SubscriptionCancelResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The response body for a successful subscription cancellation.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object SubscriptionCancelResponse
```

#### Discussion

This is the response body for the [`Cancel a Subscription`](cancel-a-subscription.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.

## See Also

- [Cancel a Subscription](cancel-a-subscription.md)
  Turn off automatic renewal to cancel a customer’s auto-renewable subscription.
- [object SubscriptionCancelRequest](subscriptioncancelrequest.md)
  The request body for turning off automatic renewal of a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncancelresponse)*