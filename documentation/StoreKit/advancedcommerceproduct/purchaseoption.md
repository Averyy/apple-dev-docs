# AdvancedCommerceProduct.PurchaseOption

**Framework**: StoreKit  
**Kind**: struct

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct PurchaseOption
```

## Topics

### Type Methods
- [static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool) -> AdvancedCommerceProduct.PurchaseOption](advancedcommerceproduct/purchaseoption/onstorefrontchange(shouldcontinuepurchase:).md)
  A closure that determines whether the transaction continues if the device’s App Store storefront changes during a transaction.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func purchase(compactJWS: String, confirmIn: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:confirmin:options:)-7x4bh.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:confirmin:options:)-54lkw.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchase(compactjws:options:).md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](advancedcommerceproduct/purchaseresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchaseoption)*