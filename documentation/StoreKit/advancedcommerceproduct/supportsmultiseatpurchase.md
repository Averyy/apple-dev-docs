# supportsMultiSeatPurchase

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether multiseat purchases are allowed for this product.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let supportsMultiSeatPurchase: Bool
```

## Discussion

When this value is `true`, you can sell the product as a multiseat subscription. You specify the seats and their price tiers in the Advanced Commerce API request that you sign for the purchase. For more information, see [Advanced Commerce API](../../AdvancedCommerceAPI/AdvancedCommerceAPI.md).

Generic product identifiers for the Advanced Commerce API aren’t enabled for multiseat purchases by default. To sell them in quantity, turn on multiseat purchasing in App Store Connect. For more information, see [Manage purchase options for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

## See Also

### Initiating purchases
- [AdvancedCommerceProduct.PurchaseOption](./purchaseoption.md)
- [func purchase(compactJWS: String, confirmIn: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-7x4bh.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, confirmIn: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,confirmin,options%29-54lkw.md)
  Processes a purchase for the product.
- [func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption>) async throws -> AdvancedCommerceProduct.PurchaseResult](./purchase%28compactjws,options%29.md)
  Processes a purchase for the product.
- [AdvancedCommerceProduct.PurchaseResult](./purchaseresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/supportsmultiseatpurchase)*