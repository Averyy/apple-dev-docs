# type

**Framework**: StoreKit  
**Kind**: property

The type of offer that applies to the transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
let type: Transaction.OfferType
```

## Mentions

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)

#### Discussion

See [`Transaction.OfferType`](transaction/offertype-swift.struct.md) for the complete list of offer types.

For more information about introductory offers, see [`Set an introductory offer for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions).

For more information about promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

For more information about offer codes, see [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

## See Also

- [let id: String?](transaction/offer-swift.struct/id.md)
  A string that identifies an offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of offers that apply to a transaction.
- [let paymentMode: Transaction.Offer.PaymentMode?](transaction/offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for offers that apply to a transaction.
- [let period: Product.SubscriptionPeriod?](transaction/offer-swift.struct/period.md)
  The duration of the offer applied to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/type)*