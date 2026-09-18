# Using StoreKit in Unity

**Framework**: StoreKit

Provide in-app purchases in Unity-based games using C#.

#### Overview

Apple provides a StoreKit plug-in for Unity — an open source C# wrapper that gives Unity developers direct access to StoreKit, Apple’s framework for implementing in-app purchases. If your game is built in Unity, use this plug-in to add Apple In-App Purchases without writing platform-specific Swift or Objective-C code.

The plug-in exposes the same APIs and the same full feature set available to native Apple developers, through idiomatic C# calls that fit naturally into a Unity project. It’s maintained by Apple, ships as source on GitHub, and includes a sample project demonstrating the core purchase flow.

#### Understand the Storekit Plugins Capabilities

- **[`Product fetching`](https://developer.apple.comhttps://github.com/apple/unityplugins/blob/27-beta/plug-ins/Apple.StoreKit/Apple.StoreKit_Unity/Assets/Apple.StoreKit/Documentation~/Apple.StoreKit.md#fetching-products)** — retrieve product metadata (price, display name, description) for your app’s in-app purchases and subscriptions.
- **[`Purchases`](https://developer.apple.comhttps://github.com/apple/unityplugins/blob/27-beta/plug-ins/Apple.StoreKit/Apple.StoreKit_Unity/Assets/Apple.StoreKit/Documentation~/Apple.StoreKit.md#making-a-purchase)** — initiate a purchase and receive a verification result.
- **Transaction verification** — cryptographically verify transactions via `VerificationResult`.
- **Transaction updates** — listen for real-time transaction changes (renewals, refunds, revocations) via `Transaction.Updates`.
- **Current entitlements** — check what a player currently owns via `GetCurrentEntitlements`.
- **App Transaction** — access app-level purchase information via `AppTransaction`.
- **Offer codes** — present the system integrated offer-code redemption sheet.
- **Subscriptions** — read subscription status, renewal info, and win-back offer eligibility via `SubscriptionInfo`.
- **Promotional offers and purchase intents** — support Apple Search Ads / App Store product page purchase flows via `PurchaseIntent` and `Product.PromotionInfo`.
- **Advanced Commerce** — `AdvancedCommerceProduct` support for custom pricing and purchase options.
- **Storefront and app lifecycle helpers** — `Storefront.GetCurrent`, `AppStore.Sync`, `AppStore.RequestReview`.

#### Getting Started

For installation, setup, and usage instructions, see the plug-in’s [`README`](https://developer.apple.comhttps://github.com/apple/unityplugins/blob/main/README.md) in the GitHub repository — this article doesn’t duplicate that content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/using-storekit-in-unity)*