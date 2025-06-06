# Product.SubscriptionOffer

**Framework**: StoreKit  
**Kind**: struct

Information about a subscription offer that you configure in App Store Connect.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SubscriptionOffer
```

## Mentions

- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

#### Overview

You set up subscription offers, such as introductory offers and win-back offers, in App Store Connect.

For more information about subscription offers, see [`Providing subscription offers`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#providing-subscription-offers). For information about configuring the various types of subscription offers in App Store Connect, see:

- [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [`Set up introductory offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [`Set up win-back offers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## Topics

### Getting the subscription offer identifier
- [let id: String?](product/subscriptionoffer/id.md)
  The subscription offer identifier.
### Getting the subscription offer type
- [let type: Product.SubscriptionOffer.OfferType](product/subscriptionoffer/type.md)
  The type of subscription offer, which can be introductory, promotional, or win-back.
- [Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype.md)
  The types of offers for auto-renewable subscriptions.
### Getting price information
- [let displayPrice: String](product/subscriptionoffer/displayprice.md)
  The localized string representation of the discounted price of the subscription offer.
- [let price: Decimal](product/subscriptionoffer/price.md)
  The decimal representation of the discounted price of the subscription offer.
- [let paymentMode: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.property.md)
  The offer’s payment mode.
- [Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct.md)
  The payment modes for subscription offers that apply to a transaction.
### Getting the subscription duration
- [let period: Product.SubscriptionPeriod](product/subscriptionoffer/period.md)
  The subscription period for the subscription offer.
- [let periodCount: Int](product/subscriptionoffer/periodcount.md)
  The number of periods that the subscription offer renews for.
### Creating a subscription offer signature
- [Product.SubscriptionOffer.Signature](product/subscriptionoffer/signature.md)
  A cryptographic signature for a promotional offer.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
  Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
  Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
  Provide subscription service for customers who redeem offer codes through the App Store or within your app.
- [Product.SubscriptionOffer.OfferType](product/subscriptionoffer/offertype.md)
  The types of offers for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer)*