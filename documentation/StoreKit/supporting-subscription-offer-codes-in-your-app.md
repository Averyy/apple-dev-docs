# Supporting offer codes in your app

**Framework**: StoreKit

Enable customers to redeem offer codes through the App Store or within your app.

#### Overview

To help you acquire, retain, and win back customers, you can use offer codes. Offer codes are alphanumeric codes that provide In-App Purchases at a discount or for free, for a specific duration. Offer codes are available for all in-app purchase types:  consumables, non-consumables, non-renewing subscriptions, and auto-renewable subscriptions. You can merchandise offer codes within your app or outside of it through your marketing channels.

Create and configure offer codes in App Store Connect, and distribute them to your customers. Customers can redeem offer codes throught a redemption URL, or by entering the code directly in the App Store, or within your app if it implements one of the following APIs:

- [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) on iOS, iPadOS, macOS, and visionOS
- [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) on iOS, iPadOS, and visionOS
- [`presentOfferCodeRedeemSheet(from:)`](appstore/presentoffercoderedeemsheet(from:).md) on macOS

When customers redeem a valid offer code, your app receives a successful transaction. If customers redeem offer codes in the App Store and don’t have your app installed, they’re prompted to download it as part of the redemption flow. Successfully redeeming an offer code entitles the customer to the product, the same as a purchase does. Your app needs to provide service for the product.

Offer codes for auto-renewable subscriptions are available starting in iOS 14.2, iPadOS 14.2, macOS 15.0, and visionOS 1.0. Offer codes for consumables, non-consumables, and non-renewing subscriptions are available starting in iOS 16.3, iPadOS 16.3,  macOS 15.0, and visionOS 1.0.

##### Set Up Offer Codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. There are three types of offer codes: one-time use codes, custom codes, and sandbox codes for testing. The offer code redemption APIs support all offer codes types. You can have up to 10 active offers at at time, with a limit of 1,000,000 codes per app, per quarter. To distribute offer codes to your customers, download them from App Store Connect.

