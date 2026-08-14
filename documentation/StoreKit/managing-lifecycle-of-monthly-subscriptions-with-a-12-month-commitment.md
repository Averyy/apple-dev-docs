# Managing the life cycle of monthly subscriptions with a 12-month commitment

**Framework**: StoreKit

Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.

#### Overview

A *monthly subscription with a 12-month commitment* is an auto-renewable subscription that bills customers monthly and has a yearly commitment. Unlike standard subscriptions that bill customers up front, its ([`billingPlanType`](transaction/billingplantype.md)) in [`Transaction`](transaction.md) is [`monthly`](product/subscriptioninfo/billingplantype/monthly.md).

For more information on configuring, merchandising, purchasing, and entitling a monthly subscription with a 12-month commitment, see [`Supporting monthly subscriptions with a 12-month commitment`](supporting-monthly-subscriptions-with-a-12-month-commitment.md).

#### Manage Subscription Renewals

A monthly subscription with a 12-month commitment automatically bills monthly. Process the resulting transaction and enable access to content the same way as for standard subscriptions. When subscriptions renew, your server receives a `DID_RENEW` notification ([`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)) at your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) endpoint. Your app receives a transaction through the [`updates`](transaction/updates.md) listener.

The following fields in the transaction provide additional information about the commitment plan:

| Field | Structure | Description |
| --- | --- | --- |
| [`billingPlanType`](transaction/billingplantype.md) | [`Transaction`](transaction.md) | A value of [`monthly`](product/subscriptioninfo/billingplantype/monthly.md) indicates a commitment plan. |
| [`willAutoRenew`](product/subscriptioninfo/renewalinfo/willautorenew.md) | [`renewalInfo`](product/subscriptioninfo/status-swift.struct/renewalinfo.md) | A Boolean value that indicates whether the next billing period will renew. This field behaves the same as for standard subscriptions. |
| [`willAutoRenew`](product/subscriptioninfo/renewalinfo/commitmentinfo-swift.struct/willautorenew.md) | [`Product.SubscriptionInfo.RenewalInfo.CommitmentInfo`](product/subscriptioninfo/renewalinfo/commitmentinfo-swift.struct.md) | A Boolean value that indicates whether the subscription will renew at the end of the 12-month commitment period. |

When the 12th billing period completes, a value of `1` for [`willAutoRenew`](product/subscriptioninfo/renewalinfo/commitmentinfo-swift.struct/willautorenew.md) indicates that the subscription automatically renews. The App Store Server Notifications sends a `DID_RENEW` notification. If the renewal is for a monthly subscription with a 12-month commitment, period `1` of the new commitment begins. The renewal may apply to a different subscription, not necessarily one with a 12-month commitment.

#### Manage Subscription Cancellation During a Commitment

When a customer cancels a monthly subscription with a 12-month commitment, they’re canceling the renewal of the commitment, not the remaining payments within the current term. Billing continues through all remaining periods. When a customer cancels the subscription mid-period, the following occurs:

- The App Store server sets [`willAutoRenew`](product/subscriptioninfo/renewalinfo/commitmentinfo-swift.struct/willautorenew.md) in the commitment information ([`Product.SubscriptionInfo.RenewalInfo.CommitmentInfo`](product/subscriptioninfo/renewalinfo/commitmentinfo-swift.struct.md)) to `0`, to indicate the commitment doesn’t renew when the term ends.
- The [`willAutoRenew`](product/subscriptioninfo/renewalinfo/willautorenew.md) in the subscription renewal info ([`renewalInfo`](product/subscriptioninfo/status-swift.struct/renewalinfo.md))  remains `1`, indicating that monthly billing continues for the remaining periods of the current commitment.
- App Store Server Notifications sends a `DID_CHANGE_RENEWAL_STATUS` [`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype) with an `AUTO_RENEW_DISABLED` [`subtype`](https://developer.apple.com/documentation/appstoreservernotifications/subtype) to your server.

App Store Server Notifications continues to send `DID_RENEW` notifications for each remaining billing period. *Continue providing access to the subscription through the end of the commitment period.* After the 12th and final period, the App Store server sends an `EXPIRED` [`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype). Access ends here.

When you receive a `DID_CHANGE_RENEWAL_STATUS` notification, check the billing plan type on the transaction first:

- If the billing plan type is `MONTHLY`, read `commitmentAutoRenewStatus` to confirm the commitment doesn’t renew. Don’t revoke access to the subscription; continue to honor all remaining billing periods.
- If the billing plan type is `BILLED_UPFRONT`, the subscription is a standard subscription. Apply your existing cancellation logic.

#### Manage Subscription Access During Billing Issues

When a monthly renewal fails due to a billing issue, the App Store automatically attempts to recover the payment. While the subscription is in a billing retry state, revoke access to the subscription, and restore it if billing recovers. If the App Store is unable to recover the payment within 90 days, the commitment ends and you revoke service permanently for that transaction.

App Store Server Notifications sends the following notifications ([`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)) to indicate the billing retry status:

| Notification type | Transaction detail | App’s action |
| --- | --- | --- |
| `DID_FAIL_TO_RENEW` | `isInBillingRetryPeriod` is `true`. | Revoke access to the subscription. |
| `DID_RENEW` with subtype `BILLING_RECOVERY` | `commitmentExpiresDate` shifts to a new billing date, reflecting the recovery date. | Restore access to the subscription. |
| `EXPIRED` with subtype `BILLING_RETRY` | `isInBillingRetryPeriod` is `false`. | Previously revoked access is final. |

For more information on the transaction and subscription renewal information you receive with notifications, see [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/appstoreservernotifications/jwstransactiondecodedpayload) and [`JWSRenewalInfoDecodedPayload`](https://developer.apple.com/documentation/appstoreservernotifications/jwsrenewalinfodecodedpayload).

After a billing issue recovery, read the `commitmentExpiresDate` from the latest transaction, because it differs from the original commitment end date. Subsequent renewals follow the shifted schedule.

Billing Grace Period doesn’t apply to monthly subscriptions with 12-month commitments. Revoke access to the subscription as soon as you receive a `DID_FAIL_TO_RENEW` [`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype).

#### Respond to Refund Consumption Requests

When a customer submits a refund request for a subscription with a commitment plan, your server receives a `CONSUMPTION_REQUEST` notification at your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) endpoint.

Respond with the consumption information and your refund preference for that billing period. For more information on consumption requests, see [`Send Consumption Information`](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information).

#### Manage Access After a Refund

Customers may receive a refund after they request one, or after making changes to their subscription plan that cause a refund.

When a customer receives a refund for a monthly subscription with a 12-month commitment, the refund behavior depends on the billing period that the refund applies to, as follows:

- If the refund applies to a prior billing period, the system revokes the transaction for that specific period, but the commitment continues unaffected. The customer remains subscribed and billing continues on schedule. Check the [`revocationDate`](transaction/revocationdate.md) on the affected transaction to detect the revocation, but don’t interpret it as a commitment cancellation.
- If the refund applies to the current billing period, the commitment ends immediately. Check the [`revocationDate`](transaction/revocationdate.md) on the latest transaction — its presence indicates the current period has been revoked and the commitment has ended. Revoke access accordingly.

#### Manage Price Changes

Price changes for monthly subscriptions with 12-month commitments follow the same rules as standard annual subscriptions. For more information, see [`Managing Price Increases for Auto-Renewable Subscriptions`](managing-price-increases-for-auto-renewable-subscriptions.md).

#### Test the Subscription Using Storekit Testing for Xcode

You can test your client-side implementation locally without a Sandbox Apple Account or an Apple Account using StoreKit Testing in Xcode. Testing monthly subscriptions with 12-month commitments is available starting in Xcode 26.5.

To configure the commitment-plan testing in Xcode:

1. Open your StoreKit configuration file in Xcode.
2. Select your 1-year auto-renewable subscription product.
3. Add the monthly billing plan type to the product’s configuration.
4. Set a monthly price for the plan.

With the configuration in place, you can:

- Test your commitment-plan merchandising by verifying that your app returns the correct product and that both the monthly price and the total commitment price display correctly.
- Test the purchase flow by initiating a purchase using the `billingPlanType(.monthly)` option and inspecting `commitmentInfo` on the resulting transaction.
- Validate commitment progress UI by reading `billingPeriodNumber`, `totalBillingPeriods`, and the expiration date fields from the transaction.
- Simulate a cancellation by canceling the subscription in the Transaction Manager. Confirm that your app continues to grant access to the subscription through the remaining billing periods. For more information, see [`Testing in-app purchases with StoreKit transaction manager in Xcode`](https://developer.apple.com/documentation/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code).
- Test your entitlement logic by confirming your app uses [`expirationDate`](transaction/expirationdate.md) in [`Transaction`](transaction.md) for subscription-access decisions and only uses [`expirationDate`](transaction/commitmentinfo-swift.struct/expirationdate.md) in [`Transaction.CommitmentInfo`](transaction/commitmentinfo-swift.struct.md) to display the commitment progress.

For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode).

#### Test Your App in the Sandbox Environment

When you’re ready to validate your server-side implementation, test in the sandbox environment using a Sandbox Apple Account.

In the sandbox environment, you can:

- Run the full 12-month commitment at an accelerated rate to validate the complete commitment life cycle end-to-end.
- Validate your server-side logic with real signed transactions and App Store Server Notifications V2.
- Test cancellation flows by canceling a commitment mid-period and verifying that your server and app correctly handle `DID_CHANGE_RENEWAL_STATUS`, continue granting access through remaining billing periods, and revoke access only after the final `EXPIRED` notification.
- Test billing issues and recovery flows by simulating payment issues and verifying that your server revokes access on `DID_FAIL_TO_RENEW`, restores access on `DID_RENEW BILLING_RECOVERY`, and reads the updated `commitmentExpiresDate` from the recovered transaction.
- Test a billing issue without a recovery by leaving the Allow Purchases & Renewal toggle off past the billing retry window. Verify that your server receives an `EXPIRED` notification type with subtype `BILLING_RETRY`. You would have already revoked access to the subscription based on a previously received `DID_FAIL_TO_RENEW` notification; the revocation is now final.

## See Also

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md)
  Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Supporting monthly subscriptions with a 12-month commitment](supporting-monthly-subscriptions-with-a-12-month-commitment.md)
  Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.
- [struct Product](product.md)
  Information about a product that you configure in App Store Connect.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [typealias SubscriptionInfo](subscriptioninfo.md)
  Information about an auto-renewable subscription.
- [typealias SubscriptionStatus](subscriptionstatus.md)
  Represents the renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-)*