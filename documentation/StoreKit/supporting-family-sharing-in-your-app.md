# Supporting Family Sharing in your app

**Framework**: StoreKit  
**Role**: Article

Provide service to share subscriptions and non-consumable products to family members.

## Overview

Family Sharing allows a customer to share access to auto-renewable subscriptions or non-consumables with up to five family members on all of their Apple devices. Enabling Family Sharing for a subscription can make your content or service more appealing to subscribers, and may encourage conversion to a paid subscription, increase customer engagement, and improve retention. Developers can choose to turn on Family Sharing for Apple In-App Purchases and non-consumables in App Store Connect. Users can also choose whether to share their purchases with family.

When users share a purchase through Family Sharing, each family member gets their own unique receipts and transactions. Process the transactions in the same way you already handle purchases — you don’t need any special logic for shared products. However, you do need to implement a new method in your transaction observer, and listen for a new notification type in server notifications. Specifically, to support Family Sharing, you need to:

- Enable Family Sharing for your Apple In-App Purchases in App Store Connect. For more information, see [Turn on Family Sharing for Apple In-App Purchases](https://help.apple.com/app-store-connect/#/dev45b03fab9).
- During runtime, check whether Apple In-App Purchases support Family Sharing using either  [`isFamilyShareable`](./product/isfamilyshareable.md) in [`Product`](./product.md) or [`isFamilyShareable`](./skproduct/isfamilyshareable.md) in [`SKProduct`](./skproduct.md). Then inform users when merchandising your subscriptions.
- Process purchased and restored transactions in your app. This is standard processing you already do for any purchases.
- Implement [`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md) in your transaction observer to handle conditions in which products are no longer shared.
- Listen for the `REVOKE` [`notification_type`](../AppStoreServerNotifications/notification_type.md) from [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md) on your server.

> **Related Sessions from WWDC20**:  Session 10661: [What’s new with Apple In-App Purchase](https://developer.apple.com/videos/play/wwdc2020/10661/)

### Enable Family Sharing for Apple In-App Purchases

To make Family Sharing available for an Apple In-App Purchase, developers need to turn on Family Sharing in App Store Connect. After you enable Family Sharing for an Apple In-App Purchase, you can’t turn it off. For more information, see [Turn on Family Sharing for Apple In-App Purchases](https://help.apple.com/app-store-connect/#/dev45b03fab9).

Users can choose whether to share their purchases with family. As users join or leave family groups and enable or disable sharing, your app needs to update the family’s access to your products. For information about how users manage their Family Sharing choices, see [Set Up Family Sharing on iPhone](https://support.apple.com/guide/iphone/set-up-family-sharing-iph223f61318/ios).

### Provide access to shared purchases

Your app receives a unique receipt for each family member entitled to a shared purchase, on each of their devices. For subscriptions, your app unlocks access through the normal purchase flow. For non-consumable products, unlocking access may require users to initiate a restored purchase, depending on the Family Sharing settings at the time of purchase.

To provide access for family members to a subscription or non-consumable, your app needs to handle purchased and restored transactions as usual. Specifically, follow these steps:

1. Set up a transaction observer at app launch so your app receives transactions that occur outside of your app, such as receiving a Family Sharing purchase. For more information on this best practice, see [Setting up the transaction observer for the payment queue](./setting-up-the-transaction-observer-for-the-payment-queue.md).
2. Verify the receipt. Look for a transaction in the latest receipt info array ([`responseBody.Latest_receipt_info`](../AppStoreReceipts/responsebody/latest_receipt_info-data.dictionary.md)) with the new Family Sharing purchase.
3. Handle purchased ([`SKPaymentTransactionState.purchased`](./skpaymenttransactionstate/purchased.md)) transactions. This is a standard state apps need to handle, and you don’t need anything special for Family Sharing. For shared subscriptions, the transaction always has a purchased state. For shared non-consumable products, the transaction has a purchased state if Family Sharing was enabled for the product at the time of the purchase. For more information about handling transactions, see [Processing a transaction](./processing-a-transaction.md).
4. Handle restored ([`SKPaymentTransactionState.restored`](./skpaymenttransactionstate/restored.md)) transactions, which is also a standard state apps need to handle. For shared non-consumable products, your app gets a restored transaction if developers enable Family Sharing after the user purchases the product. To gain access to the shared product, family members use your app’s restore functionality. For more information about restoring, see [Restoring purchased products](./restoring-purchased-products.md).
5. Unlock access to the shared subscription or non-consumable product.
6. Call [`finishTransaction(_:)`](./skpaymentqueue/finishtransaction%28_%29.md).

### Revoke access if Family Sharing is disabled

With Family Sharing products, users have access to products only while Family Sharing is enabled. If the purchaser leaves the group, gets a refund, or stops sharing, the expectation is that the family’s access to the product stops immediately.

When a condition occurs that disables sharing, StoreKit informs your app by updating the receipt, and then calling the [`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md) method of the [`SKPaymentTransactionObserver`](./skpaymenttransactionobserver.md) protocol. Implement this method on your transaction observer, and do the following:

1. Verify the receipt. Revoked products appear in the receipt with a `cancellation_date` field present.
2. Provide the app with access to all the products to which the user is entitled.

For more information, including a list of conditions that trigger this call, see [`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md).

### Listen for the revoke notification

If you set up your server to receive [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md), your server gets a `REVOKE` [`notification_type`](../AppStoreServerNotifications/notification_type.md) as soon as a shared purchase is no longer shared. This notification serves the same purpose as the [`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md)call. Listen for and process this notification by:

1. Checking the latest receipt ([`unified_receipt.Latest_receipt_info`](../AppStoreServerNotifications/unified_receipt/latest_receipt_info-data.dictionary.md)) in the response body. Revoked products appear in the receipt with a `cancellation_date` field present.
2. Providing the app with access to all products to which the user is entitled.
3. Updating your records, if you keep server-based records to manage your customers’ subscriptions.

### Indicate to users when products support Family Sharing

When your app displays Apple In-App Purchases, indicate in your UI whether users can share the product with family. Call [`isFamilyShareable`](./skproduct/isfamilyshareable.md) to determine at runtime whether the Apple In-App Purchase supports Family Sharing. Knowing whether a product is shareable helps users make a selection that best fits their needs.

## See Also

### Family Sharing
- [var isFamilyShareable: Bool](./skproduct/isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
- [func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers: [String])](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md)
  Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/supporting-family-sharing-in-your-app)*