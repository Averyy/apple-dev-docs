# Get Refund History

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a paginated list of all of a customer’s refunded in-app purchases for your app.

**Availability**:
- App Store Server API 1.6+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

## Discussion

Call this endpoint to get the customer’s complete refund history for your app by providing the transaction identifier ([`transactionId`](./transactionid.md)) for any of the customer’s in-app purchases. Each response ([`RefundHistoryResponse`](./refundhistoryresponse.md)) contains a maximum of 20 refunded transactions. If the [`hasMore`](./hasmore.md) property in the response is `true`, call the endpoint again using the `revision` token from the response to get the next set of refunded transactions.

The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [In-app purchase](https://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([`notificationType`](../AppStoreServerNotifications/notificationtype.md)) from [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [`JWSTransactionDecodedPayload`](./jwstransactiondecodedpayload.md).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

To get a customer’s full refund history for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.apple.com/inApps/v2/refund/lookup/{anyTransactionId}
```

For subsequent requests, include the `revision` token from the previous [`RefundHistoryResponse`](./refundhistoryresponse.md).

```javascript
GET https://api.storekit.apple.com/inApps/v2/refund/lookup/{anyTransactionId}?revision={revision}
```

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v2/refund/lookup/{anyTransactionId}`

## Parameters

### Path Parameters

- `anyTransactionId` (anyTransactionId) *(required)*: Any [`originalTransactionId`](./originaltransactionid.md), [`transactionId`](./transactionid.md) or [`appTransactionId`](./apptransactionid.md) that belongs to the customer for your app.

### Query Parameters

- `revision` (revision): A token you provide to get the next set of up to 20 transactions. All responses include a `revision` token. Use the `revision` token from the previous [`RefundHistoryResponse`](./refundhistoryresponse.md).

  You can store the `revision` token from the final results page and use it for a future call. For more information, see [`RefundHistoryResponse`](./refundhistoryresponse.md).

  The `revision` token is required in all requests except the initial request.

## Responses

- `200` OK (`RefundHistoryResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | InvalidRequestRevisionError)`, `application/json`): Invalid request. Check the specific error message for further information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`): Invalid request. Check the specific error message for further information.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Refund lookup
- [object RefundHistoryResponse](./refundhistoryresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history)*