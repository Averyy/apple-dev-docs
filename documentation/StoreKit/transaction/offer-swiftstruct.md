# Transaction.Offer

**Framework**: StoreKit  
**Kind**: struct

The subscription offers that apply to a transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
struct Offer
```

#### Overview

You set up subscription offers for auto-renewable subscriptions in App Store Connect. If a customer redeems an offer, it appears in the [`offer`](transaction/offer-swift.property.md) property of the transaction. If the offer applies to one or more renewal periods, it also appears in the [`offer`](product/subscriptioninfo/renewalinfo/offer.md) property of [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md).

For more information about subscription offers, see [`Providing subscription offers`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#providing-subscription-offers). For information about configuring the various subscription offers in App Store Connect, see:

- [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [`Set up introductory offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [`Set up win-back offers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## Topics

### Getting offer details
- [let id: String?](transaction/offer-swift.struct/id.md)
  A string that identifies the subscription offer that applies to the transaction.
- [let type: Transaction.OfferType](transaction/offer-swift.struct/type.md)
  The type of subscription offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.
- [let paymentMode: Transaction.Offer.PaymentMode?](transaction/offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for subscription offers that apply to a transaction.
### Instance Properties
- [let period: Product.SubscriptionPeriod?](transaction/offer-swift.struct/period.md)
  The duration of the offer applied to a transaction.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let offer: Transaction.Offer?](product/subscriptioninfo/renewalinfo/offer.md)
  A subscription offer that applies to the transaction at the next renewal period.
- [let eligibleWinBackOfferIDs: [String]](product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md)
  An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct)*