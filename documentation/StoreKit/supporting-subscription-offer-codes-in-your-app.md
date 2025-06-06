# Supporting subscription offer codes in your app

**Framework**: StoreKit

Provide subscription service for customers who redeem offer codes through the App Store or within your app.

#### Overview

To help you acquire, retain, and win back subscribers, you can use offer codes. Offer codes are alphanumeric codes that provide subscriptions at a discount or for free for a specific duration. Configure the offers and create offer codes in App Store Connect, and distribute them to your customers. Customers can redeem offer codes in the App Store, using offer code redemption URLs, or in your app if it implements one of the following APIs:

- [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) on iOS, iPadOS, macOS, and visionOS
- [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) on iOS, iPadOS, and visionOS
- [`presentOfferCodeRedeemSheet(from:)`](appstore/presentoffercoderedeemsheet(from:).md) on macOS

When customers redeem a valid offer code, your app receives a successful transaction. If customers redeem offer codes in the App Store and don’t have your app installed, they’re prompted to download it as part of the redemption flow. Successfully redeeming an offer code entitles the customer to the auto-renewable subscription, the same as a purchase does. Your app needs to provide service for the product.

##### Set Up Offer Codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. You can have up to 10 active offers per subscription, and create codes for a maximum of 1,000,000 redemptions per app, per quarter. There are two types of offer codes: one-time use codes, and custom codes. The offer code redemption APIs support both.

To distribute offer codes to your customers, download them from App Store Connect. For more information on creating and distributing offer codes, and to learn which type of offer code may work for your campaign, see [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

##### Redeem Offer Codes in Your App

To display the system sheet for customers to redeem offer codes within your app, call one of the redemption APIs, depending on your app’s UI implementation:

- Call [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) if your app uses SwiftUI.
- Call [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) if your app uses UIKit.
- Call [`presentOfferCodeRedeemSheet(from:)`](appstore/presentoffercoderedeemsheet(from:).md) if your app uses AppKit for macOS.

The redemption sheet takes care of the redemption flow, including alerting users about invalid entries, as appropriate. Invalid entries may include, for example, expired offer codes, invalid codes, or codes that would result in a subscription downgrade.

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

Including the redemption sheet in your app is recommended, but optional. For more guidance on supporting offer code redemption within your app, see Human Interface Guidelines > [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase).

##### Support Offer Codes Redeemed Outside of Your App

Customers may redeem offer codes outside your app, by entering the offer code in the App Store, or by using a redemption URL. To handle offer codes — and other transactions that can occur outside of your app — your app needs to use [`updates`](transaction/updates.md) on [`Transaction`](transaction.md) to receive new transactions while the app is running. Create a [`Task`](https://developer.apple.com/documentation/Swift/Task) to iterate through the transactions from the listener as soon as your app launches. For more information and sample code, see [`updates`](transaction/updates.md).

When the app launches, it needs to check [`all`](transaction/all.md) or [`currentEntitlements`](transaction/currententitlements.md) on [`Transaction`](transaction.md) to get any transactions that may have occurred while the app wasn’t running. Process the transactions to ensure your app provides service for all products it’s entitled to.

##### Identify Subscriptions Purchased with Offer Codes

When customers successfully redeem subscription offer codes, the transaction or subscription renewal information contain fields that identify the offer and its offer type. Find the offer code details in the transaction information, in your app and on your server, as follows.

In your app, use the following StoreKit APIs to locate the offer code information:

- See the [`Transaction`](transaction.md) properties [`offerID`](transaction/offerid.md) and [`offerType`](transaction/offertype-swift.property.md). An offer type value of [`code`](transaction/offertype-swift.struct/code.md) indicates the customer redeemed an offer code.
- Some offer code redemptions may apply to an auto-renewable subscription’s next renewal period, for example, if the customer is already subscribed. In this case, see the [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md) properties [`offerID`](product/subscriptioninfo/renewalinfo/offerid.md) and [`offerType`](transaction/offertype-swift.property.md). An offer type value of [`code`](transaction/offertype-swift.struct/code.md) indicates the customer redeemed an offer code.

On your server, use the following server-side APIs to locate offer code information:

- In the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI), when you call endpoints such as [`Get Transaction History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Transaction-History), [`Get All Subscription Statuses`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses), and others, the response contains the signed transaction, [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction). In its decoded payload, [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload), look for the fields [`offerIdentifier`](https://developer.apple.com/documentation/AppStoreServerAPI/offerIdentifier) and [`offerType`](https://developer.apple.com/documentation/AppStoreServerAPI/offerType). An [`offerType`](https://developer.apple.com/documentation/AppStoreServerAPI/offerType) value of `3` indicates the customer redeemed an offer code.
- The [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) sends a notification with an `OFFER_REDEEMED` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) when someone redeems an offer code for an active subscription. It sends a `SUBSCRIBED` notification type if someone redeems the offer code as an initial purchase or to resubscribe. The decoded payloads [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) and [`JWSRenewalInfoDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) contain the fields [`offerIdentifier`](https://developer.apple.com/documentation/AppStoreServerNotifications/offerIdentifier) and [`offerType`](https://developer.apple.com/documentation/AppStoreServerNotifications/offerType). An [`offerType`](https://developer.apple.com/documentation/AppStoreServerNotifications/offerType) value of `3` indicates the customer redeemed an offer code.

##### Provide Subscription Service to New and Existing Customers

When you acquire new customers with an offer code, they already have an auto-renewable subscription when they open your app for the first time. In addition to providing subscription service, you may need to update your backend system’s records. Your app follows these steps:

1. When the app launches, check [`all`](transaction/all.md) or [`currentEntitlements`](transaction/currententitlements.md) on [`Transaction`](transaction.md) to get all transactions or current entitlements, respectively. StoreKit automatically validates the transactions, and returns verified results in [`VerificationResult.verified(_:)`](verificationresult/verified(_:).md). To perform your own validation, use the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property.
2. To determine if a subscription results from an offer code redemption, check the [`offerID`](transaction/offerid.md) and [`offerType`](transaction/offertype-swift.property.md) properties on the subscription’s [`Transaction`](transaction.md).
3. Provide the subscription service based on the offer and call [`finish()`](transaction/finish().md) on [`Transaction`](transaction.md).
4. Guide new customers through your new-user experience, as needed. Update your backend system’s records.

When an existing customer redeems an offer code within your app, the transaction comes in through the [`updates`](transaction/updates.md) sequence on [`Transaction`](transaction.md). Process the transaction as usual, providing service based on the offer, and call [`finish()`](transaction/finish().md).

##### Supporting Systems Earlier Than Ios 16 and Ipados 16

If your app runs on iOS 16 or earlier, and iPadOS 16 or earlier, use [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) to display the offer code redemption UI. Otherwise, use the APIs referred to in this article. For more information about supporting earlier systems, see [`Implementing offer codes in your app`](implementing-offer-codes-in-your-app.md).

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