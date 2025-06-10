# Promoting In-App Purchases

**Framework**: StoreKit

Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.

#### Overview

Starting in iOS 11, you can promote in-app purchases on the App Store.

> **Note**:  To support promoted in-app purchases in apps with a minimum version of iOS 16.4 and later, use [`PurchaseIntent`](purchaseintent.md). For more information, see [`Supporting promoted In-App Purchases in your app`](supporting-promoted-in-app-purchases-in-your-app.md).

Promoted in-app purchases appear on your product page, can appear in search results, and can appear as featured items on an appropriate tab on the App Store. Users can start an in-app purchase on the App Store and then transition to your app to continue the transaction. If your app isn’t installed, they receive a prompt to download it.

Promoting in-app purchases requires two steps:

1. In App Store Connect, set up promotions by uploading promotional images. Use the App Store Promotions feature in App Store Connect to manage their order and visibility. For more information about the setup, see [`Promote in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).
2. In your app, implement the delegate method [`paymentQueue(_:shouldAddStorePayment:for:)`](skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:).md) from the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol to handle the purchase.

> ❗ **Important**:  To enable promoted in-app purchases, your app needs to use either [`PurchaseIntent`](purchaseintent.md) (starting in iOS 16.4) or [`paymentQueue(_:shouldAddStorePayment:for:)`](skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:).md) (starting in iOS 11). Don’t use both at the same time. If necessary, use conditional compilation to identify the OS version the app is running in. For more information, see [`Running code on a specific platform or OS version`](https://developer.apple.com/documentation/Xcode/running-code-on-a-specific-version).

To customize the list of promoted in-app purchases for users, you can override their default order and visibility using [`SKProductStorePromotionController`](skproductstorepromotioncontroller.md). Use overrides to show promotions that are relevant to the user. Overrides are specific to a device, and take effect after the user launches the app at least once. Using [`SKProductStorePromotionController`](skproductstorepromotioncontroller.md) is optional and isn’t required for your in-app purchases to appear on the App Store.

For marketing guidance on this feature, see [`Promoting Your In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/app-store/promoting-in-app-purchases/).

> **Note**:  Promoted in-app purchases aren’t available to compatible iPad or iPhone apps running in visionOS.

##### Complete the Purchase in the App

When a user selects an in-app product to purchase on the App Store, StoreKit automatically opens your app and sends the transaction information to the delegate in the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol. Your app needs to complete the purchase transaction and any related actions that are specific to it.

In the delegate method, return `true` to continue the transaction, or `false` to defer or cancel it.

If your app isn’t installed when the user selects to purchase the in-app product, the App Store automatically downloads the app or prompts the user to purchase it. If the installed version of your app is an older version that doesn’t support in-app purchase promotions, the App Store prompts the user to upgrade the app.

##### Continue the Transaction

To continue an in-app purchase transaction, implement the delegate method in the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol and return `true`. StoreKit then displays the payment sheet, and the user can complete the transaction.

```swift
//Continuing a transaction from the App Store.

//MARK: - SKPaymentTransactionObserver

func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
        for product: SKProduct) -> Bool {
    // Check to see if you can complete the transaction.
    // Return true if you can.
    return true
}
```

##### Defer or Cancel the Transaction

If your app needs to defer or cancel a transaction, return `false`. For example, you may need to defer a transaction if the user is in the middle of onboarding, and continue it after they complete the onboarding. Or, you may need to cancel a transaction if the user has already unlocked the product they’re trying to buy.

To defer a transaction:

1. Save the `payment` to use when the app is ready. The payment already contains information about the product. Don’t create a new [`SKPayment`](skpayment.md) with the same product.
2. Return `false`.
3. After the user finishes the onboarding or other actions that require a deferral, send the saved payment to the payment queue as you do with a typical in-app purchase.

To cancel a transaction:

1. Return `false`.
2. Provide feedback to the user. Although this step is optional, if you don’t provide feedback, the app’s lack of action after the user selects to purchase an in-app product in the App Store may seem like a bug.

