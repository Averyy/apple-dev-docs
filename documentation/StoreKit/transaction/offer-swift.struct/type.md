# type

**Framework**: StoreKit  
**Kind**: property

The type of subscription offer that applies to the transaction.

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

#### Discussion

See [`Transaction.OfferType`](transaction/offertype-swift.struct.md) for the complete list of subscription offer types.

For more information about introductory offers, see [`Set an introductory offer for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions).

For more information about promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

For more information about offer codes, see [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

## See Also

- [let id: String?](transaction/offer-swift.struct/id.md)
  A string that identifies the subscription offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.
- [let paymentMode: Transaction.Offer.PaymentMode?](transaction/offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for subscription offers that apply to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/type)*