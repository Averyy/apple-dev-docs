# Handling Subscriptions Billing

**Framework**: StoreKit

Build logic around the date and time constraints of subscription products, while planning for all scenarios where you control access to content.

#### Overview

Apps that offer subscriptions have some unique behaviors and considerations. Because subscriptions involve an element of time, your app must be able to determine whether the subscription is currently active and determine the subscription states for past dates. Your app must also react to new, renewed, and lapsed subscriptions, and properly handle expired auto-renewable subscriptions that may be in a billing retry state.

To validate changes in and identify the status of a subscription, you can use the different values in the receipt, which provides details on app and in-app purchases. For information about server-side receipt validation, see [`Validating receipts with the App Store`](validating-receipts-with-the-app-store.md).

> **Note**:  Each subscription has a unique product identifier associated with a single app. Apps with an iOS and a macOS version have separate products, with a unique product identifier on each platform. You could let users who have a subscription in an iOS app access the content from a macOS app, or vice versa, but implementing that functionality is your responsibility. In order to support cross-platform subscription products, you would need a system to identify users and keep track of the content to which they subscribe. For more information, see [`Offering a Subscription Across Multiple Apps`](offering-a-subscription-across-multiple-apps.md).

There are two types of subscriptions you can offer in your app:  and . Non-renewing subscriptions differ from auto-renewable subscriptions in a few key ways. These differences give your app the flexibility to implement the correct behavior for a non-renewing subscription, as follows:

- Your app is responsible for calculating the time period that the subscription is active and determining what content needs to be made available to the user.
- Your app is responsible for detecting that a non-renewing subscription is approaching its expiration date and prompting the user to renew the subscription by purchasing the same product again.
- Your app is responsible for making purchased subscriptions available across all the user’s devices and for letting users restore past purchases. For example, most subscriptions are provided by a server; your server would need some mechanism to identify users and associate subscription purchases with the user who purchased them.

The following sections provide guidance for handling auto-renewable subscriptions. To quickly react to changes in users’ auto-renewable subscriptions, you can choose to receive status update notifications on your server. Status update notifications inform you of real-time changes in a user’s subscription status and are only supported for auto-renewable subscriptions. For more information on setting up and handling server notifications, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md).

##### Calculate a Subscriptions Promotional Offer Status

You can set up promotional offers in App Store Connect to provide users with free or discounted service for a subscription. All new and eligible subscribers can redeem an introductory offer, and all lapsed and existing subscribers can redeem a subscription offer. There are multiple types of introductory and subscription offers, each with different billing cycles. Customers who redeem a free trial introductory offer or a downgrade subscription offer will not be billed for the subscription until the end of the free trial period. For more information, see [`Implementing introductory offers in your app`](implementing-introductory-offers-in-your-app.md) and [`Implementing promotional offers in your app`](implementing-promotional-offers-in-your-app.md).

Check the `is_in_intro_offer_period` or `is_trial_period` field from each receipt entry to validate whether the user redeemed an introductory offer at the beginning of their subscription. You can use this information to accurately present subscription products from the same subscription group at the end of the introductory offer period for that user. Check the `promotional_offer_id` field from each receipt entry to validate whether the user redeemed a subscription offer. You can use this information to determine eligibility for this user to redeem subscription offers in the future.

##### Calculate a Subscriptions Active Period

Your app needs to determine which content the user has access to based on the period of time their auto-renewable subscription is active. To provide the customer access to the content to which they are entitled, keep a record of the date that each piece of content is published. Read the `original_purchase_date`, `purchase_date`, and `expires_date` field from each receipt entry to determine the start and end dates of each subscription period. The user has access to all content published between each subscription start and end date in addition to the content that was initially unlocked when the subscription was purchased.

For example, because purchasing a subscription always unlocks content, a user who purchases a monthly subscription mid-month to a magazine that publishes a new issue on the first day of every month gets access to two issues in their first month of subscribing: the most recently published issue, which is unlocked at the time that the subscription is purchased, and the issue you publish on the subsequent first day of the month, which is unlocked at the time you publish it.

> ❗ **Important**:  Don’t calculate the subscription period by adding a subscription duration to the purchase date. That approach fails to take into account the free trial period, the marketing opt-in period, and the content made available immediately after the user purchased the subscription.

If the subscription lapsed, there will be multiple periods of time during which the subscription was active, and there will be pieces of content unlocked at the beginning of a subscription period. To identify lapses in a subscription, compare the `expires_date` field from each receipt entry to the `purchase_date` field of the previous receipt entry for all entries in the receipt.

##### Detect an Expiration or Renewal

The subscription renewal process begins in the 10 days before the expiration date. During those 10 days, the App Store checks for any billing issues that might delay or prevent the subscription from being automatically renewed, for example, whether:

- The customer’s payment method is active.
- The product increased in price since the user bought the subscription.
- The product is no longer available.

The App Store notifies users of any issue so that they can resolve it before the subscription expires and avoid an interruption in their service.

During the 24-hour period before the subscription expires, the App Store starts trying to renew it automatically. The App Store makes several attempts to automatically renew the subscription over a period of time but eventually stops if there are too many failed attempts.

##### Handle Lapsed Subscriptions

