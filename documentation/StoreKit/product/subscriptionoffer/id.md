# id

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The offer identifier.

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
let id: String?
```

## Mentions

- [Merchandising win-back offers in your app](../../merchandising-win-back-offers-in-your-app.md)

#### Discussion

The [`id`](./id.md) is a string that contains the alphanumeric offer identifier you provide when you configure an offer in App Store Connect.

This value is `nil` if the offer is an [`introductory`](./offertype/introductory.md) offer.

Pass the [`id`](./id.md) to a method in [`purchase(options:)`](../purchase%28options%29.md) to create a purchase option based on the offer’s [`type`](./type.md). For example, pass the [`id`](./id.md) for a promotional offer to the [`promotionalOffer(offerID:signature:)`](../purchaseoption/promotionaloffer%28offerid,signature%29.md) to apply the promotion to a purchase.

For more information about configuring offers in App Store Connect, see [`Product.SubscriptionOffer`](../subscriptionoffer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/id)*