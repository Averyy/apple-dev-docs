# promotionalOffer(offerID:signature:)

**Framework**: StoreKit  
**Kind**: method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption
```

## See Also

- [static func appAccountToken(UUID) -> Product.PurchaseOption](product/purchaseoption/appaccounttoken(_:).md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](product/purchaseoption/winbackoffer(_:).md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func quantity(Int) -> Product.PurchaseOption](product/purchaseoption/quantity(_:).md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:signature:))*