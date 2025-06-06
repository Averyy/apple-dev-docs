# Testing win-back offers in Xcode

**Framework**: Storekit

Validate your app’s handling of win-back offers that you configure for the testing environment.

#### Overview

A win-back offer is an offer for a discount on an auto-renewable subscription to a customer who was previously subscribed.

To test win-back offers in Xcode, first set up your StoreKit configuration file with auto-renewable subscriptions and win-back offers. Subscribe to an auto-renewable subscription with one or more win-back offers. Then, cancel the subscription and allow it to expire. If the win-back offer’s setting is Eligible, the testing system makes the win-back offer available to redeem immediately after the subscription expires.

Testing win-back offers in Xcode is convenient early in the development process, because it doesn’t rely on any product configurations in App Store Connect. However, you can also test win-back offers in the sandbox environment, which does rely on your App Store Connect configuration. For more information, see [`Testing win-back offers in the sandbox environment`](testing-win-back-offers-in-the-sandbox-environment.md).

##### Perform Basic Setup

Before you can begin testing in Xcode, complete the steps in [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode), including creating a StoreKit configuration file and enabling StoreKit testing in Xcode.

##### Configure Win Back Offers for Testing

Start by opening the StoreKit configuration editor in Xcode and defining at least one auto-renewable subscription and subscription group. Then follow these steps to configure one or more win-back offers:

1. In the left pane, select the subscription under the Auto-Renewable Subscriptions heading.
2. Under the Win-back Offers heading in the editor, click the Add button (+) to configure a new offer by filling out the offer details as follows, and then clicking Save.

> **Note**:  The eligibility criteria that determine whether a customer can redeem a win-back offer can have many rules and states. Rather than requiring you to construct all the conditions before you can test win-back offers in your app, the testing UI provides a simplified Eligible or Not Eligible setting that bypasses any other eligibility criteria. Set the value to Eligible to test your app’s response when a customer receives a win-back offer.

##### Run the Test

To display a win-back offer, run your app in the Xcode environment and follow these steps:

1. In your app, subscribe to an auto-renewable subscription that has at least one win-back offer.
2. In the StoreKit configuration, set the Eligibility setting for the win-back offer to Eligible.
3. Cancel the subscription. If your app implements subscription management, such as by calling [`showManageSubscriptions(in:)`](appstore/showmanagesubscriptions(in:).md), cancel the subscription through your app. Otherwise, use the transaction manager in Xcode by choosing Debug > StoreKit > Manage Transactions, selecting the subscription transaction, and turning off the auto-renew option.
4. Wait for the canceled subscription to expire. The system makes the win-back offer available to redeem as soon as the subscription expires.
5. In your app, open your store. Examine your app’s implementation of the win-back offer. For example, if your app uses [`StoreKit views`](storekit-views.md), the eligible offers appear automatically when your app displays a [`SubscriptionStoreView`](subscriptionstoreview.md).

For more information about using the transaction manager, see [`Testing in-app purchases with StoreKit transaction manager in Xcode`](https://developer.apple.com/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code).

##### Reset or Rerun the Test

You can rerun the test without resetting any state values. Win-back offers that you set to be Eligible appear as soon as their related subscriptions expire.

## See Also

- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)
  Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/testing-win-back-offers-in-xcode)*