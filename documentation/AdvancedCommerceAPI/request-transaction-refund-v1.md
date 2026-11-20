# Request Transaction Refund V1

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Advanced Commerce API 1.0+

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/transaction/requestRefund/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `RequestRefundRequestV1`

## Responses

- `200` OK (`RequestRefundResponse`, `application/json`)
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | MismatchedStorefrontError | OperationNotAllowedError | MalformedPayloadError | SimulateRefundDeclineOnlyInSandboxError | RefundAmountWithoutCustomError | NullRefundRiskingError | InvalidRefundTypeError | InvalidRefundReasonError | NegativeRefundAmountError | NullRefundAmountError | NullRefundReasonError | NullRefundTypeError | RemovalAllNotAllowedError | PendingRefundError | ProratedOnlyLatestTransactionError | PartialSimulateRefundDeclineError | CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError)`, `application/json`)
- `401` Unauthorized
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ProductNotOwnedError | InsufficientFundsError | AlreadyRefundedError | TransactionNotRefundableError)`, `application/json`)
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/request-transaction-refund-v1)*