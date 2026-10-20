# Revoke Subscription

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Immediately cancel a customer’s subscription and all the items that are included in the subscription, and request a full or prorated refund.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Advanced Commerce API changelog](./changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

#### Discussion

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false`, and revokes the subscription with a full or prorated refund. The App Store Server Notifications sends a `REFUND`  [`notificationType`](../AppStoreServerNotifications/notificationtype.md) to your [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) endpoint. Check the `revocationDate` property in the notification’s  [`JWSTransactionDecodedPayload`](../AppStoreServerNotifications/jwstransactiondecodedpayload.md). Turn off service for the subscription and its items as of the revocation date. Don’t turn off service to the subscription until you receive the notification.

To cancel a subscription at the end of the current period instead, see [`Cancel a Subscription`](./cancel-a-subscription.md).

> **Note**: To use the `Revoke Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [`Cancel a Subscription`](./cancel-a-subscription.md), `Revoke Subscription`, and [`Request Transaction Refund`](./request-transaction-refund.md) APIs.

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/subscription/revoke/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: The transaction identifier of the auto-renewable subscription to revoke. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionRevokeRequest`

## Responses

- `200` OK (`SubscriptionRevokeResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | MismatchedStorefrontError | MismatchedStorefrontError | OperationNotAllowedError | MalformedPayloadError | SimulateRefundDeclineOnlyInSandboxError | RefundAmountWithoutCustomError | NullRefundRiskingError | InvalidRefundTypeError | InvalidRefundReasonError | NegativeRefundAmountError | NullRefundAmountError | NullRefundReasonError | NullRefundTypeError | PendingRefundError | RevokeOnInactiveSubscriptionError)`, `application/json`)
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Authorizing API requests from your server](./authorizing-server-calls.md).
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ProductNotOwnedError | InsufficientFundsError | AlreadyRefundedError | TransactionNotRefundableError)`, `application/json`)
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md).
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Subscription revocation from the server
- [object SubscriptionRevokeRequest](./subscriptionrevokerequest.md)
  The request body you provide to terminate a subscription and all its items immediately.
- [object SubscriptionRevokeResponse](./subscriptionrevokeresponse.md)
  The response body for a successful revoke-subscription request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/revoke-subscription)*