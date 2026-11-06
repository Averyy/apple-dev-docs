# Managing the life cycle of multiseat subscriptions

**Framework**: StoreKit  
**Role**: Article

Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.

## Overview

A multiseat subscription changes after the purchase: the group purchaser adds seats, removes members, or reduces the group size, in your app or in their subscription settings, and organizations assign and reassign seats. Most of these changes start with the group purchaser or the organization rather than with your app, and they reach you as transactions and as App Store Server Notifications.

Keep two kinds of information apart:

- **The group’s seats and price**: The group purchaser’s transactions record how many seats the group has and what each seat cost.
- **Each person’s access**: Each person’s own transaction records their access: the group purchaser’s, each invited member’s with Apple-hosted invitations, and each organization assignee’s. For invited members with developer-hosted invitations, the seat claims you store on your server grant access.

For configuring, selling, and granting access to multiseat subscriptions, see [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md). For developer-hosted invitations, see [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md).

## Read seat counts and prices

The group purchaser’s transaction and renewal information describe the group’s seats:

| StoreKit | App Store Server API | Meaning |
| --- | --- | --- |
| [`purchasedQuantity`](./transaction/purchasedquantity.md) | `quantity` | The number of seats the transaction covers |
| [`priceTiers`](./transaction/multiseatinfo-swift.struct/pricetiers.md) | `multiSeatInfo.priceTiers` | The seats bought at each price |
| [`revokedSeatQuantity`](./transaction/multiseatinfo-swift.struct/revokedseatquantity.md) | `multiSeatInfo.revokedSeatQuantity` | The seats a refund removed from the transaction |
| [`renewalQuantity`](./product/subscriptioninfo/renewalinfo/renewalquantity.md) | `renewalQuantity` | The number of seats at the next renewal |
| [`renewalPriceTiers`](./product/subscriptioninfo/renewalinfo/multiseatinfo-swift.struct/renewalpricetiers.md) | `multiSeatInfo.renewalPriceTiers` | The seats and prices at the next renewal |

In StoreKit, a transaction’s [`multiSeatInfo`](./transaction/multiseatinfo-swift.property.md) holds its price tiers and revoked seats, and the renewal information’s [`multiSeatInfo`](./product/subscriptioninfo/renewalinfo/multiseatinfo-swift.property.md) holds the price tiers for the next renewal.

The transaction’s [`price`](./transaction/price.md) is the average price per seat. To find what the group purchaser pays, add up each price tier’s price multiplied by its quantity; don’t multiply the price by the seat count. For example, a group of eight with tiers of 1–5 seats at $9.99 and 6–10 seats at $7.99 reports these tiers on the server, in milliunits — 5 × 9990 plus 3 × 7990, a total of 73,920 milliunits, or $73.92:

```json
{
    "quantity": 8,
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 7990, "quantity": 3 }
        ]
    }
}
```

The tiers aren’t listed in any particular order. To show them in the order seats fill them, sort them by price, highest first.

## Manage renewals

Each renewal produces one transaction for the group purchaser that covers the full renewal quantity, and your server receives a `DID_RENEW` notification. This holds even when several transactions covered the previous period, so don’t predict the next period’s transactions from the current one’s.

## Handle added seats

A group purchaser can add seats at any time, in your app or in their subscription settings. To add seats in your app, call [`purchase(options:)`](./product/purchase%28options%29.md) with [`seats(_:)`](./product/purchaseoption/seats%28_%29.md) set to the new total number of seats. The App Store charges a prorated amount for the rest of the current period, and the subscription renews at the new size on its existing renewal date.

Adding seats creates a new transaction for the added seats in the same period; the earlier transaction stays valid. Both transactions report a reason of `SEAT_ADDITION` — `additionalTransactionReason` on the server, [`seatAddition`](./transaction/additionaltransactionreason-swift.struct/seataddition.md) in StoreKit — including the earlier transaction, which gains the value when the seats are added. The group’s paid seats for the period are the sum of the quantities of the period’s unrevoked transactions.

The price of the transaction for the added seats is prorated, but its price tiers keep the full per-seat prices. As a result, that transaction’s tiers don’t add up to the amount the group purchaser paid for the added seats.

Your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `INCREASE_QUANTITY`.

Help the group purchaser fill new seats right away when they add them in your app. With Apple-hosted invitations, the system presents the invitation sheet after a purchase in your app, unless you suppress it; if you suppress it, present the invitation sheet yourself. The group purchaser can also add seats outside your app, in their subscription settings. The new transaction appears in [`updates`](./transaction/updates.md), so offer the invitation sheet the next time they’re in your app. With developer-hosted invitations, update your server’s seat count from the `INCREASE_QUANTITY` notification, and start your invitation flow as soon as the group purchaser is back in your app; the new seats are available to claim as soon as they’re added.

