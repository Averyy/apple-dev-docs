# Product.SubscriptionOffer.OfferType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The types of offers for auto-renewable subscriptions.

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
struct OfferType
```

## Topics

### Getting offer types
- [static let introductory: Product.SubscriptionOffer.OfferType](./offertype/introductory.md)
  An introductory offer for an auto-renewable subscription.
- [static let promotional: Product.SubscriptionOffer.OfferType](./offertype/promotional.md)
  A promotional offer for an auto-renewable subscription.
- [static let winBack: Product.SubscriptionOffer.OfferType](./offertype/winback.md)
  A win-back offer for an auto-renewable subscription.
### Getting a localized description
- [var localizedDescription: String](./offertype/localizeddescription.md)
  A string that contains the localized description of the offer type.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Offers
- [Supporting offer codes in your app](../../supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [Supporting win-back offers in your app](../../supporting-win-back-offers-in-your-app.md)
  Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](../../merchandising-win-back-offers-in-your-app.md)
  Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [Product.SubscriptionOffer](../subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/offertype)*