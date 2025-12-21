# In-App Purchase

**Framework**: StoreKit

Offer content and services in your app across Apple platforms using a Swift-based interface.

#### Overview

With the In-App Purchase API, you can offer customers the opportunity to purchase digital content and services in your app. Customers can make the purchases within your app, and find your promoted products on the App Store.

The StoreKit framework connects to the App Store on your app’s behalf to prompt for, and securely process, payments. The framework then notifies your app, making the transactions for In-App Purchases available to your app on all of the customer’s devices. For each transaction that represents a current purchase, your app delivers the purchased products. To validate purchases, you can verify transactions on your server, or rely on StoreKit’s verification.

![A diagram of the interactions between StoreKit, your app, the App Store, and your server that occur during a transaction.](https://docs-assets.developer.apple.com/published/3cddba76b6de9f552b4afc2d69fd0799/media-4447232%402x.png)

The App Store can also communicate with your server. It notifies your server of transactions and auto-renewable subscription events through [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications), and provides the same transaction information, and more, through the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).

To learn how adding In-App Purchases fits in an overall app development workflow for the App Store, see [`App Store Pathway`](https://developer.apple.comhttps://developer.apple.com/app-store/pathway/). For an overview of In-App Purchases and its features, including its configuration, testing capabilities, marketing for your products, and more, see [`Simple and safe In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/). For an overview on subscriptions, including creating subscription groups, Family Sharing, and more, see [`Auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/).

##### Configure in App Purchases

To use the In-App Purchase API, you first need to configure the products that your app merchandises.

- In the early stages of development, you can configure the products in the StoreKit configuration file in Xcode, and test your code without any dependency on App Store Connect. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).
- When you’re ready for sandbox testing and production, configure the products in App Store Connect. You can add or remove products and refine or reconfigure existing products as you develop your app. For more information, see [`Configure In-App Purchase settings`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases).

You can also offer apps and In-App Purchases that run on multiple platforms as a single purchase. For more information on universal purchase, see [`Add platforms`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-platforms/).

##### Support a Store in Your App

The In-App Purchase API takes advantage of Swift features like concurrency to simplify your In-App Purchase workflows, and SwiftUI to build stores with [`StoreKit views`](storekit-views.md). Use the API to manage access to content and subscriptions, receive App Store-signed transaction information, get the history of all In-App Purchase transactions, and more.

> **Note**:  Session 10114: [`Meet StoreKit 2`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10114/)

The In-App Purchase API offers:

- Transaction information that’s App Store-signed in JSON Web Signature (JWS) format.
- Transaction and subscription status information that’s simple to parse in your app.
- An entitlements API, [`currentEntitlements`](transaction/currententitlements.md), that simplifies determining entitlements to unlock content and services for your customers.

> **Note**:  Session 110404: [`Implement proactive in-app purchase restore`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110404/)

To support a store in your app, implement the following functionality:

- Listen for transaction state changes using the transaction listener, [`updates`](transaction/updates.md), to provide up-to-date service and content while your app is running.
- Use [`StoreKit views`](storekit-views.md) to merchandise your products; or request products to display from the App Store with [`products(for:)`](product/products(for:).md) and enable purchases using [`purchase(options:)`](product/purchase(options:).md). Unlock purchased content and services based on the purchase result, [`Product.PurchaseResult`](product/purchaseresult.md).
- Iterate through a customer’s purchases anytime using the transaction sequence [`all`](transaction/all.md), and unlock the purchased content and services.
- Optionally, validate the signed transactions and signed subscription status information that you receive from the API.

## Topics

### In-App Purchase merchandising
- [StoreKit views](storekit-views.md)
  Display a customizable In-App Purchase store using StoreKit views for SwiftUI.
### Product and subscription information
- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md)
  Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [struct Product](product.md)
  Information about a product that you configure in App Store Connect.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [typealias SubscriptionInfo](subscriptioninfo.md)
  Information about an auto-renewable subscription.
- [typealias SubscriptionStatus](subscriptionstatus.md)
  Represents the renewal status information for an auto-renewable subscription.
### Purchase requests and results
- [struct PurchaseAction](purchaseaction.md)
  An action that starts an In-App Purchase.
- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.
### Transaction history and entitlements
- [struct Transaction](transaction.md)
  Information that represents the customer’s purchase of a product in your app.
- [static var updates: Transaction.Transactions](transaction/updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.
### JWS verification
- [enum VerificationResult](verificationresult.md)
  A type that describes the result of a StoreKit verification.
- [VerificationResult.VerificationError](verificationresult/verificationerror.md)
  Error cases for StoreKit JWS verification.
### Subscription status and renewal information
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo](product/subscriptioninfo/renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [typealias SubscriptionRenewalInfo](subscriptionrenewalinfo.md)
  Represents the renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionRenewalState](subscriptionrenewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionPeriod](subscriptionperiod.md)
  Represents the duration of time between subscription renewals.
### Offers
- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
  Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
  Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype.md)
  The types of offers for auto-renewable subscriptions.
### Promoted In-App Purchases
- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
  Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [struct PurchaseIntent](purchaseintent.md)
  An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [Product.PromotionInfo](product/promotioninfo.md)
  Information about a promoted In-App Purchase that customizes its order and visibility on the device.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md)
  Test your In-App Purchases before making your app available in the App Store.
### App Store interactions
- [enum AppStore](appstore.md)
  Interactions with the App Store, such as managing subscriptions, verifying devices, authorizing payments, synchronizing transactions, getting the environment, and more.
- [struct AppTransaction](apptransaction.md)
  Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.
### Storefront information
- [struct Storefront](storefront.md)
  The region and unique identifier of the App Store storefront for the device.
- [static var current: Storefront?](storefront/current.md)
  The current App Store storefront for product purchases.
- [static var updates: Storefront.Storefronts](storefront/updates.md)
  The asynchronous sequence that emits storefront information when the system updates the storefront.
### In-App Purchase Testing
- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)
  Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md)
  Validate your app’s handling of win-back offers that you configure for the testing environment.
- [Testing Ask to Buy in Xcode](testing-ask-to-buy-in-xcode.md)
  Validate your app’s handling of Ask To Buy in the testing environment.
### Advanced Commerce API interactions
- [struct AdvancedCommerceProduct](advancedcommerceproduct.md)
  A product configured as a generic SKU in App Store Connect for use with the Advanced Commerce API.
- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md)
  Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.
- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md)
  Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.
### Errors
- [enum StoreKitError](storekiterror.md)
  StoreKit In-App Purchase error codes.
### Deprecated
- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md)
  Use the latest API to support In-App Purchases in new or existing apps, or the original API to support In-App Purchases in earlier operating systems.
- [Original API for In-App Purchase](original-api-for-in-app-purchase.md)
  Offer additional content and services in your app using the Original In-App Purchase API.

## See Also

- [Understanding StoreKit workflows](understanding-storekit-workflows.md)
  Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](getting-started-with-in-app-purchases-using-storekit-views.md)
  Set up an in-app store using SwiftUI and StoreKit views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/in-app-purchase)*