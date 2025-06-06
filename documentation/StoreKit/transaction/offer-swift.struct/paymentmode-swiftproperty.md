# paymentMode

**Framework**: StoreKit  
**Kind**: property

The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
let paymentMode: Transaction.Offer.PaymentMode?
```

#### Discussion

You set up subscription offers and determine the payment mode when you configure subscriptions in App Store Connect. For more information about the Free Trial ([`freeTrial`](transaction/offer-swift.struct/paymentmode-swift.struct/freetrial.md)), Pay As You Go ([`payAsYouGo`](transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo.md)), and Pay Up Front ([`payUpFront`](transaction/offer-swift.struct/paymentmode-swift.struct/payupfront.md)) payment modes, see [`Pricing and availability`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

## See Also

- [let id: String?](transaction/offer-swift.struct/id.md)
  A string that identifies the subscription offer that applies to the transaction.
- [let type: Transaction.OfferType](transaction/offer-swift.struct/type.md)
  The type of subscription offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.
- [Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct.md)
  The payment modes for subscription offers that apply to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.property)*