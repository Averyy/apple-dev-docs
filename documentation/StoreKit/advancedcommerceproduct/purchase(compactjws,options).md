# purchase(compactJWS:options:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Processes a purchase for the product.

**Availability**:
- watchOS 11.4+

## Declaration

```swift
@MainActor
func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```

#### Return Value

The result of the purchase.

#### Discussion

> **Throws**:  A `PurchaseError`, `StoreKitError`, or `InvalidRequest` error.

## Parameters

- `compactJWS`: The compact JSON Web Signature (JWS) string for the operation.
- `options`: A set of purchase options.

## See Also

### Initiating purchases
- [AdvancedCommerceProduct.PurchaseOption](./purchaseoption.md)
- [func purchase(compactJWS: String, confirmIn: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-7x4bh.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-54lkw.md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](./purchaseresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchase(compactjws:options:))*