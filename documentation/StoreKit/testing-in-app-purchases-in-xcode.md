# Testing In-App Purchases in Xcode

**Framework**: StoreKit

Use locally configured product data to test and debug your In-App Purchases implementation.

#### Overview

Testing your StoreKit implementation in Xcode ensures that your app behaves correctly when your customers perform various tasks associated with subscriptions and In-App Purchase transactions. Be sure to test a variety of in-app purchase scenarios, such as receipt validation, promotional offers, interrupted purchases, introductory offers, subscription renewals, and purchase restoration.

##### Perform Basic Setup

Before you begin StoreKit testing in Xcode, complete the steps in [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode), including creating a StoreKit configuration file, enabling StoreKit testing in Xcode, and preparing to validate receipts in the test environment. The test scenarios in this article require this basic setup.

Select the relevant test scenarios to build a test plan for your app. Each test scenario provides additional setup steps, if necessary, along with instructions about how to minimally reset the environment to repeat the test.

##### Validate a Receipt in the Test Environment

Validating receipts is an integral part of handling and testing in-app purchases. As you test in-app purchases, StoreKit in Xcode generates receipts that are valid only in the test environment. Your app can validate the receipts locally using a certificate that Xcode provides.

> ❗ **Important**:  You can’t validate receipts from the test environment with [`verifyReceipt`](https://developer.apple.com/documentation/appstorereceipts/verifyreceipt) because the App Store doesn’t sign these receipts, and the verification fails.

The test environment’s certificate is a root certificate. There’s no certificate chain to validate when you verify the receipt signature. The following code example retrieves the local receipt:

```swift
// Get the receipt if it's available.
if let appStoreReceiptURL = Bundle.main.appStoreReceiptURL,
    FileManager.default.fileExists(atPath: appStoreReceiptURL.path) {
    do {
        let receiptData = try Data(contentsOf: appStoreReceiptURL, options: .alwaysMapped)
        let receiptString = receiptData.base64EncodedString(options: [])
        // Add code to read receiptData.
    }
    catch { 
        print("Couldn't read receipt data: " + error.localizedDescription) }
}
```

For more information, see [`Validating receipts on the device`](https://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device).

##### Test a Promotional Offer

For this test scenario, let’s assume the app determines that customers are eligible for the promotional offer when the subscription expires. Use the test environment to speed up the time rate so the subscription expires. Then, you’re ready to test the offer eligibility logic in your app.

Additional setup steps for this test scenario are:

- Add a subscription offer to your StoreKit configuration file.
- In the app, purchase a subscription within the same subscription group to be eligible for a promotional offer.

Ensure your test user is eligible for the offer according to your app’s requirements, then purchase the subscription with the offer. Test users can redeem subscription offers if:

- They have an existing or expired subscription, including free, discount, or discounted with a subscription offers.
- They qualify for the offer according to criteria that you define.

See [`Implementing promotional offers in your app`](implementing-promotional-offers-in-your-app.md) for more information.

1. In Xcode, select the StoreKit configuration file in the Project navigator, and then choose Editor > Subscription Renewal Rate > Monthly Renewal Every 30 Seconds.
2. Wait until the subscription expires.
3. Reset the Subscription Renewal rate to Monthly Renewal Every 30 Minutes.
4. In the app, select the option to buy the subscription with the offer.
5. In your code, verify that the payment request includes the discount, [`paymentDiscount`](skpayment/paymentdiscount.md).
6. Observe that the system displays the payment sheet with the promotional offer.
7. In your code, verify that [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) receives the transaction in the [`SKPaymentTransactionState.purchasing`](skpaymenttransactionstate/purchasing.md) state.
8. In the app, tap Confirm on the payment sheet.
9. In your code, verify that [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) receives the transaction in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state.

To test the same promotional offer purchase again, delete the transaction. In Xcode, choose Debug > StoreKit > Manage Transactions. Select the transaction for the promotional offer purchase, and click Delete.

##### Test an Interrupted Purchase

An interrupted purchase is a transaction that requires the user to perform some action outside your app before the transaction can complete successfully. For example, the user may need to update a payment method or approve new terms and conditions. In Xcode, you can simulate a purchase interruption and its resolution to test how your code handles this scenario end-to-end. You can test this scenario for all in-app purchase product types.

1. In the Xcode Project navigator, select the StoreKit configuration file. Choose Editor > Enable Interrupted Purchases. Run the app in the simulator or on a device.
2. In the app, buy an in-app purchase.
3. Observe that the system displays the payment sheet in the app.
4. In your code, verify that your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) gets a callback on [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) with a transaction in the [`SKPaymentTransactionState.purchasing`](skpaymenttransactionstate/purchasing.md) state.
5. In the app, tap Confirm on the payment sheet.
6. In your code, observe that the payment fails (because you enabled interrupted purchases in the test environment). The payment queue receives a transaction in the [`SKPaymentTransactionState.failed`](skpaymenttransactionstate/failed.md) state.
7. Check that your code calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) to remove it from the queue.
8. In Xcode, choose Debug > StoreKit > Manage Transactions.
9. Select the transaction and click Resolve. The test environment resumes a successful purchase.
10. In your code, verify that the payment queue receives a transaction in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state for the same [`productIdentifier`](skproduct/productidentifier.md) in the same quantity as the failed transaction.
11. In your code, validate the receipt.
12. Check that your app provides the service or product, and then calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md).

