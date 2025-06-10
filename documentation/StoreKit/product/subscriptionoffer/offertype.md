# Product.SubscriptionOffer.OfferType

**Framework**: StoreKit  
**Kind**: struct

The types of offers for auto-renewable subscriptions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct OfferType
```

## Topics

### Getting offer types
- [static let introductory: Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype/introductory.md)
  An introductory offer for an auto-renewable subscription.
- [static let promotional: Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype/promotional.md)
  A promotional offer for an auto-renewable subscription.
- [static let winBack: Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype/winback.md)
  A win-back offer for an auto-renewable subscription.
### Getting a localized description
- [var localizedDescription: String](product/subscriptionoffer/offertype/localizeddescription.md)
  A string that contains the localized description of the offer type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
  Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
  Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
  Provide subscription service for customers who redeem offer codes through the App Store or within your app.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/offertype)*