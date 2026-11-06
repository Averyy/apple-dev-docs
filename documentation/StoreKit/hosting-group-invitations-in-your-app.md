# Hosting group invitations in your app

**Framework**: StoreKit  
**Role**: Article

Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.

## Overview

With *developer-hosted invitations*, your app and server run the invitations for a group subscription: you invite people, decide who can accept, and grant each invited member access. The App Store handles everything else as it does for any subscription, including the purchase, the number of seats, billing, and renewals. Invited members receive no App Store transaction, so your server is the record of who has access.

Your server keeps the App Store’s record of the group’s seats in step with yours, with four App Store Server API endpoints: [`Claim Seat`](../AppStoreServerAPI/claim-seat.md) when someone accepts an invitation, [`Unclaim Seat`](../AppStoreServerAPI/unclaim-seat.md) when they leave or you remove them, [`Associate Seat`](../AppStoreServerAPI/associate-seat.md) to link a seat to the member’s Apple Account, and [`Get Seat Info`](../AppStoreServerAPI/get-seat-info.md) to read the group’s seat counts.

To compare the two invitation models and choose one in App Store Connect, see [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md).

## Meet the requirements

When you choose developer-hosted invitations in App Store Connect, your app and server take on two responsibilities:

- **Seat management**: Use the seat management endpoints to claim a seat for every invited member, and to unclaim it when they leave.
- **Age assurance**: Make sure that only age-appropriate customers join your service. On Apple platforms, at a minimum, use the [Declared Age Range](../DeclaredAgeRange/DeclaredAgeRange.md) API to request that people share their age range with your app, so that a parent or guardian or the Family Organizer can decide whether to allow the member to join the group, or remove them from it. For more information, see [Implementing age assurance and permissions](../DeclaredAgeRange/implementing-age-assurance-and-permissions.md).

