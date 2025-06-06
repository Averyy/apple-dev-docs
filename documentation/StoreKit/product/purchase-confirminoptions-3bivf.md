# purchase(confirmIn:options:)

**Framework**: Storekit  
**Kind**: method

Processes a purchase for the product.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func purchase(confirmIn viewController: UIViewController, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

#### Return Value

The result of the purchase

#### Discussion

> **Note**: A `PurchaseError` or `StoreKitError`.

## Parameters

- `viewController`: The view controller to show purchase confirmation UI in proximity to.
- `options`: A set of options to configure the purchase.

## See Also

- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-6dj6y.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: NSWindow, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-8eai6.md)
  Processes a purchase for the product.
- [Product.PurchaseOption](product/purchaseoption.md)
  Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.
- [Product.PurchaseError](product/purchaseerror.md)
  Error information for product purchase errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchase(confirmin:options:)-3bivf)*