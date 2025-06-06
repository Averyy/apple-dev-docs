# purchase(compactJWS:confirmIn:options:)

**Framework**: StoreKit  
**Kind**: method

Processes a purchase for the product.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func purchase(compactJWS: String, confirmIn window: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```

#### Return Value

The result of the purchase.

#### Discussion

> **Note**:  A `PurchaseError`, `StoreKitError`, or `InvalidRequest` error.

 A `PurchaseError`, `StoreKitError`, or `InvalidRequest` error.

## Parameters

- `compactJWS`: The compact JSON Web Signature (JWS) string for the operation.
- `window`: The window the system uses to display purchase confirmation UI in proximity to.
- `options`: A set of purchase options.

## See Also

- [AdvancedCommerceProduct.PurchaseOption](advancedcommerceproduct/purchaseoption.md)
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:confirmin:options:)-54lkw.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:options:).md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchaseresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchase(compactjws:confirmin:options:)-7x4bh)*