Apple extends its parental controls to group subscriptions. When you associate the seat of a member whose account has Ask to Buy turned on, Apple asks a parent or guardian or the Family Organizer whether to allow the member to keep access. If they choose Don’t Allow, you’re required to revoke the member’s access; see [Associate the seat with the member](./hosting-group-invitations-in-your-app.md#Associate-the-seat-with-the-member).

## Design your invitation flow

Your invitation flow has two sides: the group purchaser invites people and manages the group, and the people they invite receive and accept an invitation.

### Design the group purchaser’s experience

Give the group purchaser a place in your app to see how many seats are taken and available, invite people, and remove members.

Keep a count of the group’s seats on your server. To start it, have your app send the group purchaser’s transaction to your server as its [`jwsRepresentation`](./verificationresult/jwsrepresentation-21vgo.md), which carries the same seat information as the App Store Server API. Then keep the count up to date from your seat claims and from App Store Server Notifications: the group purchaser can add seats at any time (`DID_CHANGE_RENEWAL_PREF` with a subtype of `INCREASE_QUANTITY`, effective right away), reduce the group size at the next renewal (`DECREASE_QUANTITY`, then `DID_RENEW`), or get a refund for some seats (`REFUND` with a subtype of `SEATS`). To check your count — for example, after your server misses a notification — call Get Seat Info.

Before you offer invitations, check the group’s invitation model in the group purchaser’s signed transaction. On your server, it’s [`invitationManagement`](../AppStoreServerAPI/invitationmanagement.md) in the `multiSeatInfo` of the [`JWSTransactionDecodedPayload`](../AppStoreServerAPI/jwstransactiondecodedpayload.md), which you get from App Store Server Notifications, the App Store Server API, or your app. In your app, StoreKit provides it as [`invitationManagement`](./transaction/multiseatinfo-swift.struct/invitationmanagement-swift.property.md).

A group subscription keeps the invitation model that was set in App Store Connect when the group purchaser subscribed. When you change the setting, in either direction, it applies to new purchases and resubscriptions, and existing group subscriptions keep their original model, so support both.

The seat management endpoints identify a group by the `originalTransactionId` of the group purchaser’s subscription, so save it on your server when you receive the purchase.

### Design the invited member’s experience

You decide how people receive and accept an invitation, in your app or on the web. Before you grant an invited member access, verify their age, as described in [Meet the requirements](./hosting-group-invitations-in-your-app.md#Meet-the-requirements), and enforce any storefront restrictions your content or service has — for example, for content rights. To let the member see the group subscription in their subscription settings, get their `appTransactionId` so you can associate their seat; see [Associate the seat with the member](./hosting-group-invitations-in-your-app.md#Associate-the-seat-with-the-member).

## Claim a seat when someone accepts an invitation

When a person accepts an invitation, call Claim Seat before you grant them access. The response contains a `seatClaimId`; store it with the member’s record, because you use it to associate or unclaim the seat, and the App Store uses it to tell you about seats it unclaims.

Claim seats only for invited members. The group purchaser always holds the first seat, so it’s never available to claim.

Send a `requestIdentifier` with each claim, so a retry after a failure or timeout doesn’t claim a second seat. For details, see [`requestIdentifier`](../AppStoreServerAPI/requestidentifier.md).

Stop sending invitations when your records show no available seats. If a claim still fails because the group has none, tell the invited person that the group is full. Only the group purchaser can add seats, in your app or in their subscription settings. If the group purchaser manages the group on your website, direct them to your app or to their subscription settings to add seats.

## Associate the seat with the member

With developer-hosted invitations, invited members don’t see the group subscription in their subscription settings until you associate their seat with their Apple Account. Associating it gives them the same experience as their other App Store subscriptions: the group subscription appears in their subscription settings, and their name appears in the group purchaser’s. Associate each seat as soon as you know the member’s `appTransactionId`, whether you get it when they use your app on an Apple device or stored it from an earlier visit, even if they access your content outside of your app.

If the invited member’s account has Ask to Buy turned on, associating their seat also tells a parent or guardian or the Family Organizer that the member has access, and asks whether to allow the member to keep it. If they choose Don’t Allow, the App Store unclaims the member’s seat and sends an `UNCLAIM_SEATS` notification, and you must revoke the member’s access; see [Respond when the App Store unclaims seats](./hosting-group-invitations-in-your-app.md#Respond-when-the-App-Store-unclaims-seats).

Associating a seat doesn’t change a member’s access: you grant and revoke access based on the seat claims your server records.

To associate a seat, you need the member’s `appTransactionId`. Read [`appTransactionID`](./apptransaction/apptransactionid.md) in your app and send it to your server, or use one your server stored earlier:

```swift
let result = try await AppTransaction.shared
if case .verified(let appTransaction) = result {
    // Send appTransaction.appTransactionID to your server, with the member's account.
}
```

If you have the member’s `appTransactionId` when you claim the seat, include it in the Claim Seat request. If you don’t — for example, because the member hasn’t installed or opened your app on an Apple device — claim the seat without it, and call Associate Seat if you learn it later.

An invited member can leave the group from their subscription settings by choosing Leave Subscription. They lose access, the App Store unclaims their seat, and your server receives an `UNCLAIM_SEATS` notification; see [Respond when the App Store unclaims seats](./hosting-group-invitations-in-your-app.md#Respond-when-the-App-Store-unclaims-seats). If a member chooses to remove the subscription from their Apple Account instead, the subscription only leaves their subscription settings: their seat and access don’t change, and you aren’t notified.

## Grant and revoke member access

Grant a member access once you claim their seat, and tie it to the group purchaser’s subscription: when that subscription expires, is revoked, or is refunded in full, revoke access for every invited member. For the events that affect a group, see [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md).

When an invited member leaves the group in your app or on your website, or the group purchaser removes them there, revoke their access right away and call Unclaim Seat. The seat becomes available for someone else; the group size doesn’t change. When a member leaves the group from their subscription settings instead, the App Store unclaims the seat for you; see [Respond when the App Store unclaims seats](./hosting-group-invitations-in-your-app.md#Respond-when-the-App-Store-unclaims-seats).

## Handle a smaller group at renewal

The group purchaser can reduce the group size in their subscription settings, effective at the next renewal. Each time they change it, your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `DECREASE_QUANTITY`; compare its `renewalQuantity` with the number of claimed seats, plus the group purchaser’s own seat, to find out whether the group will have more members than seats after the renewal. The App Store never unclaims seats to fit a smaller group: after the renewal, the group can have more claimed seats than paid seats, and claims fail until you unclaim enough of them. The claimed seats have to fit in the new size, minus the group purchaser’s seat; for example, if a group of ten with nine claimed seats renews at six, unclaim at least four.

Ask the group purchaser which members to remove before the renewal date, and unclaim those seats when the renewal takes effect, so those members keep access until the end of the period that was paid for. If they don’t choose, decide which seats to unclaim — for example, the most recently claimed.

## Respond when the App Store unclaims seats

The App Store unclaims seats that invited members hold when a member leaves the group from their subscription settings, when a seat refund covers more seats than are unclaimed, and when a parent or guardian or the Family Organizer declines a member’s request to keep access. Your server then receives an `UNCLAIM_SEATS` notification whose [`unclaimInfo`](../AppStoreServerNotifications/unclaiminfo.md) lists the unclaimed seats. The App Store has already unclaimed them, so revoke access for the members whose `seatClaimId` appears in `unclaimSeatIds`.

## See Also

### Related Documentation
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.
- [Testing multiseat subscriptions](./testing-multiseat-subscriptions.md)
  Test group purchases, invitations, seat changes, refunds, and purchases from organizations in the sandbox environment before you release your app.
### Multiseat subscriptions
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/hosting-group-invitations-in-your-app)*