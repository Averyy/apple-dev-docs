# purchase(confirmIn:options:)

**Framework**: StoreKit  
**Kind**: method

Initiates a purchase for the product with the App Store and displays the confirmation sheet.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func purchase(confirmIn scene: some UIScene, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

#### Return Value

The result of the purchase, [`Product.PurchaseResult`](product/purchaseresult.md).

#### Discussion

StoreKit provides several APIs you can use to enable customers to initiate a purchase. Before using [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-6dj6y.md), consider the following APIs and choose the one that best suits your app’s implementation:

- Use [`PurchaseAction`](purchaseaction.md) for apps that use [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) on any platform, including multi-scene apps for visionOS.
- Use [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-6dj6y.md) for apps that use [`UIKit`](https://developer.apple.com/documentation/UIKit).
- Use [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-8eai6.md) for apps that run on macOS and use [`AppKit`](https://developer.apple.com/documentation/AppKit).
- Use [`purchase(options:)`](product/purchase(options:).md) for apps that runs on watchOS.

> ❗ **Important**:  If you use StoreKit views such as [`ProductView`](productview.md), [`StoreView`](storeview.md), or [`SubscriptionStoreView`](subscriptionstoreview.md) you don’t need to call any other API to initiate a purchase. StoreKit manages the purchase action automatically, including presenting the purchase confirmation UI. For more information, see [`StoreKit views`](storekit-views.md).

This method may throw a [`Product.PurchaseError`](product/purchaseerror.md) or [`StoreKitError`](storekiterror.md).

## Parameters

- `scene`: The   the system uses to show the purchase confirmation UI.
- `options`: A set of options ( ) you can associate with the purchase.

## See Also

- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: UIViewController, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-3bivf.md)
  Processes a purchase for the product.
- [func purchase(confirmIn: NSWindow, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-8eai6.md)
  Processes a purchase for the product.
- [Product.PurchaseOption](product/purchaseoption.md)
  Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.
- [Product.PurchaseError](product/purchaseerror.md)
  Error information for product purchase errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchase(confirmin:options:)-6dj6y)*