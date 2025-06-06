# Testing purchases made outside your app

**Framework**: StoreKit

Verify that your app receives and handles transactions that occur outside your app, such as subscription purchases, renewals, and offer and promo code redemptions.

#### Overview

When your app offers In-App Purchases, customers typically buy the products from within your app. However, purchase transactions can also occur on another device or even outside your app. Your app needs to handle these transactions when it launches. Use the Test Transactions feature in Account Settings in iOS to simulate and test such transactions in the sandbox environment.

##### Simulate a Variety of Purchase Events

Several types of events result in a purchase transaction that occurs outside your app, including the following:

All of these events result in StoreKit sending a transaction to your app through the [`updates`](transaction/updates.md) asynchronous sequence in [`Transaction`](transaction.md). Test your app to be sure it receives and handles the transaction.

##### Set Up a Test in Account Settings

To create a transaction outside your app for the testing environment, first open Account Settings on the iOS device, as follows:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account. If you’re not yet signed in, see [`Sign in to your Sandbox Apple Account for a development-signed app`](testing-in-app-purchases-with-sandbox#Sign-in-to-your-Sandbox-Apple-Account-for-a-development-signed-app.md).
3. Select Manage on the pop-up sheet. The Account Settings page appears.
4. Check that the Allow Purchases & Renewals toggle remains selected. If it’s deselected, all purchases fail, which represents a different test case. For more information, see [`Testing failing subscription renewals and In-App Purchases`](testing-failing-subscription-renewals-and-in-app-purchases.md).

Next, you need the product ID for a product you set up in App Store Connect and your app’s bundle ID. If you’re testing win-back offers, see [`Testing win-back offers in the sandbox environment`](testing-win-back-offers-in-the-sandbox-environment.md) for further steps.

> **Note**:  Changes that you make to product metadata in App Store Connect can take up to one hour to appear in the sandbox environment.

 Changes that you make to product metadata in App Store Connect can take up to one hour to appear in the sandbox environment.

##### Simulate a Purchase Outside Your App

To simulate a purchase outside your app, follow these steps:

1. On the Account Settings page, select Test Transactions.
2. Enter your product ID and the bundle ID in the applicable text boxes.
3. Select Test Transactions.
4. The system presents the App Store [Sandbox] payment sheet for the sandbox environment. Confirm the purchase. The sandbox environment doesn’t process actual payments. Instead, it returns transactions as if the system successfully processes them.

After you confirm the purchase, use the following steps to test your app:

1. Open your app. The system delivers the new transaction to your app through the [`updates`](transaction/updates.md) asynchronous sequence in [`Transaction`](transaction.md).
2. Confirm that your app receives and processes the transaction to provide access to the purchased product.

##### Conclude or Restart a Test

You can repeat the test by purchasing the product again through the Test Transactions feature in Account Settings. To repurchase some products, you might first need to clear the transactions for the Sandbox Apple Account, following these steps:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account.
3. Select Manage on the pop-up sheet.
4. On the Account Settings page, select Clear Purchase History.

Restart your app. The purchase history for the Sandbox Apple Account is empty and ready for testing. Clearing the purchase history for Sandbox Apple Accounts with a high number of purchases may take longer.

## See Also

- [Testing win-back offers in the sandbox environment](testing-win-back-offers-in-the-sandbox-environment.md)
  Verify that your app receives and handles win-back offer transactions, including those made outside your app.
- [Testing an interrupted purchase](testing-an-interrupted-purchase.md)
  Verify that your app handles an interrupted purchase by inspecting and invoking payment transactions.
- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)
  Verify that your app handles failed subscription renewals that are in the billing retry or billing grace period states, as well as failed In-App Purchases.
- [Testing a payment request](testing-a-payment-request.md)
  Verify that requests for payment function properly in the sandbox environment by inspecting the calls to the payment transaction observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-purchases-made-outside-your-app)*