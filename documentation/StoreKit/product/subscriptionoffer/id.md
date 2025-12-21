# id

**Framework**: StoreKit  
**Kind**: property

The offer identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let id: String?
```

## Mentions

- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

#### Discussion

The [`id`](product/subscriptionoffer/id.md) is a string that contains the alphanumeric offer identifier you provide when you configure an offer in App Store Connect.

This value is `nil` if the offer is an [`introductory`](product/subscriptionoffer/offertype/introductory.md) offer.

Pass the [`id`](product/subscriptionoffer/id.md) to a method in [`purchase(options:)`](product/purchase(options:).md) to create a purchase option based on the offer’s [`type`](product/subscriptionoffer/type.md). For example, pass the [`id`](product/subscriptionoffer/id.md) for a promotional offer to the [`promotionalOffer(offerID:signature:)`](product/purchaseoption/promotionaloffer(offerid:signature:).md) to apply the promotion to a purchase.

For more information about configuring offers in App Store Connect, see [`Product.SubscriptionOffer`](product/subscriptionoffer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/id)*