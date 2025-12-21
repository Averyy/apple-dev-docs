# originalTransactionId

**Framework**: App Store Server API  
**Kind**: typealias

The original transaction identifier of a purchase.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string originalTransactionId
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)

#### Discussion

The App Store generates an original transaction identifier when a customer makes a successful in-app purchase. Most App Store Server API endpoints accept an `originalTransactionId`.

There are several ways to obtain this value: from your app after a user makes a successful in-app purchase, from transaction information provided in [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications), or from [`App Store Receipts`](https://developer.apple.com/documentation/AppStoreReceipts) for apps that use the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase).

To get the original transaction identifier from your app, use the [`originalID`](https://developer.apple.com/documentation/StoreKit/Transaction/originalID) property of the [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) object that represents the in-app purchase.

If you’ve enabled [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications), your server receives notifications for in-app purchase events that include the transaction information with the original transaction identifier. For more information, see [`responseBodyV2DecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload).

If your app uses the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase), the original transaction identifier is the [`transactionIdentifier`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier) property in the [`SKPaymentTransaction`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction) object. For restored purchases, the original transaction identifier is found in the [`transactionIdentifier`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier) of the [`original`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/original) property. If you verify receipts using [`verifyReceipt`](https://developer.apple.com/documentation/AppStoreReceipts/Verify-Receipt), the original transaction identifier is the [`original_transaction_id`](https://developer.apple.com/documentation/AppStoreReceipts/original_transaction_id) value.

Use the value of the original transaction identifier that you get from your app, a notification, or a receipt as the value for [`originalTransactionId`](originaltransactionid.md) when you send requests to the App Store Server API.

> 💡 **Tip**:  If you maintain a database to manage your subscribers, save the original transaction identifier to uniquely identify auto-renewable subscriptions.

## See Also

- [type effectiveDate](effectivedate.md)
  The new subscription expiration date for a subscription-renewal extension.
- [type success](success.md)
  A Boolean value that indicates whether the subscription-renewal-date extension succeeded.
- [type webOrderLineItemId](weborderlineitemid.md)
  The unique identifier of subscription-purchase events across devices, including renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/originaltransactionid)*