To perform the test again for non-consumable products and subscriptions, delete the transaction to run the test again. To delete the transaction, choose Debug > StoreKit > Manage Transactions. Select the transaction and click Delete.

For consumable in-app purchases, you can test again without additional setup. To reset the test environment to its default behavior, select the StoreKit configuration file in Xcode, then choose Editor > Disable Interrupted Purchases.

##### Test an Introductory Offer

Customers are eligible to redeem an introductory offer one time. Configure an introductory offer for a subscription in your StoreKit configuration file. For more information, see [`Implementing introductory offers in your app`](implementing-introductory-offers-in-your-app.md).

Ensure that your app is eligible for an introductory offer by verifying there’s no subscription purchase for the product ID that includes the offer. Either verify the receipt in your code or check the transactions in Xcode by choosing Debug > StoreKit > Manage Transactions.

1. In the app, buy the subscription that has an introductory offer.
2. Observe that the system displays the payment sheet with the introductory offer in the app.
3. In your code, verify your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) receives a callback on [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) with the transaction in the [`SKPaymentTransactionState.purchasing`](skpaymenttransactionstate/purchasing.md) state.
4. In the app, tap Confirm on the payment sheet.
5. In your code, verify your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) receives a callback on [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) with the transaction in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state.
6. In your code, validate the receipt.
7. Check that your app provides the service or product, and then calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md).

To retry the same test scenario, delete the transaction that contains the introductory offer purchase. In Xcode, choose Debug > StoreKit > Manage Transactions. Select the transaction and click Delete. This resets the eligibility for the test user.

##### Test Restoring Purchases Without Existing Purchases

All apps need to provide a way for customers to restore purchases, such as by providing a Restore Purchases button. Test how your app handles this request when the customer has no existing purchases. For more information, see [`Restoring purchased products`](restoring-purchased-products.md).

Include at least one non-consumable product, auto-renewable subscription, or non-renewable subscription in the StoreKit configuration file. To simulate a user account with no in-app purchases, delete all the transactions before starting the test. In Xcode, choose Debug > StoreKit > Manage Transactions, select all the transactions, and click Delete.

