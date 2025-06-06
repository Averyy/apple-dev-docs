# quantity(_:)

**Framework**: StoreKit  
**Kind**: method

Indicates the quantity of items the customer is purchasing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func quantity(_ quantity: Int) -> Product.PurchaseOption
```

#### Return Value

An instance of [`Product.PurchaseOption`](product/purchaseoption.md) to use in [`purchase(options:)`](product/purchase(options:).md).

#### Discussion

The quantity applies to consumable in-app purchases and non-renewing subscriptions.

## Parameters

- `quantity`: The default value is 1. The maximum value is 10.

## See Also

- [static func appAccountToken(UUID) -> Product.PurchaseOption](product/purchaseoption/appaccounttoken(_:).md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](product/purchaseoption/winbackoffer(_:).md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:signature:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/quantity(_:))*