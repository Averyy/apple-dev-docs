# Get Transaction Info

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a single transaction for your app.

**Availability**:
- App Store Server API 1.8+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

#### Discussion

Use this endpoint to get transaction information for any transaction identifier, including original transaction identifiers.  This endpoint supports all in-app purchase types, including consumable, non-consumable, non-renewing subscriptions, and auto-renewable subscriptions. It also supports transactions that your app marked as finished using [`finish()`](../StoreKit/transaction/finish%28%29.md) or [`finishTransaction(_:)`](../StoreKit/skpaymentqueue/finishtransaction%28_%29.md) in StoreKit.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/transactions/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (transactionId) *(required)*: The identifier of a transaction that belongs to the customer, and which may be an original transaction identifier ([`originalTransactionId`](./originaltransactionid.md)).

## Responses

- `200` OK (`TransactionInfoResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | AppTransactionIdNotSupportedError)`, `application/json`): Invalid request.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`): The transaction identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Transaction information
- [object TransactionInfoResponse](./transactioninforesponse.md)
  A response that contains signed transaction information for a single transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info)*