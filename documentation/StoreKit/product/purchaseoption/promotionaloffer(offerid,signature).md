# promotionalOffer(offerID:signature:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- macOS 14.4+ - Deprecated in 26.0
- tvOS 17.4+ - Deprecated in 26.0
- visionOS 1.1+ - Deprecated in 26.0
- watchOS 10.4+ - Deprecated in 26.0

> **Deprecated**: Sign promotional offers with JWS and use promotionalOffer(_:compactJWS:) instead

## Declaration

```swift
static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption
```

## See Also

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](./appaccounttoken%28_%29.md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](./winbackoffer%28_%29.md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](./promotionaloffer%28offerid,keyid,nonce,signature,timestamp%29.md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func quantity(Int) -> Product.PurchaseOption](./quantity%28_%29.md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:signature:))*