```swift
//Handling a transaction from the App Store.

//MARK: - SKPaymentTransactionObserver

func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
        for product: SKProduct) -> Bool {

    // Add code here to check if your app needs to defer the transaction.
    let shouldDeferPayment = ...
    // If you need to defer until onboarding is complete, save the payment and return false.
    if shouldDeferPayment {
        self.savedPayment = payment
        return false
    }

    // Add code here to check if your app needs to cancel the transaction.
    let shouldCancelPayment = ...
    // If you need to cancel the transaction, then return false:
    if shouldCancelPayment {
        return false
    }
}

// If you cancel the transaction, provide feedback to the user.

// Continuing a previously deferred payment.
SKPaymentQueue.default().add(savedPayment)
```

##### Get Visibility Settings

To get the visibility settings for a promoted product, call [`fetchStorePromotionVisibility(for:completionHandler:)`](skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:).md), providing the product information.

```swift
// Reading visibility override of a promoted in-app purchase.

// Fetch product info for "Hidden Beaches pack."

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.fetchStorePromotionVisibility(forProduct: hiddenBeaches,
    completionHandler: { visibility: SKProductSTorePromotionVisiblity, error: Error?) in
        // visibility == .default
})
```

##### Override Visibility Settings

For each device, you can decide whether to make in-app purchases visible or hidden. For example, you may want to hide products the customer already purchased, and show only the products they can buy.

For example, to hide the Pro Subscription product after a user purchases it, fetch the product information and update the store promotion controller with the `.hide` setting, as the following code example shows. The Pro Subscription promoted in-app purchase no longer appears in the App Store on the device.

```swift
// Hide the promoted product Pro Subscription after the user purchases it.

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.update(storePromotionVisibility: .hide, for: proSubscription,
    completionHandler: { (error: Error?) in
        // Completion.
    })
```

##### Override the Order of Promoted Products

You can customize the promoted in-app purchases on each device by overriding their default order. Use overrides to show promotions that are relevant to the user. For example, you can override the order to promote an in-app purchase that unlocks a level in your game when a user reaches the preceding level.

To override the promotion order, add the product information to an array in the order they are to appear. Pass the array to the [`update(storePromotionOrder:completionHandler:)`](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md) method. The App Store displays the products in the array, followed by the remaining promoted products, which appear in the same relative order that you set in App Store Connect.

```swift
// Overriding the order of promoted in-app purchases.

// Fetch product information for three products: Pro Subscription, Fishing Hot Spots, and Hidden Beaches.
let storePromotionController = SKProductStorePromotionController.default()

// Update the order.
let newProductsOrder = [hiddenBeaches, proSubscription, fishingHotSpots]
storePromotionController.updateStorePromotionOrder(newProductsOrder,
    completionHandler: { (error: Error?) in
        // Complete.
    })
```

##### Cancel Order Overrides

To remove overrides and use the default promotion order, send an empty product array to the [`update(storePromotionOrder:completionHandler:)`](skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:).md) method. The App Store then displays the promoted in-app purchase products in the default order that you set in App Store Connect.

##### Fetch Order Overrides

To get the product promotion order for the device, call [`fetchStorePromotionOrder(completionHandler:)`](skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:).md). This method returns an array of products that have an overridden order. If you get an empty array, there aren’t any overrides and the products are in the default order.

```swift
// Getting the order override of promoted in-app purchases.

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.fetchStorePromotionOrder(completionHandler: {
    (products: [SKProduct], error: Error?) in
        // products == [hiddenBeaches, proSubscription, fishingHotSpots]
    })
```

## See Also

- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md)
  Test your In-App Purchases before making your app available in the App Store.
- [class SKProductStorePromotionController](skproductstorepromotioncontroller.md)
  A product promotion controller for customizing the order and visibility of In-App Purchases per device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/promoting-in-app-purchases)*