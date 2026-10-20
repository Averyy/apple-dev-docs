# promotionalOffer(offerID:keyID:nonce:signature:timestamp:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Applies a promotional offer for an auto-renewable subscription.

**Availability**:
- iOS 15.0+ - Deprecated in 26.0
- iPadOS 15.0+ - Deprecated in 26.0
- Mac Catalyst 15.0+ - Deprecated in 26.0
- macOS 12.0+ - Deprecated in 26.0
- tvOS 15.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 8.0+ - Deprecated in 26.0

> **Deprecated**: Sign promotional offers with JWS and use promotionalOffer(_:compactJWS:) instead

## Declaration

```swift
static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption
```

#### Return Value

An instance of [`Product.PurchaseOption`](../purchaseoption.md) to use in [`purchase(options:)`](../purchase%28options%29.md).

#### Discussion

For information about `keyID`, `nonce`, `signature`, and `timestamp`, see [Generating a signature for promotional offers](../../generating-a-signature-for-promotional-offers.md). If you’re providing an [`appAccountToken(_:)`](./appaccounttoken%28_%29.md) in the purchase options, you must include that value when you generate the `signature`. Use lowercase for the UUID string representations of the app account token and the `nonce` in the signature.

You can offer a discounted or free period of service for auto-renewable subscriptions on iOS, iPadOS, macOS, and tvOS using promotional offers. Before you can provide promotional offers in your app, you must set up the offers in your App Store Connect account. To configure your offer, see [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

## Parameters

- `offerID`: The subscription-offer identifier, [`id`](../subscriptionoffer/id.md).
- `keyID`: The key ID of the subscription key.
- `nonce`: The antireplay value used in the signature. Use lowercase.
- `signature`: The cryptographic signature of the offer parameters, which you generate on your server.
- `timestamp`: The UNIX time, in milliseconds, when you generate the signature.

## See Also

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](./appaccounttoken%28_%29.md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](./winbackoffer%28_%29.md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](./promotionaloffer%28offerid,signature%29.md)
- [static func quantity(Int) -> Product.PurchaseOption](./quantity%28_%29.md)
  Indicates the quantity of items the customer is purchasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:))*