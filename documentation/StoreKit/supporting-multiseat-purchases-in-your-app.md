# Supporting multiseat purchases in your app

**Framework**: StoreKit  
**Role**: Article

Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.

## Overview

A *multiseat subscription* is an auto-renewable subscription that a customer can buy in a quantity greater than one. Each unit of quantity is a *seat*, and each seat gives one person access to your subscription. You don’t create a new product type; a multiseat purchase uses the same product ID as an individual purchase, and the same subscription can sell both ways.

Customers buy multiseat subscriptions in two ways:

- **Group Purchases**: A customer, the *group purchaser*, buys seats in your app, distributed on the App Store, and invites people to the group. The group purchaser pays for every seat; the people they invite, the *invited members*, are never billed. The group purchaser and the invited members are all members of the group.
- **Volume Purchasing**: An organization buys seats in Apple Business or Apple School Manager and assigns them to people with a device management service.

Supporting multiseat subscriptions involves the following steps:

- Choosing how people join a group, and configuring the subscription in App Store Connect
- Merchandising seat-based pricing and initiating a purchase
- Granting access to the purchaser and to everyone who holds a seat
- Inviting members, and showing the group in your app

Group Purchases requires Xcode 27.3 or later. Customers can buy group subscriptions in your app on iOS, iPadOS, and macOS. The purchase options that buy seats, [`seats(_:)`](./product/purchaseoption/seats%28_%29.md) and [`multiSeatInvitationSheetSuppressed(_:)`](./product/purchaseoption/multiseatinvitationsheetsuppressed%28_%29.md), are available in iOS 15, iPadOS 15, macOS 12, and later. The rest of the multiseat API — including seat-based pricing terms, multiseat transaction information, and the invitation and data sharing consent sheets — requires iOS 27.3, iPadOS 27.3, or macOS 27.3 or later. On every platform, including tvOS, watchOS, and visionOS, your app receives the transactions that grant access to group members and to people who receive a seat from an organization.

Use [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) to follow each group through its life cycle on your server, and the [App Store Server API](../AppStoreServerAPI/AppStoreServerAPI.md) to look up transactions and groups. For seat additions, removals, refunds, and other changes after the purchase, see [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md).

## Understand the customer experience

### Group Purchases

