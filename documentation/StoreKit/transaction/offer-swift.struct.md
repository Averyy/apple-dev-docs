# Transaction.Offer

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Discounts or promotions that apply to a transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
struct Offer
```

#### Overview

You set up offers for auto-renewable subscriptions and other Apple In-App Purchase types in App Store Connect. If a customer redeems an offer, it appears in the [`offer`](./offer-swift.property.md) property of the transaction. For auto-renewable subscriptions, if the offer applies to one or more renewal periods, it also appears in the [`offer`](../product/subscriptioninfo/renewalinfo/offer.md) property of [`Product.SubscriptionInfo.RenewalInfo`](../product/subscriptioninfo/renewalinfo.md).

For more information on configuring the various offers in App Store Connect, see:

- [Create offer codes for Apple In-App Purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases)
- [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).
- [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [Set up introductory offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [Set up win-back offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## Topics

### Getting offer details
- [let id: String?](./offer-swift.struct/id.md)
  A string that identifies an offer that applies to the transaction.
- [let type: Transaction.OfferType](./offer-swift.struct/type.md)
  The type of offer that applies to the transaction.
- [Transaction.OfferType](./offertype-swift.struct.md)
  The types of offers that apply to a transaction.
- [let paymentMode: Transaction.Offer.PaymentMode?](./offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [Transaction.Offer.PaymentMode](./offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for offers that apply to a transaction.
- [let period: Product.SubscriptionPeriod?](./offer-swift.struct/period.md)
  The duration of the offer applied to a transaction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting offers
- [let offer: Transaction.Offer?](../product/subscriptioninfo/renewalinfo/offer.md)
  A subscription offer that applies to the transaction at the next renewal period.
- [let eligibleWinBackOfferIDs: [String]](../product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md)
  An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct)*