1. In the app, select the option your app provides to restore purchases.
2. In your code, verify that it calls [`restoreCompletedTransactions()`](skpaymentqueue/restorecompletedtransactions().md) or [`restoreCompletedTransactions(withApplicationUsername:)`](skpaymentqueue/restorecompletedtransactions(withapplicationusername:).md).
3. In your code, verify that StoreKit notifies your observer that the restore is complete by calling [`paymentQueueRestoreCompletedTransactionsFinished(_:)`](skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:).md). Note that StoreKit doesn’t notify the queue of any restored transactions.

You can repeat this test scenario without additional steps.

##### Test Presenting the App Store Sheet for Managing Subscriptions

Your app can present an App Store sheet that customers can use to manage their subscriptions.

Additional setup steps for this test scenario are:

- Include two auto-renewable subscriptions that belong to the same subscription group in the StoreKit configuration file.
- Subscribe the sandbox user to the subscription with the lowest level of service in that subscription group.
- In the app, implement a Manage Subscriptions button that invokes the [`showManageSubscriptions(in:)`](appstore/showmanagesubscriptions(in:).md) or [`manageSubscriptionsSheet(isPresented:)`](https://developer.apple.com/documentation/SwiftUI/View/manageSubscriptionsSheet(isPresented:)) method.

See [`showManageSubscriptions(in:)`](appstore/showmanagesubscriptions(in:).md) and [`manageSubscriptionsSheet(isPresented:)`](https://developer.apple.com/documentation/SwiftUI/View/manageSubscriptionsSheet(isPresented:)) for more information.

1. In the app, tap the Manage Subscriptions button.
2. Observe that the system displays the App Store sheet for managing subscriptions.
3. Verify that the test user is a subscriber of the lower-grade subscription.
4. Upgrade the test user to the higher-grade subscription in that group.
5. Verify that the user is a subscriber of the higher-grade subscription.
6. Cancel the subscription and confirm it in the Confirm Cancellation dialog.
7. Verify that the user is no longer a subscriber of any subscription.

You can repeat this test scenario without additional steps.

##### Test an Offer Code

Your app can present a sheet to redeem preconfigured subscription offer codes.

Additional setup steps for this test scenario are:

- Include one auto-renewable subscription in the StoreKit configuration file.
- Configure an offer code for the above subscription in your StoreKit configuration file under the Offer Codes heading.
- In the app, implement a Redeem Offer Code button that invokes the [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) method.

See [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) for more information.

1. In the app, tap the Redeem Offer Code button.
2. Observe that the system displays the Redeem Offer Code sheet.
3. Select the offer code that you configured and redeem it.
4. Observe that the system displays the payment sheet with the applied offer.
5. In the app, tap Confirm on the payment sheet.
6. In your code, verify your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) receives a callback on [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) with the transaction in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state.
7. Check that your app provides the service or product, and then calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md).

To retry the same test scenario, delete the transaction that contains the offer code purchase. In Xcode, choose Debug > StoreKit > Manage Transactions. Select the transaction and click Delete.

##### Test Billing Retry and Grace Period for Auto Renewable Subscriptions

When billing for a subscription renewal fails, such as due to an expired card, the App Store retries billing and attempts to recover the subscription. You can enable a billing grace period for your app in App Store Connect so your subscribers can continue accessing paid content while the App Store retries billing. For more information about the billing grace period, see [`Reducing Involuntary Subscriber Churn`](reducing-involuntary-subscriber-churn.md).

Test these scenarios in Xcode to ensure your app detects subscriptions that are in billing retry or billing grace period states. In your code, look at the [`renewalInfo`](product/subscriptioninfo/status-swift.struct/renewalinfo.md) for the subscription to inspect its [`Product.SubscriptionInfo.RenewalState`](product/subscriptioninfo/renewalstate.md). For subscriptions in a billing grace period state, ensure your app continues to provide uninterrupted subscription features.

Additional setup steps for this scenario are:

