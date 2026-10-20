# quantity(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Indicates the quantity of items the customer is purchasing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func quantity(_ quantity: Int) -> Product.PurchaseOption
```

#### Return Value

An instance of [`Product.PurchaseOption`](../purchaseoption.md) to use in [`purchase(options:)`](../purchase%28options%29.md).

#### Discussion

The quantity applies to consumable Apple In-App Purchases and non-renewing subscriptions.

## Parameters

- `quantity`: The number of items the customer is purchasing.

  The default value is 1. The maximum value is 10.

## See Also

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](./appaccounttoken%28_%29.md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](./winbackoffer%28_%29.md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](./promotionaloffer%28offerid,keyid,nonce,signature,timestamp%29.md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](./promotionaloffer%28offerid,signature%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/quantity(_:))*