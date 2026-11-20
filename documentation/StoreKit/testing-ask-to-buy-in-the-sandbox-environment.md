# Testing Ask to Buy in the sandbox environment

**Framework**: StoreKit  
**Role**: Article

Verify that your app handles Ask to Buy purchases, including those made outside your app.

## Overview

To test the Ask to Buy flow, including approving and declining requests, sign in to a Sandbox Apple Account on a device running iOS 27.2 or later or iPadOS 27.2 or later. For information on creating and signing in to a Sandbox Apple Account, see [Create a Sandbox Apple Account](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids) and [Testing Apple In-App Purchases with sandbox](./testing-in-app-purchases-with-sandbox.md). With Ask to Buy, when a child tries to make a purchase, the system sends a request to their parent or guardian, who approves or declines it. For more information about the feature, see [Approve what kids buy with Ask to Buy](https://support.apple.com/105055).

In the sandbox environment, you can start Ask to Buy in two ways:

- **Account level**: A setting that applies to every purchase by a Sandbox Apple Account. When you turn on Enable Ask to Buy, every purchase that the account makes on any device requires approval. Turn off the setting to return the account to its usual purchasing behavior.
- **Single purchase**: A purchase option that puts one purchase into the pending state. Pass the [`simulatesAskToBuyInSandbox(_:)`](./product/purchaseoption/simulatesasktobuyinsandbox%28_%29.md) purchase option when you call [`purchase(options:)`](./product/purchase%28options%29.md). If you’re signed in to a Sandbox Apple Account, you can then approve or decline the request in Account Settings.

You can’t approve or decline an Ask to Buy request without signing into a Sandbox Apple account, but you can use the single-purchase option to test the pending state without signing in. For example, when you’re testing an app that you download from TestFlight, if `simulatesAskToBuyInSandbox` is an option for a purchase and you try to make a purchase then select Ask in the Ask Permission dialog, the purchase enters the [`Product.PurchaseResult.pending`](./product/purchaseresult/pending.md) state.

You approve or decline each request on the Ask to Buy page in Account Settings page. If you’re signed in to a Sandbox Apple Account, the page lists requests from purchases that you make while Enable Ask to Buy is on and from purchases that use the [`simulatesAskToBuyInSandbox(_:)`](./product/purchaseoption/simulatesasktobuyinsandbox%28_%29.md) purchase option. Each request shows the product name, the request date, and Decline and Approve buttons. To open the page, go to Settings > Developer, select the Sandbox Apple Account, tap Manage, then select Ask to Buy.

When a purchase needs approval, every iPhone and iPad where you’re signed in to the Sandbox Apple Account receives a push notification. Tap the notification on any of those devices to open the Account Settings page, select Ask to Buy, then tap Approve or Decline for the request. For example, attempt a purchase in your tvOS app, then approve it on your iPhone.

You can also test Ask to Buy in Xcode. For more information, see [Testing Ask to Buy in Xcode](./testing-ask-to-buy-in-xcode.md).

### Turn on Ask to Buy for a Sandbox Apple Account

Before you begin, create a Sandbox Apple Account and sign in to it on your test device. For more information, see [Create a Sandbox Apple Account](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids) and [Testing Apple In-App Purchases with sandbox](./testing-in-app-purchases-with-sandbox.md).

On the device, turn on the setting:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account.
3. Tap Manage. The Account Settings page appears.
4. Select Ask to Buy.
5. Tap to turn on Enable Ask to Buy.

### Test a purchase that awaits approval

Treat an approved Ask to Buy purchase like any other transaction. A parent or guardian can respond at any time, so the transaction can arrive while your app isn’t active. StoreKit delivers it through the [`updates`](./transaction/updates.md) asynchronous sequence in [`Transaction`](./transaction.md), the same way it delivers purchases made outside your app. For more information, see [Testing purchases made outside your app](./testing-purchases-made-outside-your-app.md).

To test a purchase that’s awaiting approval:

1. Choose how to start Ask to Buy. To test it on every purchase, complete the steps in [Turn on Ask to Buy for a Sandbox Apple Account](./testing-ask-to-buy-in-the-sandbox-environment.md#Turn-on-Ask-to-Buy-for-a-Sandbox-Apple-Account). To test it on a specific purchase without turning on Enable Ask to Buy, pass the [`simulatesAskToBuyInSandbox(_:)`](./product/purchaseoption/simulatesasktobuyinsandbox%28_%29.md) purchase option when you call [`purchase(options:)`](./product/purchase%28options%29.md).
2. In your app, attempt to purchase the Apple In-App Purchase.
3. Select Ask in the Ask Permission dialog. The system indicates that the purchase needs approval instead of completing it.
4. In your code, check that [`purchase(options:)`](./product/purchase%28options%29.md) returns [`Product.PurchaseResult.pending`](./product/purchaseresult/pending.md).
5. Confirm that your app doesn’t unlock the content.

### Approve a request and confirm your app unlocks the content

Approve a request, then check that your app delivers the purchase:

1. Complete the [Test a purchase that awaits approval](./testing-ask-to-buy-in-the-sandbox-environment.md#Test-a-purchase-that-awaits-approval) steps.
2. Tap the Ask to Buy push notification on any iPhone or iPad where you’re signed in to the Sandbox Apple Account to open the Account Settings page, then select Ask to Buy. You can also open Settings > Developer, select the Sandbox Apple Account, tap Manage, then select Ask to Buy.
3. Find a request for the product you attempted to purchase, then tap Approve.
4. To confirm the approval, authenticate in the dialog that appears.
5. Open or return to your app. StoreKit delivers the transaction through the [`updates`](./transaction/updates.md) asynchronous sequence.
6. Confirm that your app verifies the transaction, unlocks the content, and calls [`finish()`](./transaction/finish%28%29.md).

StoreKit doesn’t report a declined Ask to Buy request. If you tap Decline, your app doesn’t receive any information, so don’t show the pending state in your app’s interface. Requests remain on the Ask to Buy page until you respond to them. If you attempt to purchase the same product several times before responding, the page lists a separate request for each attempt. When you approve or decline one of them, the other requests for that product disappear from the page.

## See Also

### Payment transactions
- [Testing purchases made outside your app](./testing-purchases-made-outside-your-app.md)
  Verify that your app receives and handles transactions that occur outside your app, such as subscription purchases, renewals, and offer and promo code redemptions.
- [Testing win-back offers in the sandbox environment](./testing-win-back-offers-in-the-sandbox-environment.md)
  Verify that your app receives and handles win-back offer transactions, including those made outside your app.
- [Testing an interrupted purchase](./testing-an-interrupted-purchase.md)
  Verify that your app handles an interrupted purchase by inspecting and invoking payment transactions.
- [Testing failing subscription renewals and Apple In-App Purchases](./testing-failing-subscription-renewals-and-in-app-purchases.md)
  Verify that your app handles failed subscription renewals that are in the billing retry or billing grace period states, as well as failed Apple In-App Purchases.
- [Testing a payment request](./testing-a-payment-request.md)
  Verify that requests for payment function properly in the sandbox environment by inspecting the calls to the payment transaction observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-ask-to-buy-in-the-sandbox-environment)*