# Finish Transaction

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Notifies the App Store server that your system has finished processing the customer’s transaction.

**Availability**:
- App Store Server API 1.20+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

## Discussion

If you manage entitlement logic on your server, your server can call `Finish Transaction` after it finishes providing the customer with the new content. If you call [`finish()`](../StoreKit/transaction/finish%28%29.md) in your app, there’s no need to call the `Finish Transaction` endpoint from your server.

## Endpoint

`POST https://api.storekit-sandbox.apple.com/inApps/v1/transactions/{transactionId}/finish`

## Parameters

### Path Parameters

- `transactionId` (transactionId) *(required)*: The transaction identifier of the transaction to mark as finished.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | AppTransactionIdNotSupportedError)`, `application/json`): The request is invalid and can’t be accepted.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`): The transaction identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/finish-transaction)*