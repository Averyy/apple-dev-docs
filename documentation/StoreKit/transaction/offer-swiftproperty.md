# offer

**Framework**: StoreKit  
**Kind**: property

The offer that applies to the transaction, including its offer type, payment mode, and ID.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
let offer: Transaction.Offer?
```

## Mentions

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

#### Discussion

This value is `nil` if the transaction doesn’t include an offer.

You set up offers for auto-renewable subscriptions and other In-App Purchase product types in App Store Connect. If a customer redeems an offer, this property contains the offer details, including its [`type`](transaction/offer-swift.struct/type.md), [`paymentMode`](transaction/offer-swift.struct/paymentmode-swift.property.md), and [`id`](transaction/id.md). For more information, see [`Transaction.Offer`](transaction/offer-swift.struct.md).

## See Also

- [Transaction.Offer](transaction/offer-swift.struct.md)
  Discounts or promotions that apply to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.property)*