For more information on creating and distributing offer codes, and to learn which type of offer code may work for your campaign, see [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes) and [`Create offer codes for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

##### Redeem Offer Codes in Your App

To display the system sheet for customers to redeem offer codes within your app, call one of the redemption APIs, depending on your app’s UI implementation:

- Call [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) if your app uses SwiftUI.
- Call [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) if your app uses UIKit.
- Call [`presentOfferCodeRedeemSheet(from:)`](appstore/presentoffercoderedeemsheet(from:).md) if your app uses AppKit for macOS.

The redemption sheet takes care of the redemption flow, including alerting customers about invalid entries, as appropriate. For example, an entry may be invalid if the offer code is expired or invalid, or if redeeming the code would result in a subscription downgrade.

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](transaction/updates.md).  To ensure your app receives all the transactions that `updates` emits, set up the task to listen for transactions as soon as your app launches. See [`updates`](transaction/updates.md) for a code example.

Including the redemption sheet in your app is recommended, but optional. For more guidance on supporting offer code redemption within your app, see Human Interface Guidelines > [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase).

##### Support Offer Codes Redeemed Outside of Your App

Customers may redeem offer codes outside your app, by entering the offer code in the App Store, or by using a redemption URL. To handle offer codes — and other transactions that can occur outside of your app — your app needs to use [`updates`](transaction/updates.md) on [`Transaction`](transaction.md) to receive new transactions while the app is running. Create a [`Task`](https://developer.apple.com/documentation/Swift/Task) to iterate through the transactions from the listener as soon as your app launches. For more information and sample code, see [`updates`](transaction/updates.md).

When your app launches, it needs to check [`currentEntitlements`](transaction/currententitlements.md) and [`unfinished`](transaction/unfinished.md) on [`Transaction`](transaction.md) to get any transactions that may have occurred while the app wasn’t running. Process the transactions to ensure your app provides service for all products it’s entitled to. Call [`finish()`](transaction/finish().md) after you process the unfinished transactions.

##### Identify Products Purchased with Offer Codes

When customers successfully redeem offer codes, the transaction contains fields that identify the offer and its offer type. Find the offer code details in the transaction information, in your app and on your server, as follows.

In your app, use the following StoreKit APIs to locate the offer code information:

- Check the [`offer`](transaction/offer-swift.property.md) property of [`Transaction`](transaction.md), and its [`type`](transaction/offer-swift.struct/type.md) property. An offer type value of [`code`](transaction/offertype-swift.struct/code.md) indicates the customer redeemed an offer code.
- If the offer code redemption applies to an auto-renewable subscription’s next renewal period, see the [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md) properties [`offerID`](product/subscriptioninfo/renewalinfo/offerid.md) and [`offerType`](transaction/offertype-swift.property.md). An offer type value of [`code`](transaction/offertype-swift.struct/code.md) indicates the customer redeemed an offer code.

On your server, use the following server-side APIs to locate offer code information:

- In the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI), when you call endpoints such as [`Get Transaction History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Transaction-History), [`Get All Subscription Statuses`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses), and others, the response contains the signed transaction, [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction). In its decoded payload, [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload), look for the fields [`offerIdentifier`](https://developer.apple.com/documentation/AppStoreServerAPI/offerIdentifier) and [`offerType`](https://developer.apple.com/documentation/AppStoreServerAPI/offerType). An [`offerType`](https://developer.apple.com/documentation/AppStoreServerAPI/offerType) value of `3` indicates the customer redeemed an offer code.
- You receive a notification on your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint if someone redeems an offer code. The [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) is `OFFER_REDEEMED` when someone redeems an offer for an active auto-renewable subscription; `SUBSCRIBED` when they redeem the offer code as an initial purchase or to resubscribe. The `notificationType` is `ONE_TIME_CHARGE` when someone redeems an offer code for a consumable, non-consumable, or non-renewing subscription product type. The decoded payloads [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) and [`JWSRenewalInfoDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) contain the fields [`offerIdentifier`](https://developer.apple.com/documentation/AppStoreServerNotifications/offerIdentifier) and [`offerType`](https://developer.apple.com/documentation/AppStoreServerNotifications/offerType).

##### Provide Service to New and Existing Customers

When you acquire new customers with an offer code, they already have an In-App Purchase when they open your app for the first time. In addition to enabling that In-App Purchase, you may need to update your backend system’s records. Your app follows these steps:

1. When the app launches, check [`currentEntitlements`](transaction/currententitlements.md) and [`unfinished`](transaction/unfinished.md) on [`Transaction`](transaction.md) to get the current entitlements and any new consumable transactions, respectively. StoreKit automatically validates the transactions, and returns verified results in [`VerificationResult.verified(_:)`](verificationresult/verified(_:).md). To perform your own validation, use the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property.
2. To determine whether a transaction includes an offer code redemption, check the [`offer`](transaction/offer-swift.property.md) property of [`Transaction`](transaction.md) and [`type`](transaction/offer-swift.struct/type.md) property of `offer`.
3. Provide the service or product based on the offer, and call [`finish()`](transaction/finish().md) on [`Transaction`](transaction.md).
4. Guide new customers through your new-user experience, as needed. Update your backend system’s records.

When an existing customer redeems an offer code within your app, the transaction comes in through the [`updates`](transaction/updates.md) sequence on [`Transaction`](transaction.md). Process the transaction as usual, providing service based on the offer, and call [`finish()`](transaction/finish().md).

##### Test Offer Codes in the Sandbox Environment

You can test your app’s handling of offer codes in the sandbox environment for all In-App Purchase product types: consumable, non-consumable, non-renewing subscription, and auto-renewable subscription. First, create offer codes for the sandbox environment in App Store Connect. For more information on creating these codes, see [`Create offer codes for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases). Each quarter, you can create up to 10,000 codes for testing.

To redeem an offer code in the sandbox environment, follow these steps:

- On your device, sign in using a Sandbox Apple Account.
- On the Sandbox Account Settings page, tap Initiate Transaction.
- Select Offer Codes and redeem a sandbox offer code you created in App Store Connect.

If your app supports redeeming offer codes in your app, test redeeming a sandbox offer code from your app. Navigate to the redemption sheet in your app and enter the offer code.

The sandbox environment operates with these conditions:

- It doesn’t enforce a redemption limit for a Sandbox Apple Account. This means you can test multiple offer codes using the same testing account.
- It ignores eligibility criteria for offer codes for consumable, non-consumable, and non-recurring subscription product types.
- It applies eligibility criteria to offer codes for auto-renewable subscriptions. To test subscription offer codes again, clear the sandbox account purchase history. For more information, see [`Manage Sandbox Apple Account settings`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings)
- It verifies whether an offer code is available in the storefront of the Sandbox Apple Account.

On your server, [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) notifies you of offer code redemptions in the sandbox environment if you enable a notifications endpoint for the sandbox environment. For more information, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md).

