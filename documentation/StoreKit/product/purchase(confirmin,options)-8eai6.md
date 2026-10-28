# purchase(confirmIn:options:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Processes a purchase for the product.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func purchase(confirmIn window: NSWindow, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Return Value

The result of the purchase

## Discussion

> **Throws**: A `PurchaseError` or `StoreKitError`.

## Parameters

- `window`: The window to show purchase confirmation UI in proximity to.
- `options`: A set of options to configure the purchase.

## See Also

### Purchasing a product
- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28options%29.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28confirmin,options%29-6dj6y.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: UIViewController, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28confirmin,options%29-3bivf.md)
  Processes a purchase for the product.
- [Product.PurchaseOption](./purchaseoption.md)
  Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [Product.PurchaseResult](./purchaseresult.md)
  The result of a purchase.
- [Product.PurchaseError](./purchaseerror.md)
  Error information for product purchase errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchase(confirmin:options:)-8eai6)*