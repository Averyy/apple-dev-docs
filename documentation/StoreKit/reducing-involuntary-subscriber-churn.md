# Reducing Involuntary Subscriber Churn

**Framework**: StoreKit

Prevent unintentional loss of subscribers due to billing issues.

#### Overview

After acquiring new customers for your subscription service, you can minimize subscriber loss, known as churn, by keeping them engaged as active subscribers. However, irregular billing events can occur throughout the lifecycle of a subscription that can impact your customer’s subscription status.

Involuntary churn occurs when users do not intend to leave your service but their subscription fails to renew, usually due to billing issues. Because involuntary churn is not related to customer satisfaction, consider creating a user experience that avoids subscriber loss due to a failed renewal. For business guidance on retaining subscribers, see [`Keeping Subscribers`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#keeping-subscribers).

Billing-related issues trigger a subscription to automatically enter a billing retry state, where the App Store attempts to recover the subscription. While the App Store tries to recover these customers, you have the option to prompt users to update their billing information or implement a grace period, or both, to assist in recovery efforts. Enabling a grace period and providing uninterrupted service provides a great customer experience, and avoids interrupting your days of paid service and revenue loss if Apple is able to recover the subscription within the grace period. For information on auto-renewable subscription proceeds and days of paid service, see [`Net Revenue After a Year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

##### React to Billing Issues

If the customer’s billing is invalid, the renewal fails and the user’s subscription enters a billing retry state, where the App Store attempts to collect payment for up to 60 days. This billing retry lowers the rate of involuntary churn and prevents the need to re-acquire subscribers if they churned. If the user is recovered within the 60 days, the new billing date is established on the date of recovery and subsequent renewal dates are based on this new billing date, as shown in the figure below.

![An example timeline for a monthly subscription that goes into a billing retry state and is recovered within 60 days. When the user is recovered, the next subscription renewal date shifts to the date the customer is billed.](https://docs-assets.developer.apple.com/published/9ea262f4c44fd5499f800f6531d3e456/media-3382824%402x.png)

For example, if the user’s payment information is no longer valid, the first renewal attempt fails. If you have server-to-server notifications enabled, you receive a server notification of type `DID_FAIL_TO_RENEW`. You can check the `expiration_intent` and `is_in_billing_retry_period` values in the [`verifyReceipt`](https://developer.apple.com/documentation/AppStoreReceipts/Verify-Receipt) response or [`unified_receipt`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt) object in the server notification to validate the reason for the subscription to lapse and monitor the retry status of the subscription. If the user is recovered during this period, you receive a server notification of types `RENEWAL` and `DID_RECOVER` when the retry is successful. For more information on server-to-server notifications, see [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications).

> ❗ **Important**:  The `RENEWAL` notification type is scheduled for deprecation. Update any existing code to rely on the identical `DID_RECOVER` notification type instead.

Your app may optionally present in-app messaging that informs users they can avoid losing access to paid service by taking action and resolving their billing error. If you choose to prompt the user, ensure your app’s subscription logic can handle different values of [`expiration_intent`](https://developer.apple.com/documentation/AppStoreReceipts/expiration_intent) along with [`expires_date_ms`](https://developer.apple.com/documentation/AppStoreReceipts/expires_date_ms), to show the appropriate message. An invalid payment method could be due to a number of things, such as a low balance on a stored value card or an expired credit card. Your app should be ready to react immediately to a billing information update. Your app can deep link customers to the Manage Payments page on their account settings by opening this URL:

```http
https://apps.apple.com/account/billing
```

> **Note**:  This URL is only supported for iOS and macOS.

For more general guidance on handling subscriptions that enter a billing retry state, see [`WWDC 2018 > Engineering Subscriptions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/705/). You can also agree to provide a grace period for subscribers in a billing retry state. Billing error recoveries made within the set grace period automatically recover subscribers onto their current billing cycle, also providing revenue continuity.

##### Enable Billing Grace Period

To avoid interrupting days of paid service, you can enable Billing Grace Period in App Store Connect, which allows subscribers to retain full access to your app’s paid content while Apple attempts to collect payment. For guidance on opting in to enable Billing Grace Period for your app, see [`Enable Billing Grace Period for Auto-Renewable Subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev58bda3212).

Billing Grace Period is applied at the time of a billing error when it’s enabled for subscriptions in the app, and cannot be altered once assigned to a user. Grace period durations are dependent on the subscription period length as follows:

- 3 or 6 days for a weekly subscription
- 3, 16, or 28 days for monthly and longer subscriptions

If you choose to enable Billing Grace Period, ensure that you provide full service for the subscription throughout the grace period. You can check the `grace_period_expires_date_ms` field in the [`responseBody.Pending_renewal_info`](https://developer.apple.com/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) array of the `verifyReceipt` response or `unified_receipt` object in the server notification to determine the end of this grace period duration. For more information on reducing involuntary churn using a grace period, see [`WWDC 2019 > In-App Purchases and Using Server-to-Server Notifications`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/302/).

If the user is recovered within this grace period, neither the subscriber’s days of paid service, nor your revenue for auto-renewable subscriptions will be interrupted. Billing error recoveries made after the grace period expires, but within the overall billing retry period, will maintain existing behavior and renew on the recovery date, starting a new billing cycle. Payment for the provided full service during the grace period would not be collected.

![Two example timelines for a monthly subscription that enters a billing retry state, in an app for which Billing Grace Period is enabled. In the first scenario, the user is recovered within the grace period, the developer is paid for providing full service, and the following renewal date is preserved. In the second scenario, the user is recovered not within the grace period but within 60 days, so the next renewal date shifts to the date the customer is billed.](https://docs-assets.developer.apple.com/published/22d0c7c2153d8e4779bcaba050f41e3f/media-3382825%402x.png)

When implementing Billing Grace Period, use the [`verifyReceipt`](https://developer.apple.com/documentation/AppStoreReceipts/Verify-Receipt) JSON response and server-to-server notifications. Consider using `expiration_intent`, `is_in_billing_retry_period`, and `grace_period_expires_date_ms` of the `unified_receipt` object in the server notifications of type `RENEWAL` and `DID_RECOVER` to identify whether the subscription is in a grace period.

The `expiration_intent` value can tell you if a subscription renewal failed due to a billing error, or simply because the user chose to cancel service. You can also see if the App Store is actively trying to recover a subscription by looking for an active `is_in_billing_retry_period flag`.

Consider all scenarios for subscription recovery:

- If the subscription renews before the time specified in `grace_period_expires_date_ms`, the `grace_period_expires_date` fields are removed along with the `is_in_billing_retry_period` indicator. You can look up a past transaction’s `purchase_date_ms` and `expires_date_ms` values to determine if a user’s subscription renewed after a lapse.
- If the subscription renews after the time specified in `grace_period_expires_date_ms` while still in the billing retry state, the `grace_period_expires_date` fields are removed along with the `is_in_billing_retry_period` indicator. You can use the `expires_date_ms` value for a past transaction to determine the lapse period.
- If attempts to renew the subscription fail, the `grace_period_expires_date` fields persist along with a value of `0` for the `auto_renew_status` and `is_in_billing_retry_period` indicators.

##### Restore Service

When users update their payment information, the App Store immediately attempts to renew the payment. Once the App Store successfully bills the customer in a billing retry state, the App Store notifies your server with notifications of types `RENEWAL` and `DID_RECOVER`, and a new receipt is generated for the successful transaction. A new value appears in the `expires_date_ms` field in the app transaction receipt, based on the date of recovery, to mark the next renewal date of the subscription.

StoreKit adds a new transaction for the renewal to the transaction queue on the device. Your app can check the transaction queue on launch and handle the renewal the same way as any other transaction. If your app is already running when the subscription renews, the transaction observer is not called; your app finds out about the renewal the next time the app launches. Restore service once the subscription is renewed if needed.

## See Also

- [Handling Subscriptions Billing](handling-subscriptions-billing.md)
  Build logic around the date and time constraints of subscription products, while planning for all scenarios where you control access to content.
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Offering a Subscription Across Multiple Apps](offering-a-subscription-across-multiple-apps.md)
  Support a single auto-renewable subscription across multiple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/reducing-involuntary-subscriber-churn)*