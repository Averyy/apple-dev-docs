# Request Transaction Refund

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Request a refund for a one-time charge or subscription transaction.

**Availability**:
- Advanced Commerce API 1.3+

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

## Discussion

> **Note**: To use the `Request Transaction Refund` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [`Cancel a Subscription`](./cancel-a-subscription.md), [`Revoke Subscription`](./revoke-subscription.md), and `Request Transaction Refund` APIs.

### Refund a multiseat purchase

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

For a subscription that a customer buys as a multiseat purchase, a request that revokes the subscription needs a refund type of `FULL` or `PRORATED`; a `CUSTOM` refund type with a revocation returns [`CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError`](./customrefundwithrevokenotallowedformultiseatsubscriptionerror.md). For more information, see [`RefundItem`](./refunditem.md). To revoke only some of the subscription’s unclaimed seats, call the [`Revoke Subscription`](./revoke-subscription.md) endpoint with a [`revokeSeatQuantity`](./revokeseatquantity.md).

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v2/transaction/requestRefund/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: The transaction identifier for which you request a refund.

## Request Body

**Content-Type**: `application/json`  
**Type**: `RequestRefundRequest`

The request body.

## Responses

- `200` OK (`TransactionsResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(FamilyTransactionNotSupportedError | InvalidTransactionIdError | RepeatedRequestReferenceIdError | NullRequestInfoError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | MismatchedStorefrontError | SimulateRefundDeclineOnlyInSandboxError | RefundAmountWithoutCustomError | InvalidRefundTypeError | InvalidRefundReasonError | NegativeRefundAmountError | NullRefundAmountError | NullRefundReasonError | NullRefundTypeError | PendingRefundError | ProratedOnlyLatestTransactionError | PartialSimulateRefundDeclineError | CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError | InvalidCurrencyError | SKULengthExceededError | NullCurrencyError | NullItemsError | NullSKUError | InvalidSKUError | InvalidAmountError | MissingPricingConfigForStorefrontError | MultipleOperationsOnSingleSKUError | RevokeOnInactiveSubscriptionError)`, `application/json`)
- `401` Unauthorized (`UnauthorizedError`, `application/json`): The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Authorizing API requests from your server](./authorizing-server-calls.md).
- `403` Forbidden (`(ForbiddenError | SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ProductNotOwnedError | InsufficientFundsError | AlreadyRefundedError | TransactionNotRefundableError | RefundOfBundleItemNotAllowedError)`, `application/json`)
- `404` Not Found (`(NotFoundError | TransactionIdNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md).
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Refund request from the server
- [object RequestRefundRequest](./requestrefundrequest.md)
  The request body for requesting a refund for a transaction.
- [object RequestRefundResponse](./requestrefundresponse.md)
  The response body for a transaction refund request.
- [object RequestRefundItem](./requestrefunditem.md)
  Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.
- [object RefundItem](./refunditem.md)
  Information about the item to refund, such as its SKU, the type of refund, and whether to revoke entitlement.
- [object RequestRefundRequestV1](./requestrefundrequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/request-transaction-refund)*