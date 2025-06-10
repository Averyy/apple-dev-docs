# PurchaseIntent

**Framework**: StoreKit  
**Kind**: struct

An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 14.4+

## Declaration

```swift
struct PurchaseIntent
```

## Mentions

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
- [Promoting In-App Purchases](promoting-in-app-purchases.md)

#### Overview

Using `PurchaseIntent` is required in the following cases:

- If you promote in-app purchases on the App Store
- If you turn off the Streamlined Purchasing setting in App Store Connect and use win-back offers or contingent pricing

You set up these offers and settings in App Store Connect. For more information, see [`Promote in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases), [`Set up win-back offers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers), and [`Manage Streamlined Purchasing`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-streamlined-purchasing).

> ❗ **Important**:  To enable promoted in-app purchases, your app must use either [`PurchaseIntent`](purchaseintent.md) (starting in iOS 16.4) or [`paymentQueue(_:shouldAddStorePayment:for:)`](skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:).md) (starting in iOS 11). Don’t use both at the same time. If necessary, use conditional compilation to identify the OS version the app is running in. For more information, see [`Running code on a specific platform or OS version`](https://developer.apple.com/documentation/Xcode/running-code-on-a-specific-version).

When a customer selects a promoted product on the App Store or a win-back offer outside of your app, it initiates a purchase that they complete in your app. If they don’t have your app installed, the system prompts them to download it. After the app downloads, the transaction continues in the app, which receives a purchase intent from the [`intents`](purchaseintent/intents.md) sequence.

The purchase intent identifies the [`product`](purchaseintent/product.md) the customer selected. To enable customers to complete the purchase, call [`purchase(options:)`](product/purchase(options:).md) on this product instance. The following example code receives the purchase intent, and calls a method to complete the purchase workflow:

```swift
func purchaseProduct(_ product: Product) async {
    // Complete the purchase workflow.
    do {
        try await product.purchase()
    }
    catch {
        // Add your error handling here.
    }
    // Add your remaining purchase workflow here.
}

for await purchaseIntent in PurchaseIntent.intents {
    // Complete the purchase workflow.
    await purchaseProduct(purchaseIntent.product)
}

```

For more information, see [`Supporting promoted In-App Purchases in your app`](supporting-promoted-in-app-purchases-in-your-app.md) and [`Supporting win-back offers in your app`](supporting-win-back-offers-in-your-app.md).

In Mac apps built with Mac Catalyst, this instance doesn’t emit purchase intents for promoted in-app purchases because the Mac App Store doesn’t support this feature.

> **Note**:  `PurchaseIntent` and promoted in-app purchases aren’t available to compatible iPad or iPhone apps running in visionOS.

## Topics

### Identifying the product
- [var id: Product.ID](purchaseintent/id.md)
  The product identifier of the In-App Purchase that the customer selects to purchase outside of the app.
- [let product: Product](purchaseintent/product.md)
  The product information of the In-App Purchase the customer selects to purchase outside of the app.
### Getting purchase intents
- [static var intents: PurchaseIntent.PurchaseIntents](purchaseintent/intents.md)
  The asynchronous sequence that emits a purchase intent when customers initiate a purchase outside of the app.
- [PurchaseIntent.PurchaseIntents](purchaseintent/purchaseintents.md)
  An asynchronous sequence of purchase intents for purchases that customers initiate outside of the app.
### Identifying the offer
- [let offer: Product.SubscriptionOffer?](purchaseintent/offer.md)
  The subscription offer that the customer redeems outside of your app.
### Default Implementations
- [Identifiable Implementations](purchaseintent/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
  Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [Product.PromotionInfo](product/promotioninfo.md)
  Information about a promoted In-App Purchase that customizes its order and visibility on the device.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md)
  Test your In-App Purchases before making your app available in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/purchaseintent)*