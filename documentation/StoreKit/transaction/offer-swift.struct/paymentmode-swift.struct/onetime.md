# oneTime

**Framework**: StoreKit  
**Kind**: property

A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
@backDeployed(before: iOS 26.0, macOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
static var oneTime: Transaction.Offer.PaymentMode { get }
```

## See Also

- [static let freeTrial: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial.
- [static let payAsYouGo: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [static let payUpFront: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/onetime)*