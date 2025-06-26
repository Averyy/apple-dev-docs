# purchase(options:)

**Framework**: StoreKit  
**Kind**: method

Initiates a purchase for the product with the App Store and displays the confirmation sheet.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
func purchase(options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md)

#### Return Value

Returns a [`Product.PurchaseResult`](product/purchaseresult.md).

#### Discussion

StoreKit provides several APIs you can use to enable customers to initiate a purchase. Before using [`purchase(options:)`](product/purchase(options:).md) consider the following APIs and choose the one that best suits your app’s implementation:

- Use [`PurchaseAction`](purchaseaction.md) for apps that use [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) on any platform, including multi-scene apps for visionOS.
- Use [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-6dj6y.md) for apps that use [`UIKit`](https://developer.apple.com/documentation/UIKit).
- Use [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-8eai6.md) for apps that run on macOS and use [`AppKit`](https://developer.apple.com/documentation/AppKit).
- Use [`purchase(options:)`](product/purchase(options:).md) for apps that runs on watchOS.

> ❗ **Important**:  If you use StoreKit views such as [`ProductView`](productview.md), [`StoreView`](storeview.md), or [`SubscriptionStoreView`](subscriptionstoreview.md) you don’t need to call any other API to initiate a purchase. StoreKit manages the purchase action automatically, including presenting the purchase confirmation UI. For more information, see [`StoreKit views`](storekit-views.md).

##### Use the Purchase Api

Call the [`purchase(options:)`](product/purchase(options:).md) method when a customer initiates a purchase, either within your app or after selecting a promoted in-app purchase on the App Store. This method brings up the system-confirmation sheet. The user can confirm to complete the transaction or cancel it.

Include the purchase options to provide additional information about the purchase, such as:

- [`appAccountToken(_:)`](product/purchaseoption/appaccounttoken(_:).md) to associate the purchase with the resulting transaction
- [`promotionalOffer(offerID:keyID:nonce:signature:timestamp:)`](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md), if the customer is redeeming a promotional offer for an auto-renewable subscription
- [`quantity(_:)`](product/purchaseoption/quantity(_:).md), if the customer is purchasing more than one of the product

The following example illustrates calling [`purchase(options:)`](product/purchase(options:).md) using the `options` parameter to provide an app account token:

```swift
let appAccountToken = <# Generate an app account token. #>
let purchaseResult = try await product.purchase(options: [
    .appAccountToken(appAccountToken)
])
```

If you’re testing your app in the sandbox environment, test an Ask to Buy scenario by setting the [`simulatesAskToBuyInSandbox(_:)`](product/purchaseoption/simulatesasktobuyinsandbox(_:).md) purchase option to `true`. For more information about Ask to Buy, see [`Approve what kids buy with Ask to Buy`](https://developer.apple.comhttps://support.apple.com/en-us/HT201089).

This method may throw a [`Product.PurchaseError`](product/purchaseerror.md) or [`StoreKitError`](storekiterror.md).

For more information about purchases that users initiate on the App Store, see [`Promoting In-App Purchases`](promoting-in-app-purchases.md).

## Parameters

- `options`: A set of options you can associate with the purchase.

## See Also

- [struct PurchaseAction](purchaseaction.md)
  An action that starts an In-App Purchase.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchase(options:))*