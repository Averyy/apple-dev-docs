# appAccountToken(_:)

**Framework**: StoreKit  
**Kind**: method

Sets a UUID to associate the purchase with an account in your system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func appAccountToken(_ token: UUID) -> Product.PurchaseOption
```

#### Return Value

An instance of [`Product.PurchaseOption`](product/purchaseoption.md) to use in [`purchase(options:)`](product/purchase(options:).md).

#### Discussion

When you set the app account token in the purchase options, the App Store returns the same app account token value in the resulting transaction, in [`appAccountToken`](transaction/appaccounttoken.md).

## Parameters

- `token`: A UUID you provide to associate with the purchase.

## See Also

- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](product/purchaseoption/winbackoffer(_:).md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:signature:).md)
- [static func quantity(Int) -> Product.PurchaseOption](product/purchaseoption/quantity(_:).md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/appaccounttoken(_:))*