The group purchaser chooses a group size when they subscribe. You decide how your app presents the seat purchase experience and shows prices; see [Merchandise multiseat subscriptions](./supporting-multiseat-purchases-in-your-app.md#Merchandise-multiseat-subscriptions). They pay for every seat in the group, whether or not each seat has a member, and every seat renews together, on the same date each billing period, whatever the subscription’s duration. The group purchaser always holds the first seat, so their own access continues as long as the subscription does. A group holds up to 100 people, including the group purchaser.

After the purchase, the group purchaser invites people to fill the remaining seats. How invitations work depends on the invitation model you choose; see [Choose how people join a group](./supporting-multiseat-purchases-in-your-app.md#Choose-how-people-join-a-group). The group purchaser can add seats at any time, up to the group size limit, in your app or in their subscription settings, and reduce the group size at the next renewal, in their subscription settings. They remove members in their subscription settings with Apple-hosted invitations, or in your app with developer-hosted invitations. Invited members can leave the group at any time.

With Apple-hosted invitations, the group purchaser sees the group’s members in their subscription settings; invited members don’t see each other there. If you turn on Family Sharing for a subscription that also allows multiseat purchases, only the group purchaser can share their access with family members. Every other seat is for individual use only.

### Volume Purchasing

In an organization, an administrator buys seats in Apple Business or Apple School Manager and assigns them to people with a device management service. The people who receive a seat don’t buy anything; the subscription appears in your app as a transaction with an ownership type of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md), almost identical to a standard purchase. You can sell the same subscription to group purchasers in your app and to organizations in Apple Business and Apple School Manager, depending on where you make it available in App Store Connect.

## Compare group purchases and volume purchases

Both kinds of multiseat purchase reach your app as the same kind of transaction, so most of your entitlement code serves both. They differ in who buys, how people get a seat, and what the purchase can include:

| Feature | Group Purchases | Volume Purchasing |
| --- | --- | --- |
| Buyer | A customer, in your app | An organization, in Apple Business or Apple School Manager |
| How people get a seat | An invitation from the group purchaser | An assignment from the organization |
| Group size | Up to 100 people | No maximum |
| Pricing | Per-seat or volume discount | Per-seat or volume discount |
| Subscription offers | Supported, except offer codes | Not supported |
| Family Sharing | Group purchaser only | Not supported |

The [`storeType`](./apptransaction/storetype-swift.property.md) property tells you which store your app came from — the App Store, Apple Business, or Apple School Manager. It describes the app, not a transaction, so don’t use it to decide access to a subscription.

## Choose how people join a group

For Group Purchases, you choose who runs invitations: the App Store, or your app and server. You make this choice in App Store Connect for your app, and it applies to every group subscription a customer buys afterward.

With *Apple-hosted invitations*, the system provides the invitation sheet and the acceptance flow, and the group purchaser manages members in their subscription settings. Every invited member needs an Apple Account in the group purchaser’s storefront. Invited members need to accept invitations on an Apple device. Each invited member who accepts receives their own transaction for your subscription, so you grant access the same way you do for any other customer.

With *developer-hosted invitations*, you design the invitation flow, decide who can accept, and keep the record of who holds each seat. Invited members can accept invitations on any platform and from any storefront. If your content or service has any storefront restrictions, for example for content rights, enforce them yourself before you grant an invited member access. Invited members receive no App Store transaction, so your server is the source of truth for their access. Choosing developer-hosted invitations comes with two obligations, which App Store Connect asks you to confirm: you must keep the App Store’s record of the group’s seats up to date with the seat management endpoints in the App Store Server API, and you must make sure that only age-appropriate customers join your service — on Apple platforms, at a minimum, by using the [Declared Age Range](../DeclaredAgeRange/DeclaredAgeRange.md) API to request that people share their age range with your app. Apple extends its parental controls to group subscriptions: when an invited member’s account has Ask to Buy turned on, Apple asks a parent or guardian or the Family Organizer whether the member can keep access, and if they choose Don’t Allow, you must revoke access for that account. For more information, see [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md).

Both invitation models have the same group size limit.

When you change the invitation setting, it applies to new purchases and resubscriptions. Existing group subscriptions retain their original invitation model, so you need to support both, by reading [`invitationManagement`](./transaction/multiseatinfo-swift.struct/invitationmanagement-swift.property.md) from each group purchaser’s transaction rather than relying on your app’s current setting.

## Configure the subscription in App Store Connect

Multiseat purchasing is a setting on each auto-renewable subscription; you don’t create a separate product. New subscriptions allow multiseat purchases by default. Review your existing subscriptions, and configure them to match your business and the products you offer.

To configure multiseat purchasing:

1. In [App Store Connect](https://appstoreconnect.apple.com/login), select your app, and then select the subscription.
2. In the Purchase Options section, click Edit.
3. Select whether customers can buy multiple seats.
4. Select where customers can buy the subscription: the App Store, Apple Business, Apple School Manager, or a combination.
5. Click Save.

Apple Business and Apple School Manager sell multiseat subscriptions only, so selling there requires multiseat purchasing. For details, including who can edit these settings and what each change means for existing subscribers, see [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

A multiseat subscription uses one of two pricing models:

- **Per-seat pricing**: Every seat costs the price you set for the subscription. This is the default.
- **Volume discount pricing**: You define up to five price tiers, each cheaper per seat than the one before it. Seats fill the most expensive tier first.

## Merchandise multiseat subscriptions

Use the [`Product`](./product.md) API to fetch your subscriptions as you do today. To find out whether a subscription allows multiseat purchases, check [`supportsMultiSeatPurchase`](./product/supportsmultiseatpurchase.md).

A subscription that allows multiseat purchases has separate pricing terms for individual and group purchases. In [`pricingTerms`](./product/subscriptioninfo/pricingterms-swift.property.md), each entry’s [`pricingModel`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.property.md) is either [`Product.SubscriptionInfo.PricingTerms.PricingModel.singlePrice(_:)`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/singleprice%28_%29.md), for an individual purchase, or [`Product.SubscriptionInfo.PricingTerms.PricingModel.seatBased(_:)`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/seatbased%28_%29.md), for a group purchase. Customers buy seats only on an up-front billing plan, so seat-based pricing terms always have the [`upFront`](./product/subscriptioninfo/billingplantype/upfront.md) billing plan type.

Seat-based pricing terms contain the subscription’s price tiers. Each tier covers a range of seats, from `minimumSeats` to `maximumSeats`; the last tier has no maximum. Its `billingInfo` provides the price of one seat in that tier.

The following code example finds the seat-based pricing terms and lists their tiers:

```swift
guard product.supportsMultiSeatPurchase,
      let pricingTerms = product.subscription?.pricingTerms else {
    return
}

for terms in pricingTerms {
    guard case .seatBased(let seatPricing) = terms.pricingModel else {
        continue
    }
    for tier in seatPricing.priceTiers {
        let seats = tier.maximumSeats.map { "\(tier.minimumSeats)-\($0)" } ?? "\(tier.minimumSeats) or more"
        print("\(seats) seats: \(tier.billingInfo.displayPrice) per seat")
    }
}
```

Show customers the price per seat and the total for the group size they choose. No API calculates the total, so add it up tier by tier: seats fill the first tier at its price, then the next tier, and so on. For each tier in [`priceTiers`](./product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetiers.md) that the group size reaches, multiply the tier’s per-seat [`price`](./product/subscriptioninfo/billinginfo/price.md) by the number of seats that fall in that tier, and then add the results. For example, with tiers of 1–5 seats at $9.99 and 6–10 seats at $7.99, eight seats cost 5 × $9.99 + 3 × $7.99, a total of $73.92. To display the total, format it with the product’s [`priceFormatStyle`](./product/priceformatstyle.md).

If you use StoreKit views, [`SubscriptionStoreView`](./subscriptionstoreview.md) can show individual and group pricing side by side. To give each pricing model its own group of plans, add a [`SubscriptionPricingModelGroupSet`](./subscriptionpricingmodelgroupset.md) to the store; a subscription with both single-price and seat-based pricing terms appears in both groups. To choose the pricing terms that a store displays, apply the [`preferredSubscriptionPricingTerms(_:)`](../SwiftUI/view/preferredsubscriptionpricingterms%28_%29.md) modifier to a view, which affects every store inside it, or apply [`preferredSubscriptionPricingTerms(_:)`](./storecontent/preferredsubscriptionpricingterms%28_%29.md) to store content, which affects only that content. When you don’t choose pricing terms for a subscription, the store displays its default pricing terms. If you build a custom [`SubscriptionStoreControlStyle`](./subscriptionstorecontrolstyle.md), read [`preferredPricingTerms`](./subscriptionstorecontrolstyleconfiguration/option/preferredpricingterms.md) to display the pricing terms you chose.

## Provide subscription offers

Group purchases support subscription offers in every payment mode — free trial, pay up front, and pay as you go. Offer codes aren’t available for group purchases. An offer applies to every seat in the group, except seats whose volume discount price is already lower per day than the offer price. Seats that a group purchaser adds while an offer is running join that offer, up to the group size limit. Invited members don’t accrue paid subscription time, so they aren’t eligible for win-back offers. Volume purchases through Apple Business or Apple School Manager don’t support subscription offers of any kind.

If you have an introductory offer on an individual subscription and don’t want it to apply to group purchases, set the customer’s eligibility with the [`introductoryOfferEligibility(compactJWS:)`](./product/purchaseoption/introductoryoffereligibility%28compactjws%29.md) purchase option when initiating a purchase. In StoreKit views, use the [`subscriptionIntroductoryOffer(applyOffer:compactJWS:)`](../SwiftUI/view/subscriptionintroductoryoffer%28applyoffer,compactjws%29.md) modifier.

## Initiate a purchase

To sell a group subscription, call [`purchase(options:)`](./product/purchase%28options%29.md) with the [`seats(_:)`](./product/purchaseoption/seats%28_%29.md) purchase option, which sets the total number of seats the subscription has after the purchase. Combine it with any other purchase options you already use, such as [`appAccountToken(_:)`](./product/purchaseoption/appaccounttoken%28_%29.md).

A successful purchase delivers one transaction to the group purchaser. Its [`purchasedQuantity`](./transaction/purchasedquantity.md) is the number of seats, and its [`multiSeatInfo`](./transaction/multiseatinfo-swift.property.md) describes the price tiers the seats were bought at and the group’s invitation model.

In iOS 27.3, iPadOS 27.3, and macOS 27.3 or later, if the subscription doesn’t allow multiseat purchases, the purchase fails with [`Product.PurchaseError.multiSeatPurchaseDisabled`](./product/purchaseerror/multiseatpurchasedisabled.md). A total lower than the subscription’s current number of seats fails with [`Product.PurchaseError.seatReductionNotAllowed`](./product/purchaseerror/seatreductionnotallowed.md), because only the group purchaser can reduce the number of seats, in their subscription settings.

With Apple-hosted invitations, the system presents the invitation sheet when a group purchase succeeds. To present it yourself later instead, add the [`multiSeatInvitationSheetSuppressed(_:)`](./product/purchaseoption/multiseatinvitationsheetsuppressed%28_%29.md) purchase option with a value of `true`; presenting the sheet yourself requires iOS 27.3, iPadOS 27.3, or macOS 27.3 or later. In earlier versions, the system still presents the invitation sheet after a group purchase. To let the group purchaser invite more people later, call [`showManageSubscriptions(in:subscriptionGroupID:)`](./appstore/showmanagesubscriptions%28in,subscriptiongroupid%29.md) in your app, or link to their subscription settings, where they can invite members.

## Grant access based on entitlements

Granting access to a multiseat subscription works the same way as for any subscription. Check [`currentEntitlements`](./transaction/currententitlements.md), and grant access to the product that each verified, unrevoked transaction represents while its expiration date is in the future. This includes transactions with an [`ownershipType`](./transaction/ownershiptype-swift.property.md) of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md).

Who receives a transaction depends on how they got their seat:

- The group purchaser receives a transaction with an ownership type of [`purchased`](./transaction/ownershiptype-swift.struct/purchased.md).
- An invited member of a group with Apple-hosted invitations receives their own transaction, with an ownership type of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md).
- A person who receives a seat from an organization also receives a transaction with an ownership type of [`assigned`](./transaction/ownershiptype-swift.struct/assigned.md).
- An invited member of a group with developer-hosted invitations receives no transaction. Grant and revoke their access based on the seat claims your server records.

Decide each person’s access from their own transaction, not from the group purchaser’s. Each assigned transaction has its own [`originalID`](./transaction/originalid.md). An invited member’s transaction has no [`appAccountToken`](./transaction/appaccounttoken.md), because the group purchaser’s token isn’t copied to invited members. Invited members’ access ends when the group’s subscription ends. When a group purchaser removes a member, or an organization takes back a seat, that person’s transaction gets a [`revocationType`](./transaction/revocationtype-swift.property.md) of [`assignmentRevocation`](./transaction/revocationtype-swift.struct/assignmentrevocation.md).

To learn which invitation model a group uses, read [`invitationManagement`](./transaction/multiseatinfo-swift.struct/invitationmanagement-swift.property.md) from the transaction’s [`multiSeatInfo`](./transaction/multiseatinfo-swift.property.md).

> **Note**: Some App Store Server API endpoints don’t accept assigned transactions, because the group purchaser or organization controls the subscription. Check the transaction’s ownership type before you call [`Send Consumption Information`](../AppStoreServerAPI/send-consumption-information.md), [`Set App Account Token`](../AppStoreServerAPI/set-app-account-token.md), or [`Extend a Subscription Renewal Date`](../AppStoreServerAPI/extend-a-subscription-renewal-date.md).

## Invite members with Apple-hosted invitations

With Apple-hosted invitations, the system handles the invitation flow, but you decide where it starts. Offer an invitation button wherever a group purchaser manages their group in your app — for example, next to a list of open seats. When the group purchaser taps it, present the invitation sheet for the subscription group.

In SwiftUI, apply the [`multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)`](../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) modifier, passing the subscription group ID. In UIKit, call [`presentMultiSeatInvitationSheet(from:subscriptionGroupID:)`](./appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-5cmtd.md); in AppKit, call [`presentMultiSeatInvitationSheet(from:subscriptionGroupID:)`](./appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-ni0z.md). These APIs require iOS 27.3, iPadOS 27.3, or macOS 27.3 or later. In earlier versions, send the group purchaser to their subscription settings to invite people — for example, by calling [`showManageSubscriptions(in:subscriptionGroupID:)`](./appstore/showmanagesubscriptions%28in,subscriptiongroupid%29.md) in iOS and iPadOS.

```swift
Button("Invite People") {
    isInvitationSheetPresented = true
}
.multiSeatInvitationSheet(isPresented: $isInvitationSheetPresented, subscriptionGroupID: subscriptionGroupID) { result in
    if case .failure(let error) = result {
        // Handle the error.
    }
}
```

The sheet reports only whether the group purchaser completed the invitation flow; your app doesn’t receive details about the invitations they send. When a member accepts an invitation, their device receives a transaction through [`updates`](./transaction/updates.md), and your server receives a `SUBSCRIBED` notification with a subtype of `INITIAL_BUY` or `RESUBSCRIBE`. Grant access when the transaction arrives.

If your app has a group experience — for example, shared team folders, or the coaches in a league — this is also a good moment to ask the group purchaser to share group visibility with you. See [Show the group in your app](./supporting-multiseat-purchases-in-your-app.md#Show-the-group-in-your-app).

If you use StoreKit views, the [`multiSeatInvitationBehavior(_:)`](../SwiftUI/view/multiseatinvitationbehavior%28_%29.md) modifier controls whether [`SubscriptionStoreView`](./subscriptionstoreview.md) presents the invitation sheet automatically after a group purchase.

## Show the group in your app

If your app offers experiences for a whole group — shared content, a group name, or settings that apply to everyone — you can look up who’s in it. Group membership doesn’t determine access; keep granting access from transactions as described in [Grant access based on entitlements](./supporting-multiseat-purchases-in-your-app.md#Grant-access-based-on-entitlements). Apps that only unlock content don’t need group membership at all. Don’t ask the group purchaser repeatedly to share group visibility, and design your group experience to work when they choose not to share it.

On your server, call [`Get Customer Groups`](../AppStoreServerAPI/get-customer-groups.md) with any transaction identifier for a customer to get the groups they belong to. Each group has a `groupId` and a `groupType` that distinguishes Group Purchases from Volume Purchasing. Then call [`Get Group Members`](../AppStoreServerAPI/get-group-members.md) with the `groupId` to list the group’s members by app transaction ID. Get Group Members lists everyone in the group, including the group purchaser; to tell the group purchaser from invited members, compare each `appTransactionId` with the group purchaser’s. To relate those members to accounts in your system, send [`appTransactionID`](./apptransaction/apptransactionid.md) from your app to your server.

For Group Purchases with Apple-hosted invitations, the group purchaser decides whether to share group visibility with you, which lets you see the `appTransactionId` of each of the group’s members. When they don’t share, the group doesn’t appear in these endpoints. They can change their choice at any time in their subscription settings, and you can ask them in your app with the data sharing consent sheet: present the [`multiSeatDataSharingConsentSheet(isPresented:subscriptionGroupID:onCompletion:)`](../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) modifier in SwiftUI, or call [`presentMultiSeatDataSharingConsentSheet(from:subscriptionGroupID:)`](./appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-9gr5s.md) in UIKit or [`presentMultiSeatDataSharingConsentSheet(from:subscriptionGroupID:)`](./appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-3j1t4.md) in AppKit.

To decide whether to ask, check [`multiSeatDataSharingConsentEligibility`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md). Offer your request — for example, a button that explains what you use group visibility for — only when the value is [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.eligible`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/eligible.md), and check again each time before you present the sheet; presenting it without a new check throws [`StoreKitError.unsupported`](./storekiterror/unsupported.md). When the value is [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.ineligible(_:)`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligible%28_%29.md), the reason tells you why not to ask:

- **[`alreadyConsented`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason/alreadyconsented.md)**: The group purchaser already responded. Don’t ask again; they can change their choice in their subscription settings.
- **[`noOwnedActiveSubscription`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason/noownedactivesubscription.md)**: The person is a member rather than the group purchaser, or the subscription isn’t active.
- **[`notAppleManaged`](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason/notapplemanaged.md)**: The subscription uses developer-hosted invitations, and your own records describe the group.

Eligibility tells you whether you can ask, not what the group purchaser chose. To find out whether they share group visibility with you, call [`Get Customer Groups`](../AppStoreServerAPI/get-customer-groups.md) from your server.

For Volume Purchasing, Get Customer Groups also reports the customer’s role for each of your products. A role of `ADMIN` identifies a person who manages the group’s membership for their organization; use it, for example, to let them configure settings for the group. A role doesn’t grant access.

To let the group purchaser manage their group, call [`showManageSubscriptions(in:subscriptionGroupID:)`](./appstore/showmanagesubscriptions%28in,subscriptiongroupid%29.md), or [`showManageSubscriptions(from:subscriptionGroupID:)`](./appstore/showmanagesubscriptions%28from,subscriptiongroupid%29.md) on macOS. There, the group purchaser can change the group size and, with Apple-hosted invitations, manage the group’s members.

## See Also

### Related Documentation
- [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.
- [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.
- [Testing multiseat subscriptions](./testing-multiseat-subscriptions.md)
  Test group purchases, invitations, seat changes, refunds, and purchases from organizations in the sandbox environment before you release your app.
### Multiseat subscriptions
- [Hosting group invitations in your app](./hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.
- [Managing the life cycle of multiseat subscriptions](./managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/supporting-multiseat-purchases-in-your-app)*