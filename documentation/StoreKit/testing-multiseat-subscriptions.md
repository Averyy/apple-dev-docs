# Testing multiseat subscriptions

**Framework**: StoreKit  
**Role**: Article

Test group purchases, invitations, seat changes, refunds, and purchases from organizations in the sandbox environment before you release your app.

## Overview

In the sandbox environment, you can test your multiseat implementation end to end with Sandbox Apple Accounts, signed transactions, and App Store Server Notifications. From the sandbox settings on your device, you can buy a group subscription, add and remove members, change the group size, and refund seats, and you can switch between Apple-hosted and developer-hosted invitations without changing your app’s settings in App Store Connect.

Keep these differences from production in mind:

- In the sandbox environment, your subscriptions always allow multiseat purchases, regardless of their purchase options in App Store Connect.
- Each Sandbox Apple Account has its own invitation setting, so you can test both invitation models with the same build of your app.
- Sandbox Apple Accounts can’t accept invitation links. To add a member to a group with Apple-hosted invitations, add their Sandbox Apple Account from the group purchaser’s sandbox settings.
- Subscriptions renew at an accelerated rate, so you can step through renewals, seat reductions, and expirations in minutes. For more information, see [Manage Sandbox Apple Account settings](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/).

For general information about testing in the sandbox environment, see [Testing Apple In-App Purchases with sandbox](./testing-in-app-purchases-with-sandbox.md).

### Prepare Sandbox Apple Accounts

Create a Sandbox Apple Account for the group purchaser, and one for each member you plan to add. For more information, see [Create a Sandbox Apple Account](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids). For Apple-hosted invitations, make sure each member’s Sandbox Apple Account is in the same country or region as the group purchaser’s account to test a successful invitation.

To make testing easier, use a separate device for each account. You can also use a single device and sign in with each Sandbox Apple Account in turn.

### Choose the invitation model

The invitation model comes from the group purchaser’s Sandbox Apple Account rather than from App Store Connect. Apple-hosted invitations are the default. To change the model:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account.
3. On the popup sheet, select Manage.
4. On the Account Settings page, select Group Subscriptions.
5. Select Invitations Provided by Apple or Invitations Provided by Developer.

The setting applies to new purchases, or when you subscribe again; a group subscription keeps its invitation model until it expires.