## Handle reduced seats

Only the group purchaser can reduce the group size, in their subscription settings, and the change takes effect at the next renewal. Your app can’t reduce the seat count or prevent a reduction. To let the group purchaser reduce seats from your app, present their subscription settings with [`showManageSubscriptions(in:)`](./appstore/showmanagesubscriptions%28in%29.md), or [`showManageSubscriptions(from:)`](./appstore/showmanagesubscriptions%28from%29.md) on macOS.

Each time the group purchaser changes the size for the next renewal, your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `DECREASE_QUANTITY`. The subtype compares the new size with the current one, so it also arrives when the group purchaser undoes all or part of an earlier reduction. Read `renewalQuantity` from the renewal information each time rather than tracking the changes.

At the renewal, the group purchaser’s new transaction covers the new size. With Apple-hosted invitations, if the new size is smaller than the number of people in the group, the group purchaser chooses which members to remove when they reduce the size in their subscription settings. Those members lose access when the current period ends. With developer-hosted invitations, you manage membership with the seat endpoints; see [Handle a smaller group at renewal](./hosting-group-invitations-in-your-app.md#Handle-a-smaller-group-at-renewal).

## Handle member changes

When an invited member of an Apple-hosted group leaves the group in their subscription settings, or the group purchaser removes them in theirs, the change is immediate. The member’s transaction gets a [`revocationType`](./transaction/revocationtype-swift.property.md) of [`assignmentRevocation`](./transaction/revocationtype-swift.struct/assignmentrevocation.md) — `ASSIGNMENT_REVOKE` on the server — and your server receives a `REVOKE` notification. Revoke the member’s access to the product that the transaction represents. The removal isn’t a refund: the group purchaser’s transaction doesn’t change, and the seat becomes available for another invitation. When someone accepts an invitation, they receive their own transaction, and your server receives a `SUBSCRIBED` notification with a subtype of `INITIAL_BUY` or `RESUBSCRIBE`.

Organizations work the same way. When an organization takes a seat back from a person, that person’s transaction is revoked with the same revocation type; when the organization assigns the seat to someone else, that person receives a new transaction. Organizations buy and remove seats in Apple Business or Apple School Manager, and Apple bills the organization directly, so your app sees only the assignments and revocations. An organization takes seats back from people before it reduces its number of seats, so a reduction reaches you only as those revocations.

With developer-hosted invitations, you control the group’s membership: who holds each seat, and when it’s unclaimed, including when a member leaves the group or removes the subscription from their Apple Account; see [Grant and revoke member access](./hosting-group-invitations-in-your-app.md#Grant-and-revoke-member-access).

## Manage upgrades, downgrades, and crossgrades

Plan changes within a subscription group follow the existing upgrade, downgrade, and crossgrade rules, applied to the group purchaser’s subscription. When the group purchaser upgrades, the transaction they upgraded from has an [`isUpgraded`](./transaction/isupgraded.md) value of `true`. Adding seats never sets it.

A group purchase stays a group purchase unless the group purchaser changes to a subscription that doesn’t allow multiseat purchases, or their subscription expires and they subscribe again in your app without buying seats.

When the group purchaser changes to another subscription that allows multiseat purchases, the group keeps its size and its members. If they upgrade or downgrade, their choice to share group visibility with you also carries over. When they change to a subscription that doesn’t allow multiseat purchases, the change applies only to the group purchaser, whose own access continues without an interruption in service, and invited members lose access when the change takes effect: right away for an upgrade, and at the next renewal for a downgrade.

## Manage cancellations

When the group purchaser cancels the entire subscription, your server receives a `DID_CHANGE_RENEWAL_STATUS` notification with a subtype of `AUTO_RENEW_DISABLED`, as for any subscription. Continue to provide access to the whole group until the current period ends. When it ends, your server receives an `EXPIRED` notification, and every member loses access along with the group purchaser. The App Store doesn’t tell invited members that the group’s subscription is ending; consider letting them know in your app. The group also stops appearing in [`Get Customer Groups`](../AppStoreServerAPI/get-customer-groups.md), and the group purchaser’s choice to share group visibility resets. If they resubscribe, the new group subscription takes your current invitation setting, and you need to review [`multiSeatDataSharingConsentEligibility`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md) again before you ask them to share.

An invited member who leaves the group doesn’t cancel the subscription seat; the seat stays paid for and becomes available for another invitation. See [Handle member changes](./managing-the-life-cycle-of-multiseat-subscriptions.md#Handle-member-changes).

## Manage access during billing issues

Billing retry and Billing Grace Period work as they do for individual subscriptions, and the App Store contacts the group purchaser about the billing issue. Invited members aren’t told about the billing issue and can’t resolve it; their access follows the group purchaser’s subscription, and their subscription settings show only whether they have access. Provide access to the whole group while the group purchaser’s subscription is in a grace period — while its [`gracePeriodExpirationDate`](./product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md) (`gracePeriodExpiresDate` on the server) is in the future — and if the subscription expires because billing doesn’t recover, revoke access for everyone in the group.

## Manage access after a refund

A refund of the group purchaser’s whole purchase covers every seat, filled or unfilled. A period can include several transactions after the group purchaser adds seats, so continue to treat the group purchaser as entitled until every transaction in the period is revoked. A transaction’s top-level revocation fields appear only when every seat on it is revoked, and the subscription’s status reports revoked only when every transaction in the period is.

A group purchaser can also get a refund for some of the seats. A seat refund arrives as a `REFUND` notification with a subtype of `SEATS`, one for each transaction it affects. The transaction stays valid with fewer seats; [`revokedSeatQuantity`](./transaction/multiseatinfo-swift.struct/revokedseatquantity.md) reports how many it lost.

A seat refund starts with the most recent seats, which are also the cheapest: first unfilled seats, then the members who were added most recently, and finally the group purchaser’s own seat. With Apple-hosted invitations, the App Store revokes each removed member’s transaction with a [`revocationType`](./transaction/revocationtype-swift.property.md) of [`assignmentRevocation`](./transaction/revocationtype-swift.struct/assignmentrevocation.md), and sends a `REVOKE` notification for it. With developer-hosted invitations, it unclaims their seats and sends an `UNCLAIM_SEATS` notification; see [Respond when the App Store unclaims seats](./hosting-group-invitations-in-your-app.md#Respond-when-the-App-Store-unclaims-seats). Everyone else keeps their access, and their transactions don’t change.

Customers can’t request a refund for a group subscription in your app; refund request APIs such as [`beginRefundRequest(in:)`](./transaction/beginrefundrequest%28in%29-9k0pj.md) return an error.

## Manage price changes

For information about price changes, see [Managing Price Increases for Auto-Renewable Subscriptions](./managing-price-increases-for-auto-renewable-subscriptions.md).

## Respond to changes you make in App Store Connect

Some App Store Connect changes affect groups that already exist:

- **Turning off multiseat purchasing**: New customers can’t buy multiple seats, and the subscription won’t be available in Apple Business and Apple School Manager. Existing groups keep renewing until the group purchaser cancels; group purchasers can reduce the group size but can’t add seats.
- **Removing Apple Business or Apple School Manager**: Organizations’ subscriptions stop renewing, and they’re canceled at the end of their next renewal.
- **Changing the invitation model**: The change applies to new purchases and resubscriptions. Existing group subscriptions retain their original invitation model, so you can have group subscriptions with each model at once.

For details, see [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

## Respond to server notifications

The following notifications carry group activity to your server:

| Event | Notification type and subtype | What to do |
| --- | --- | --- |
| Seats added | `DID_CHANGE_RENEWAL_PREF`, `INCREASE_QUANTITY` | Recount paid seats from the period’s transactions. |
| Size changed for the next renewal | `DID_CHANGE_RENEWAL_PREF`, `DECREASE_QUANTITY` | Read `renewalQuantity`, and compare it with the number of people in the group to see whether members need to be removed. |
| Renewal | `DID_RENEW` | Expect one transaction for the full size. |
| An invited member accepts an invitation (Apple-hosted) | `SUBSCRIBED`, `INITIAL_BUY` or `RESUBSCRIBE` | Grant access from the member’s own transaction. |
| A member loses access | `REVOKE` | Revoke that member’s access. |
| Seats refunded | `REFUND`, `SEATS` | Lower the paid seat count; remove access only for members the refund removes. |
| Purchase refunded | `REFUND` | Revoke access once every transaction in the period is revoked. |
| Seats unclaimed (developer-hosted only) | `UNCLAIM_SEATS` | Revoke access for the listed seats. |
| Cancellation | `DID_CHANGE_RENEWAL_STATUS`, `AUTO_RENEW_DISABLED` | Keep access until the period ends. |
| Expiration | `EXPIRED` | Revoke access for the whole group. |

For each notification, decide a person’s access from their own transaction — or, for invited members with developer-hosted invitations, from the seat claims your server records — rather than from the group purchaser’s. For more information, see [`notificationType`](../AppStoreServerNotifications/notificationtype.md) and [`subtype`](../AppStoreServerNotifications/subtype.md).

## See Also

### Related Documentation
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.
- [Testing multiseat subscriptions](./testing-multiseat-subscriptions.md)
  Test group purchases, invitations, seat changes, refunds, and purchases from organizations in the sandbox environment before you release your app.
### Multiseat subscriptions
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/managing-the-life-cycle-of-multiseat-subscriptions)*