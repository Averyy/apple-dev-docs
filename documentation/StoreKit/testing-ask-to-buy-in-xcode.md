# Testing Ask to Buy in Xcode

**Framework**: StoreKit

Validate your app’s handling of Ask To Buy in the testing environment.

#### Overview

With Ask to Buy, when a child wants to make an eligible purchase or download, the system sends the purchase request to the parent or guardian. For more information, see [`Approve what kids buy with Ask to Buy`](https://developer.apple.comhttps://support.apple.com/105055).

You can test approving and declining Ask to Buy purchases in the Xcode testing environment. Use the StoreKit configuration file to set up and control the test case.

##### Perform Basic Setup

Before you can begin testing in Xcode, complete the steps in [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode), to create a StoreKit configuration file and enable StoreKit testing in Xcode.

##### Enable Ask to Buy for Testing

Open the StoreKit configuration editor in Xcode and define at least one in-app purchase. Then follow these steps in the StoreKit configuration editor:

1. In the left pane, select Configuration Settings.
2. Under the Purchase Options heading in the editor, enable Ask to Buy.

##### Test Approving a Purchase

To test approving a purchase, run your app in the Xcode environment and follow these steps:

1. In your app, attempt to purchase the in-app purchase.
2. When the Ask Permission dialog appears, select Ask.
3. In the Xcode StoreKit transaction manager, notice that the Pending Approval purchase appears with a state of Pending Ask to Buy. In your code, verify the purchase state is [`Product.PurchaseResult.pending`](product/purchaseresult/pending.md).
4. Control-click the transaction and select Approve.
5. In the Xcode StoreKit transaction manager, verify that the state is now Ask to Buy Approved. In your code, verify the purchase state is [`Product.PurchaseResult.success(_:)`](product/purchaseresult/success(_:).md).
6. Check that the app unlocks the content and finishes the transaction.

##### Test Declining a Purchase

To test declining a purchase, run your app in the Xcode environment and follow these steps:

1. In your app, attempt to purchase the in-app purchase.
2. When the Ask Permission dialog appears, select Ask.
3. In the Xcode StoreKit transaction manager, notice that the Pending Approval purchase appears with a state of Pending Ask to Buy. In your code, verify the purchase state is [`Product.PurchaseResult.pending`](product/purchaseresult/pending.md).
4. Control-click the transaction and select Decline.
5. In the Xcode StoreKit transaction manager, verify that the state is now Ask to Buy Declined. Your app doesn’t receive a transaction because you declined Ask to Buy.

For more information about using the transaction manager, see [`Testing in-app purchases with StoreKit transaction manager in Xcode`](https://developer.apple.com/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code).

##### Reset or Rerun the Test

You can run the same test again without resetting state values. When you’re done, turn off Ask to Buy to prevent it from affecting future tests.

## See Also

- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)
  Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md)
  Validate your app’s handling of win-back offers that you configure for the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-ask-to-buy-in-xcode)*