# Implementing offer codes in your app

**Framework**: StoreKit

Provide subscription service for customers who redeem offer codes through the App Store or within an app that uses receipts.

#### Overview

> ❗ **Important**: This article refers to some deprecated APIs from the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) and receipts, also deprecated. To implement offer codes using the  [`In-App Purchase`](in-app-purchase.md) APIs with the [`Transaction`](transaction.md) class, that apply to all product types and not only auto-renewable subscriptions, see [`Supporting offer codes in your app`](supporting-offer-codes-in-your-app.md) instead.

To help you acquire, retain, and win back subscribers, you can use offer codes.

Offer codes are alphanumeric codes that provide auto-renewable subscriptions at a discount or for free for a specific duration. Configure the offers and create offer codes in App Store Connect, and distribute them to your customers. Customers can redeem offer codes in the App Store, using offer code redemption URLs, or in your app if you’ve implemented one of the following APIs:

- [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) or [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md), which are available in iOS 16 and later and iPadOS 16 and later
- [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md), which is available in iOS 14 and later and iPadOS 14 and later.

When customers redeem a valid offer code, your app receives a successful transaction on the payment queue, and you receive a server notification if you’ve enabled [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications). The receipt contains an `offer_code_ref_name` field that identifies the offer.

For information on subscription offer types and choosing the offer type to suit your business needs, see [`Providing subscription offers`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).

##### Set Up Offer Codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. You can have up to 10 active offers per subscription, and create codes for a maximum of 1,000,000 redemptions per app, per quarter. There are two types of offer codes: one-time use codes, and custom codes. The offer code redemption APIs support both.

Download the offer codes from App Store Connect to distribute them to your customers. For more information on creating and distributing offer codes, and to learn which type of offer code may work for your campaign, see [`Set up offer codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1).

##### Redeem Offer Codes in Your App

To display the system sheet for customers to redeem offer codes within your app, call one of the redemption APIs, depending on your app’s UI implementation:

- Call [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) if your app uses SwiftUI.
- Call [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) if your app uses UIKit.
- Call [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) for apps running on devices prior to iOS 16 and iPadOS 16.

The redemption sheet takes care of the redemption flow, including alerting customers about invalid entries, as appropriate. Invalid entries may include, for example, expired offer codes, invalid codes, or codes that would result in a subscription downgrade.

Including the redemption sheet in your app is recommended, but optional. For more guidance on supporting offer code redemption within your app, see Human Interface Guidelines > [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase).

##### Support Offer Codes Redeemed Outside Your App

Customers may redeem offer codes outside your app. If a customer doesn’t have your app, the App Store prompts them to download it as part of the redemption flow.

To handle offer codes — and other transactions that can occur outside of your app – you need to set up a transaction observer at app launch. For more information on this best practice, see [`Setting up the transaction observer for the payment queue`](setting-up-the-transaction-observer-for-the-payment-queue.md). Check that your app’s customer-onboarding experience verifies the receipt and provides subscription service. Update your records if you keep a backend system to manage your subscribers.

##### Identify Subscriptions Purchased with Offer Codes in Receipts

When a customer successfully redeems an offer code, the receipt contains a transaction with the field: `offer_code_ref_name`. This field’s value is the offer reference name that you configure in App Store Connect. The field appears in the [`responseBody.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [`responseBody.Pending_renewal_info`](https://developer.apple.com/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) objects for receipts, and in the [`unified_receipt.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary) and [`unified_receipt.Pending_renewal_info`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt/Pending_renewal_info-data.dictionary) objects for server notifications.

##### Provide Subscription Service to Existing and New Customers

When an existing customer redeems an offer code, your app receives a transaction on the payment queue ([`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) in the [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) state. This flow is the same as a typical subscription purchase flow, but the receipt contains the offer code reference. Your app follows these steps:

1. Validates the receipt. For more information, see [`Validating receipts with the App Store`](validating-receipts-with-the-app-store.md).
2. Looks for the `offer_code_ref_name` field in the receipt to determine if the subscription is from an offer code.
3. Provides the subscription service based on the offer.
4. Calls [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md).

When you acquire new customers with an offer code, they open your app for the first time already having a subscription. In addition to providing subscription service, you may need to update your backend system’s records. Your app follows these steps:

1. When the app first launches, validate the receipt.
2. In the receipt, look for a transaction with the `offer_code_ref_name` field to determine if the subscription is from an offer code.
3. Provide the subscription service based on the offer.
4. Guide the customer through your new-customer experience as needed. Update your backend system’s records.
5. Call [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/implementing-offer-codes-in-your-app)*