TestFlight builds also run in the sandbox environment. A tester who buys with their own Apple Account can’t reach the sandbox settings, so their group purchases use the default, Apple-hosted invitations. To test developer-hosted invitations or the other group settings in a TestFlight build, sign in with a Sandbox Apple Account, as described in [Sign in to your Sandbox Apple Account for a TestFlight app](./testing-in-app-purchases-with-sandbox.md#Sign-in-to-your-Sandbox-Apple-Account-for-a-TestFlight-app).

### Open the sandbox settings for a group

The group purchaser’s sandbox settings let you manage a group without your app, as a customer does in their subscription settings. To open a group subscription’s page:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account of the group purchaser.
3. On the popup sheet, select Manage.
4. On the Account Settings page, select Subscriptions.
5. Select the group subscription.

The page shows the group size and the number of available seats, counting the group purchaser’s own seat as taken. From it, you can change the group size, refund seats or the whole subscription, and cancel the subscription. For a group with Apple-hosted invitations, the page also lists the group’s members, and you can add and remove members there.

### Test merchandising and purchases

Sign in with the group purchaser’s Sandbox Apple Account, and open your app. Check that [`supportsMultiSeatPurchase`](./product/supportsmultiseatpurchase.md) is `true` for your subscription, and that your store shows each tier’s per-seat price and the correct total for each group size.

Buy a group subscription with [`seats(_:)`](./product/purchaseoption/seats%28_%29.md). Verify that the transaction’s [`purchasedQuantity`](./transaction/purchasedquantity.md) matches the number of seats, and that its price tiers add up to the total your store showed. With another account, buy one seat of the same subscription, and verify that your app treats it as a standard subscription.

For a group with Apple-hosted invitations, check that the invitation sheet appears after the purchase, and that it doesn’t appear when you add [`multiSeatInvitationSheetSuppressed(_:)`](./product/purchaseoption/multiseatinvitationsheetsuppressed%28_%29.md) with a value of `true`.

To test an introductory offer again with the same account, select Reset Eligibility on the group subscription’s page.

### Test Apple-hosted invitations and member access

Sandbox Apple Accounts can’t accept the invitations that the invitation sheet sends. To add members to a group with Apple-hosted invitations, use the group purchaser’s sandbox settings:

1. Open the group subscription’s page, as described in [Open the sandbox settings for a group](./testing-multiseat-subscriptions.md#Open-the-sandbox-settings-for-a-group).
2. In the Manage Group Members section, select Add Members.
3. Enter the email address of a member’s Sandbox Apple Account. To add several members, separate their email addresses with commas.
4. Select Add. The new members appear in the list.

On a device signed in with a member’s Sandbox Apple Account, open your app. Verify that the member’s transaction arrives through [`updates`](./transaction/updates.md) and appears in [`currentEntitlements`](./transaction/currententitlements.md) with an ownership type of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md), and that your app grants access to the transaction’s product. On your server, verify that you receive a `SUBSCRIBED` notification with a subtype of `INITIAL_BUY` or `RESUBSCRIBE` for the member.

To remove a member, select the member in the list, select Remove Member, and confirm. The member loses access right away, and the group size doesn’t change. Verify that the member’s transaction has a revocation type of [`assignmentRevocation`](./transaction/revocationtype-swift.struct/assignmentrevocation.md), that your server receives a `REVOKE` notification, that your app removes the member’s access, and that the group purchaser keeps access.

To test a member leaving, sign in with the member’s Sandbox Apple Account and choose Leave Subscription in its sandbox subscription settings. Verify the same revocation and `REVOKE` notification.

To test your group experience, call [`Get Customer Groups`](../AppStoreServerAPI/get-customer-groups.md) with a member’s transaction identifier, and [`Get Group Members`](../AppStoreServerAPI/get-group-members.md) with the group’s `groupId`.

To test the consent flow, check [`multiSeatDataSharingConsentEligibility`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md) with each account:

1. As the group purchaser, before they respond, check that the value is `eligible` and that your app offers its request.
2. Present the data sharing consent sheet and choose to share group visibility. Check that the value becomes `ineligible(.alreadyConsented)`, that your app stops offering the request, and that Get Customer Groups and Get Group Members now return the group.
3. As a member, check that the value is `ineligible(.noOwnedActiveSubscription)` and that your app shows no request.
4. As the group purchaser, stop sharing group visibility in the subscription settings. Check that the value is `eligible` again, so you can repeat the test.

Also verify that your app checks again before each presentation; if it doesn’t, the sheet throws [`StoreKitError.unsupported`](./storekiterror/unsupported.md).

Verify that the group’s `groupType` is `CONSUMER`, that your server pages through members with `paginationToken` and an explicit `limit`, and that your app keeps granting access from transactions when a group doesn’t appear.

When a customer doesn’t belong to a Group Purchases group, Get Customer Groups returns a placeholder group in the sandbox, with a `groupId` of `900000000000000000`, and Get Group Members returns a placeholder member for it. Don’t treat the placeholder as real data.

### Test Developer-hosted seats

With the group purchaser’s account set to Invitations Provided by Developer, buy a group subscription with several seats. Then test your server against the seat management endpoints in the sandbox, at `https://api.storekit-sandbox.apple.com`: [`Get Seat Info`](../AppStoreServerAPI/get-seat-info.md), [`Claim Seat`](../AppStoreServerAPI/claim-seat.md), [`Associate Seat`](../AppStoreServerAPI/associate-seat.md), and [`Unclaim Seat`](../AppStoreServerAPI/unclaim-seat.md).

Start by calling Get Seat Info for the group, and note the number of available seats. Accept an invitation in your own flow, call Claim Seat, and check that Get Seat Info shows one fewer available seat. Send the same request again with the same `requestIdentifier`, and check that you get the same `seatClaimId` rather than a second claim. When no seats are available, check that your app stops offering invitations, and that a failed claim tells the invited person that the group is full.

To test association, sign in with a different Sandbox Apple Account, open your app, and send its [`appTransactionID`](./apptransaction/apptransactionid.md) to your server. Include the identifier in the Claim Seat request, or call Associate Seat for a seat you already claimed. Then check that the group subscription appears in that account’s sandbox settings, under Subscriptions.

To test leaving, sign in as an associated member. In the member’s sandbox subscription settings, remove the subscription from the Apple Account, and check that the seat claim and the member’s access don’t change. Then choose Leave Subscription, and check that your server receives an `UNCLAIM_SEATS` notification for the seat and revokes the member’s access.

To test unclaiming and reclaiming seats, remove a member in your app and call Unclaim Seat. Check that your app revokes the member’s access, that Get Seat Info shows the seat as available again, and that you can claim it for someone else.

To test adding seats, increase the group size in your app or in the group purchaser’s sandbox settings, as described in [Test seat changes](./testing-multiseat-subscriptions.md#Test-seat-changes). Check that your server updates its seat count from the `INCREASE_QUANTITY` notification, and that Get Seat Info reports the same total.

With developer-hosted invitations, you verify the age of each person you invite. To test how your invitation flow handles each age range, choose an Age Assurance scenario in the invited person’s Sandbox Apple Account settings. For more information, see [Testing age assurance in sandbox](./testing-age-assurance-in-sandbox.md).

To test a parent or guardian declining access, associate the seat of a Sandbox Apple Account with Ask to Buy turned on, choose Don’t Allow as its parent or guardian, and check that your server receives an `UNCLAIM_SEATS` notification and revokes the member’s access.

Check that [`multiSeatDataSharingConsentEligibility`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md) returns `ineligible(.notAppleManaged)` for the group purchaser, and that your app doesn’t offer the consent request.

### Test seat changes

Seat changes work the same way for both invitation models. To add seats, buy a larger group in your app with [`seats(_:)`](./product/purchaseoption/seats%28_%29.md), or use the group purchaser’s sandbox settings:

1. Open the group subscription’s page, as described in [Open the sandbox settings for a group](./testing-multiseat-subscriptions.md#Open-the-sandbox-settings-for-a-group).
2. Select Change Group Size.
3. Increase the group size, and select Continue.
4. Confirm the purchase. As in production, the confirmation shows the prorated charge for the added seats.

Verify that a second transaction covers the added seats, that both of the period’s transactions have an additional transaction reason of [`seatAddition`](./transaction/additionaltransactionreason-swift.struct/seataddition.md), and that your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `INCREASE_QUANTITY`.

To reduce seats, decrease the group size on the same page. The change takes effect at the next renewal. In a group with Apple-hosted invitations, if the new size is smaller than the number of members, you choose which members to remove as part of the change. Each time you change the size, verify that your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `DECREASE_QUANTITY`, including when you raise the size part of the way back, and that it reads `renewalQuantity` rather than tracking the changes. After the subscription renews, verify that one transaction covers the new size. With Apple-hosted invitations, verify that the members you removed lose access; with developer-hosted invitations, verify that Claim Seat fails until the claimed seats fit in the new size, minus the group purchaser’s seat.

### Test refunds

Refund request APIs such as [`beginRefundRequest(in:)`](./transaction/beginrefundrequest%28in%29-9k0pj.md) return an error for group subscriptions, so refund them in the group purchaser’s sandbox settings:

1. Open the group subscription’s page, as described in [Open the sandbox settings for a group](./testing-multiseat-subscriptions.md#Open-the-sandbox-settings-for-a-group).
2. Select Refund Group Subscription.
3. Select Partial Refund and enter the number of seats to refund, or select Full Refund.
4. Select Refund. An alert confirms the refund and the transaction it applies to.

A partial refund covers the current period only, up to the number of seats that aren’t already refunded. Verify that your server receives a `REFUND` notification with a subtype of `SEATS`, that the transaction stays valid, and that [`revokedSeatQuantity`](./transaction/multiseatinfo-swift.struct/revokedseatquantity.md) reports the refunded seats.

A partial refund starts with the most recent seats, which are also the cheapest: first seats that nobody holds, then the members who were added most recently, and finally the group purchaser’s own seat. With Apple-hosted invitations, verify that each removed member’s transaction is revoked and that your server receives a `REVOKE` notification for it. With developer-hosted invitations, verify that your server receives an `UNCLAIM_SEATS` notification and revokes access for the listed seats.

After a full refund, verify that your app ends access for the whole group once every transaction in the period is revoked.

### Test cancellations and billing issues

To test a cancellation, select Cancel Subscription on the group subscription’s page. Verify that your server receives a `DID_CHANGE_RENEWAL_STATUS` notification with a subtype of `AUTO_RENEW_DISABLED`, that everyone keeps access until the period ends, and that nobody has access after your server receives an `EXPIRED` notification.

To test a billing issue, turn off Allow Purchases & Renewals on the group purchaser’s Account Settings page before a renewal. Verify that members keep access while the group purchaser’s subscription is in its grace period, and that your app revokes access for the whole group at the end of the billing grace period. Members don’t see the billing issue; they lose access unless billing recovers or the group purchaser resubscribes. For more information, see [Testing failing subscription renewals and Apple In-App Purchases](./testing-failing-subscription-renewals-and-in-app-purchases.md).

### Test purchases from an organization

You can’t buy seats in Apple Business or Apple School Manager from the sandbox, but you can simulate an organization assigning a seat to a Sandbox Apple Account:

1. Open Settings and select Developer.
2. Select the Sandbox Apple Account.
3. On the popup sheet, select Manage.
4. On the Account Settings page, select Initiate Transaction.
5. Select Organizational Purchases, and enter your app’s bundle ID and the product ID of the subscription.

Verify that your app receives a transaction with an ownership type of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md) and grants access, and that your server receives a `SUBSCRIBED` notification.

To simulate the organization taking the seat back, revoke the organizational purchase from the same page. Verify that the transaction gets a revocation type of [`assignmentRevocation`](./transaction/revocationtype-swift.struct/assignmentrevocation.md), that your server receives a `REVOKE` notification, and that your app revokes access.

> ❗ **Important**: After you revoke an organizational purchase in the sandbox, the subscription keeps renewing for the Sandbox Apple Account as a standard purchase, with a new original transaction ID and an ownership type of [`purchased`](./transaction/ownershiptype-swift.struct/purchased.md) — `PURCHASED` in `inAppOwnershipType` on your server. This happens only in the sandbox.

## See Also

### Related Documentation
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.
- [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.
### Subscriptions
- [Testing an auto-renewable subscription](./testing-an-auto-renewable-subscription.md)
  Verify that your app handles a subscription lapse properly using the accelerated time rates within the sandbox environment.
- [Testing resubscribing from the subscriptions page](./testing-resubscribing-from-the-subscriptions-page.md)
  Verify that your app can reactivate an expired subscription by receiving a transaction callback or inspecting an updated receipt.
- [Testing disabling auto-renew](./testing-disabling-auto-renew.md)
  Verify that your app receives subscription updates when a user cancels a subscription by verifying the receipt or receiving a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-multiseat-subscriptions)*