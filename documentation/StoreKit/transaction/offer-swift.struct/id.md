# id

**Framework**: StoreKit  
**Kind**: property

A string that identifies the subscription offer that applies to the transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
let id: String?
```

#### Discussion

The [`id`](transaction/offer-swift.struct/id.md) is the offer identifier that you provide when you set up a subscription offer in App Store Connect.

This value is `nil` if the subscription offer is an [`introductory`](transaction/offertype-swift.struct/introductory.md) offer.

If the offer type is [`code`](transaction/offertype-swift.struct/code.md), the [`id`](transaction/offer-swift.struct/id.md) value contains the reference name of the offer code you set up in App Store Connect.  For more information, see [`Set up offer codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

- [let type: Transaction.OfferType](transaction/offer-swift.struct/type.md)
  The type of subscription offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.
- [let paymentMode: Transaction.Offer.PaymentMode?](transaction/offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for subscription offers that apply to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/id)*