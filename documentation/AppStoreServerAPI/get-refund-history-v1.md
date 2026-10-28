# Get Refund History V1

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of up to 50 of a customer’s refunded in-app purchases for your app.

**Availability**:
- App Store Server API 1.1+ - Deprecated in 1.6

> **Deprecated**: Use [`Get Refund History`](./get-refund-history.md) instead.

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

## Discussion

Call this endpoint to get a customer’s refund history for your app. The response ([`RefundLookupResponse`](./refundlookupresponse.md)) includes up to 50 of the customer’s most-recently refunded transactions, based on the [`revocationDate`](./revocationdate.md).

> **Note**:  To get the complete refund history, use [`Get Refund History`](./get-refund-history.md).

To call this endpoint, provide any original transaction identifier ([`originalID`](../StoreKit/transaction/originalid.md)) for any of the customer’s in-app purchases. The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [In-app purchase](https://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([`notificationType`](../AppStoreServerNotifications/notificationtype.md)) from [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [`JWSTransactionDecodedPayload`](./jwstransactiondecodedpayload.md).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/refund/lookup/{originalTransactionId}`

## Parameters

### Path Parameters

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier for a transaction that belongs to the customer.

## Responses

- `200` OK (`RefundLookupResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`InvalidOriginalTransactionIdError`, `application/json`): The request is invalid. Check the specific error message for further information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`OriginalTransactionIdNotFoundError`, `application/json`): The request is invalid. Check the specific error message for further information.
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): The request failed. This may be due to a temporary outage. Check the specific error message for further information.

## See Also

### Deprecated
- [Get Transaction History V1](./get-transaction-history-v1.md)
  Get a customer’s in-app purchase transaction history for your app, except finished consumable in-app purchases.
- [object RefundLookupResponse](./refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history-v1)*