The App Store renews the subscription slightly before it expires, to prevent any lapse in the subscription. However, lapses are still possible. For example, if the user’s payment information is no longer valid, the first renewal attempt fails. Billing-related issues trigger the subscription to enter a billing retry state where the App Store attempts to renew the subscription for up to 60 days. You can check the `expiration_intent` and `is_in_billing_retry_period` values to monitor the retry status of the subscription. During this period, your app may optionally offer a grace period to the user and show them a message in the app to update their payment information. Additionally, your app can deep link customers to the payment details page within App Store on their device by opening this URL

```http
https://apps.apple.com/account/billing
```

The user can also cancel their subscription by disabling auto-renew and intentionally letting their subscription lapse. This action triggers the App Store to send your server a status update notification of type `DID_CHANGE_RENEWAL_STATUS`. Your server can parse the `auto_renew_status` and the `auto_renew_status_change_date` to determine the current renewal status of the subscription.

You can also check the `expiration_intent` field in the receipt to further validate the reason for the subscription to lapse. Make sure your app’s subscription logic can handle different values of `expiration_intent` along with `expires_date` to show the appropriate message to the user.

##### Detect a Refund

Users pay for a subscription when they purchase it, and they can receive a refund by contacting Apple customer service. For example, if the user accidentally buys the wrong product and requests a refund, customer support can cancel the subscription and issue a full or partial refund. Customers may cancel a subscription in the middle of a subscription period, but the subscription remains paid through the end of the same period. Additionally, users may also receive a refund when they upgrade their subscription to another subscription product at a higher level in the same subscription group.

To identify whether a subscription has been refunded, look for the `cancellation_date` field in the receipt. The App Store notifies your server of refunds with a status update notification of type `CANCEL`, at which point you can handle the refund. For example, if the user upgraded the subscription, immediately unlock service for the higher level subscription product purchased.

##### Identify a Renewed Subscription After a Lapse

A user-initiated payment information update for an auto-renewable subscription in the billing retry period triggers an automatic renewal attempt to succeed. For this event, the App Store notifies your server with a notification of type `RENEWAL` and a new receipt will be generated for the successful transaction. You can look for a new value of the `expires_date` field to know the next renewal date of the subscription.

StoreKit adds a new transaction for the renewal to the transaction queue on the device. Your app can check the transaction queue on launch and handle the renewal the same way as any other transaction. If your app is already running when the subscription renews, the transaction observer is not called; your app finds out about the renewal the next time the app launches.

##### Detect Upgrades or Plan Changes

Users can manage their auto-renewable subscriptions in their App Store settings on-device or within your app’s interface. For each subscription purchased by the user, the App Store shows all the renewal options that the subscription group offers. Users can easily change their service levels and choose to upgrade, downgrade, or cross-grade as often as they like. Upgrades of any duration or cross-grades with same durations go into effect immediately. Downgrades of any duration or cross-grades with different durations go into effect at the next renewal date.

You can check the receipt’s `auto_renew_product_id` field to learn about any plan changes the user selected that will go into effect at the next renewal date. Additionally, you can also use the notification of type `DID_CHANGE_RENEWAL_PREF` to get notified for any user initiated plan changes that will go into effect at the next renewal date.

##### Manage Subscription Price Consent

When you increase the price of a subscription, the App Store informs the affected subscribers with an email, push notification, and in-app price consent sheet, and asks your subscribers to agree to the new price. In the app, the system asks your delegate’s function [`paymentQueueShouldShowPriceConsent(_:)`](skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(_:).md) whether to immediately display the price consent sheet, or to delay displaying the sheet until later. For example, you may want to delay showing the sheet if it would interrupt a multistep user interaction, such as setting up a user account. Return `false` in [`paymentQueueShouldShowPriceConsent(_:)`](skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(_:).md) to prevent the dialog from displaying immediately.

To show the price consent sheet after a delay, call [`showPriceConsentIfNeeded()`](skpaymentqueue/showpriceconsentifneeded().md), which shows the sheet only if the user hasn’t responded to the price increase notifications.

If users don’t agree to the subscription price increase or take no action, their subscription expires at the end of their current billing cycle. App Store attempts to notify users in the app twice. For a notification schedule, see [`Increase the price of an auto-renewable subscription`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devc9870599e).

> **Note**:  The price consent sheet appears only on devices running iOS. All affected subscribers receive an email and push notification.

##### Enable Users to Manage Subscriptions

Consider building auto-renewable subscription management UI in the app for subscribers to easily move between different subscription levels in their subscription group. Use the [`subscriptionGroupIdentifier`](skproduct/subscriptiongroupidentifier.md) property of `SKProduct` to determine which products to display in the UI. For users who wish to cancel their subscription, your app can open the following URL:

```http
https://apps.apple.com/account/subscriptions
```

Opening this URL launches iTunes or iTunes Store and displays the Manage Subscriptions page where the user can upgrade, downgrade, or cancel their subscription by disabling auto-renew. If you configure your backend server to receive status update notifications, your server receives a `DID_CHANGE_RENEWAL_STATUS` notification if the user cancels their subscription.

## See Also

- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Offering a Subscription Across Multiple Apps](offering-a-subscription-across-multiple-apps.md)
  Support a single auto-renewable subscription across multiple apps.
- [Reducing Involuntary Subscriber Churn](reducing-involuntary-subscriber-churn.md)
  Prevent unintentional loss of subscribers due to billing issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/handling-subscriptions-billing)*