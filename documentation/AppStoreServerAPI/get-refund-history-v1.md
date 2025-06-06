# Get Refund History V1

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a list of up to 50 of a customer’s refunded in-app purchases for your app.

**Availability**:
- App Store Server API 1.1+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to get a customer’s refund history for your app. The response ([`RefundLookupResponse`](refundlookupresponse.md)) includes up to 50 of the customer’s most-recently refunded transactions, based on the [`revocationDate`](revocationdate.md).

> **Note**:  To get the complete refund history, use [`Get Refund History`](get-refund-history.md).

 To get the complete refund history, use [`Get Refund History`](get-refund-history.md).

To call this endpoint, provide any original transaction identifier ([`originalID`](https://developer.apple.com/documentation/StoreKit/Transaction/originalID)) for any of the customer’s in-app purchases. The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType)) from [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

## See Also

- [Get Refund History](get-refund-history.md)
  Get a paginated list of all of a customer’s refunded in-app purchases for your app.
- [object RefundHistoryResponse](refundhistoryresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.
- [object RefundLookupResponse](refundlookupresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history-v1)*