- Choose Editor > Enable Billing Grace Period. This step simulates enabling the billing grace period for your app in App Store Connect. To test billing retry without a billing grace period, leave this setting disabled.
- Choose Editor > Enable Billing Retry on Renewal. This step causes all subscription renewals to go into a billing retry state.
- Select your StoreKit configuration file in the Project navigator.
- Create an auto-renewable subscription in-app purchase in your StoreKit configuration file.
- Purchase the auto-renewable subscription in your app.
- Adjust the time rate of subscription renewals in the testing environment by choosing Editor > Subscription Renewal Rate, and select an option. For more information about the time rates available in the testing environment, see [`timeRate`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/timeRate-swift.property).

Test your app’s handling of a billing grace period:

1. In the testing environment, wait for the subscription period to elapse. The subscription goes into a billing retry state and a billing grace period.
2. Run your app, then choose Debug > StoreKit > Manage Transactions.
3. Find and select the subscription transaction.
4. Verify the subscription transaction is in the billing grace period state.
5. Test your app to verify that it supports the billing grace period by continuing to provide uninterrupted access to the features the subscription provides.

Test your app’s handling of a billing grace period expiration:

1. In the testing environment, wait until the billing grace period elapses for the subscription.
2. Run your app, then choose Debug > StoreKit > Manage Transactions.
3. Find and select the subscription transaction.
4. Verify the subscription transaction is in the billing retry state, and is no longer in the billing grace period state.
5. Test your app to verify that it works consistently with a subscription expiration.

Test resolving a billing issue for billing retry, either with a billing grace period or without:

1. In the testing environment, wait for the subscription period to elapse. Verify your app works consistently with a subscription expiration if you’re not testing a billing grace period.
2. Run your app, then choose Debug > StoreKit > Manage Transactions.
3. Find and select the subscription transaction.
4. Verify the subscription transaction is in either the billing grace period state or the billing retry state.
5. Click the Resolve Issues button to resolve the billing issue.
6. Test your app to verify that it provides access to the subscription features as you expect.

##### Test Price Increase Consent

When you increase the price of an auto-renewable subscription by an amount that requires user consent, the App Store gives the user an opportunity to consent to the price increase by presenting a sheet in your app. Your app may defer presentation of the sheet to prevent it from appearing at an inconvenient time in the user interface. Users may also consent to a price increase outside your app. Test these scenarios in Xcode to verify that your app handles deferring or displaying the sheet.

Additional setup steps for this scenario are:

- Create an auto-renewable subscription purchase in your StoreKit configuration file.
- Purchase the subscription in your app.
- Optionally, increase the price for your subscription in your StoreKit configuration file. You can still test this scenario without increasing the price.

Test for the deferred price increase consent sheet presentation:

1. Navigate to a place in your app where you defer presentation of the price increase consent sheet.
2. Run your app, then choose Debug > StoreKit > Manage Transactions.
3. Find and select the subscription transaction.
4. Click Request Price Increase Consent.
5. Verify that the price increase consent sheet doesn’t display in your app.
6. Navigate away from the view where you defer presentation.
7. Verify that the price increase consent sheet displays in your app.
8. On the price increase consent sheet in the app, select the Agree to New Price button to test a user consenting to the price increase, or select Close to test the user not giving consent for the price increase.

Test for the price increase consent sheet presentation:

1. Navigate to a place in your app where you don’t defer presenting the price increase consent sheet.
2. In the StoreKit transaction manager, select the subscription purchase, then click Request Price Increase Consent.
3. Verify that the price increase consent sheet displays in your app.
4. On the price increase consent sheet in the app, select the Agree to New Price button to test a user consenting to the price increase, or select Close to test the user not giving consent for the price increase.

For information about testing price increase consent in an automated test suite, see [`requestPriceIncreaseConsentForTransaction(identifier:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)), [`consentToPriceIncreaseForTransaction(identifier:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)), and [`declinePriceIncreaseForTransaction(identifier:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)).

## See Also

- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md)
  Prepare your test environment to test in-app purchases with data you configure locally.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)
  Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-in-xcode)*