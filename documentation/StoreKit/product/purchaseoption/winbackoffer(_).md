# winBackOffer(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Sets a win-back offer to apply to the purchase.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func winBackOffer(_ offer: Product.SubscriptionOffer) -> Product.PurchaseOption
```

## Discussion

To test win-back offers in Xcode, set up the offers in your StoreKit configuration file. For more information, see [Setting up StoreKit Testing in Xcode](../../../Xcode/setting-up-storekit-testing-in-xcode.md).

## Parameters

- `offer`: The [`Product.SubscriptionOffer`](../subscriptionoffer.md) instance that represents the win-back offer to apply to the purchase.

## See Also

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](./appaccounttoken%28_%29.md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](./promotionaloffer%28offerid,keyid,nonce,signature,timestamp%29.md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](./promotionaloffer%28offerid,signature%29.md)
- [static func quantity(Int) -> Product.PurchaseOption](./quantity%28_%29.md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/winbackoffer(_:))*