# Get Refund History

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a paginated list of all of a customer’s refunded in-app purchases for your app.

**Availability**:
- App Store Server API 1.6+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to get the customer’s complete refund history for your app by providing the transaction identifier ([`transactionId`](get-refund-history/transactionid.md)) for any of the customer’s in-app purchases. Each response ([`RefundHistoryResponse`](refundhistoryresponse.md)) contains a maximum of 20 refunded transactions. If the [`hasMore`](hasmore.md) property in the response is `true`, call the endpoint again using the [`revision`](get-refund-history/revision.md) token from the response to get the next set of refunded transactions.

The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType)) from [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

To get a customer’s full refund history for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/refund/lookup/{transactionId}
```

For subsequent requests, include the [`revision`](get-refund-history/revision.md) token from the previous [`RefundHistoryResponse`](refundhistoryresponse.md).

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/refund/lookup/{transactionId}?revision={revision}
```

## See Also

- [object RefundHistoryResponse](refundhistoryresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.
- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.
- [object RefundLookupResponse](refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history)*