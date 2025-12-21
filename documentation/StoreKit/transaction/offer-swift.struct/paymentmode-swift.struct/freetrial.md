# freeTrial

**Framework**: StoreKit  
**Kind**: property

A payment mode of a product discount that indicates a free trial.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
static let freeTrial: Transaction.Offer.PaymentMode
```

#### Discussion

With a Free trial payment mode, customers pay nothing during the discount period.

![A timeline titled Free Trial that’s divided into three sections. The first section, which has a different timespan than the remaining sections, starts with the initial purchase and is the free trial period. The second section is labeled first renewal, and is at the regular price. The third section is labeled  second renewal, and is also at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/31535a5905cc81be4d4fa37a8089ea5f/media-4311726%402x.png)

## See Also

- [static let payAsYouGo: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [static let payUpFront: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.
- [static var oneTime: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/onetime.md)
  A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/freetrial)*