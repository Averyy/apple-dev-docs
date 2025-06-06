# Testing resubscribing from the subscriptions page

**Framework**: StoreKit

Verify that your app can reactivate an expired subscription by receiving a transaction callback or inspecting an updated receipt.

#### Overview

Customers can manage their active subscriptions, as well as their expired subscriptions for up to a year after expiry, on the Subscriptions page in iOS, tvOS, iPadOS, and macOS. From this page, customers can upgrade, downgrade, cancel, or change the type of their subscriptions.

In this test scenario, the customer resubscribes to an expired subscription from the Subscriptions page in the App Store.

##### Set Up Testing

This test case requires one or more subscriptions configured in App Store Connect and an expired subscription for your Sandbox Apple Account. If you don’t already have an expired subscription, purchase an auto-renewable subscription and let it expire.

##### Begin Testing

To test resubscribing from the Subscriptions page:

1. On the test iOS device, open Settings > Developer.
2. In the Sandbox Account section, tap your highlighted Sandbox Apple Account, and tap Manage.
3. On devices running iOS 16 or later, tap Subscriptions on the Account Settings sheet.
4. In the sandbox Subscriptions page, select the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.
5. Select a subscription product to resubscribe to.
6. To complete the purchase, authenticate the payment sheet that appears.
7. Open your app.
8. In Xcode, verify that your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) gets a callback on [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) with a transaction in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state.
9. Check that your app retrieves and verifies the app receipt. Verify that the successful transaction is in the receipt.
10. Check that your app makes the in-app purchase available and updates the subscriber’s status.
11. In Xcode, check that your app calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md). For more information, see [`Finishing a transaction`](finishing-a-transaction.md).

##### Conclude Testing

This test case requires no cleanup. For auto-renewable subscriptions, you can perform the test again when the subscription expires.

## See Also

- [Testing an auto-renewable subscription](testing-an-auto-renewable-subscription.md)
  Verify that your app handles a subscription lapse properly using the accelerated time rates within the sandbox environment.
- [Testing disabling auto-renew](testing-disabling-auto-renew.md)
  Verify that your app receives subscription updates when a user cancels a subscription by verifying the receipt or receiving a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-resubscribing-from-the-subscriptions-page)*