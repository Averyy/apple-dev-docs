# Cancel a Subscription

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Turn off automatic renewal to cancel a customer’s auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false` and the subscription doesn’t renew at the next renewal period. The customer continues to have access to the subscription until the end of the current period.

To immediately cancel a subscription instead, see [`Revoke Subscription`](revoke-subscription.md).

> **Note**: To use the `Cancel a Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the `Cancel a Subscription`, [`Revoke Subscription`](revoke-subscription.md), and [`Request Transaction Refund`](request-transaction-refund.md) APIs.

##### Example Request and Response

## Request Body

The request body that includes information about the subscription to cancel.

## See Also

- [object SubscriptionCancelRequest](subscriptioncancelrequest.md)
  The request body for turning off automatic renewal of a subscription.
- [object SubscriptionCancelResponse](subscriptioncancelresponse.md)
  The response body for a successful subscription cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/cancel-a-subscription)*