# winBackOffer(_:)

**Framework**: StoreKit  
**Kind**: method

Sets a win-back offer to apply to the purchase.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func winBackOffer(_ offer: Product.SubscriptionOffer) -> Product.PurchaseOption
```

#### Discussion

To test win-back offers in Xcode, set up the offers in your StoreKit configuration file. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

## Parameters

- `offer`: The   instance that represents the win-back offer to apply to the purchase.

## See Also

- [static func appAccountToken(UUID) -> Product.PurchaseOption](product/purchaseoption/appaccounttoken(_:).md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:signature:).md)
- [static func quantity(Int) -> Product.PurchaseOption](product/purchaseoption/quantity(_:).md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/winbackoffer(_:))*