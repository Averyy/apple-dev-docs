# Get App Transaction Info

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a customer’s app transaction information for your app.

**Availability**:
- App Store Server API 1.17+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

#### Discussion

Use this endpoint to get the app transaction information for a customer of your app. You can provide any transaction ID that belongs to the customer to get their app transaction information.

App transaction information represents the customer’s purchase of the app, cryptographically signed by the App Store. The App Store generates a single, globally unique [`appTransactionId`](./apptransactionid.md) for each Apple Account that downloads your app and for each family group member for apps that support Family Sharing. The `appTransactionId` value remains the same for the same Apple Account and app if the customer redownloads the app on any device, receives a refund, repurchases the app, or changes the storefront. For apps that support Family Sharing, the `appTransactionId` is unique for each family group member.

App transaction information includes details about the app the customer purchased, such as its bundleID, original version, original purchase date, and more. You can also get app transaction information in your app from StoreKit, using [`AppTransaction`](../StoreKit/apptransaction.md).

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/transactions/appTransactions/{anyTransactionId}`

## Parameters

### Path Parameters

- `anyTransactionId` (anyTransactionId) *(required)*: Any [`originalTransactionId`](./originaltransactionid.md), [`transactionId`](./transactionid.md) or [`appTransactionId`](./apptransactionid.md) that belongs to the customer for your app.

## Responses

- `200` OK (`AppTransactionInfoResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`InvalidTransactionIdError`, `application/json`): Invalid request.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`(TransactionIdNotFoundError | AppTransactionDoesNotExistError)`, `application/json`): Check the specific error message for further information.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### App Transaction information
- [object AppTransactionInfoResponse](./apptransactioninforesponse.md)
  A response that contains signed app transaction information for a customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-app-transaction-info)*