For more information on sandbox testing, see [`Testing In-App Purchases with sandbox`](testing-in-app-purchases-with-sandbox.md).

##### Test Offer Codes in Xcode

You can test your app’s handling of offer code redemptions in Xcode for all In-App Purchase product types: consumable, non-consumable, non-renewing subscription, and auto-renewable subscription.

Before you can begin testing in Xcode, complete the steps in [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode), including creating a StoreKit configuration file and enabling StoreKit testing in Xcode.

Start by opening the StoreKit configuration editor in Xcode and including at least one In-App Purchase product. Then follow these steps to configure an offer code:

1. In the left pane, select the product under the appropriate product type heading.
2. Under the Offer Codes heading in the editor, configure an offer code for the product.
3. In your app, implement a Redeem Offer Code button that invokes the StoreKit method, as described above in [`Redeem offer codes in your app`](supporting-offer-codes-in-your-app#Redeem-offer-codes-in-your-app.md)

To test in-app offer code redemption, run your app in the Xcode environment and follow these steps:

1. In the app, tap the Redeem Offer Code button. When you do this, the system displays the Offer Code sheet.
2. Select the offer code that you configured and redeem it. After you redeem it, the system displays the payment sheet with the applied offer.
3. In the app, tap Confirm on the payment sheet.
4. Verify that your app receives the resulting transaction and updates your UI to grant the purchased content without delay.
5. Finish the transaction with [`finish()`](transaction/finish().md).

You can simulate offer code redemptions that occur outside your app, such as from a URL or the App Store, using the Xcode Transaction Manager. To test external redemption, run your app in the Xcode environment and follow these steps:

1. Open the Transaction Manager (Debug > StoreKit > Manage Transactions).
2. Select the product that has offer codes configured.
3. In the secondary configuration view, use the dropdown menu to select an offer code.
4. Complete the redemption. On successful redemption, a new transaction posts to [`updates`](transaction/updates.md) for your app to observe and process.

> **Note**:  The Transaction Manager displays the option to trigger an external offer code redemption only when the StoreKit configuration file contains offer codes for the selected product.

To retry the same test scenario, you may need to delete the previous transaction, depending on the product type. Consumable offer codes are redeemable repeatedly, but non-consumables, non-renewing subscriptions, and auto-renewable subscriptions may block redemption if you’re already entitled. To delete a transaction, in Xcode, choose Debug > StoreKit > Manage Transactions, select the transaction, and click Delete.

For more information on configuring StoreKit Testing in Xcode, see [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest).

##### Supporting Systems Earlier Than Ios 16 and Ipados 16

If your app runs on iOS 16 or earlier, and iPadOS 16 or earlier, you can support offer codes for auto-renewable subscriptions only. Use [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) to display the offer code redemption UI. Otherwise, use the APIs referred to in this article. For more information about supporting earlier systems, see [`Implementing offer codes in your app`](implementing-offer-codes-in-your-app.md).

## See Also

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
  Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
  Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype.md)
  The types of offers for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/supporting-subscription-offer-codes-in-your-app)*