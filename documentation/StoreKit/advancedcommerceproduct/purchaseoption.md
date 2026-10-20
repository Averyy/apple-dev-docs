# AdvancedCommerceProduct.PurchaseOption

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
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
- [static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool) -> AdvancedCommerceProduct.PurchaseOption](./purchaseoption/onstorefrontchange%28shouldcontinuepurchase%29.md)
  A closure that determines whether the transaction continues if the device’s App Store storefront changes during a transaction.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Initiating purchases
- [func purchase(compactJWS: String, confirmIn: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-7x4bh.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-54lkw.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,options%29.md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](./purchaseresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchaseoption)*