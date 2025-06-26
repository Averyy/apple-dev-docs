# Revoke Subscription

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Immediately cancel a customer’s subscription and all the items that are included in the subscription, and request a full or prorated refund.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Advanced Commerce API changelog](changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)

#### Discussion

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false`, and revokes the subscription with a full or prorated refund. The App Store Server Notifications sends a `REFUND`  [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) to your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. Check the `revocationDate` property in the notification’s  [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload). Turn off service for the subscription and its items as of the revocation date. Don’t turn off service to the subscription until you receive the notification.

To cancel a subscription at the end of the current period instead, see [`Cancel a Subscription`](cancel-a-subscription.md).

> **Note**: To use the `Revoke Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [`Cancel a Subscription`](cancel-a-subscription.md), `Revoke Subscription`, and [`Request Transaction Refund`](request-transaction-refund.md) APIs.

## See Also

- [object SubscriptionRevokeRequest](subscriptionrevokerequest.md)
  The request body you provide to terminate a subscription and all its items immediately.
- [object SubscriptionRevokeResponse](subscriptionrevokeresponse.md)
  The response body for a successful revoke-subscription request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/revoke-subscription)*