# payAsYouGo

**Framework**: StoreKit  
**Kind**: property

A payment mode of a product discount that applies over a single billing period or multiple billing periods.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
static let payAsYouGo: Transaction.Offer.PaymentMode
```

#### Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each billing period for the duration of the discount.

![A timeline titled Pay As You Go that’s divided into four sections. The first three sections, labeled Introductory price, each have an equal timespan, and the fourth section, labeled Regular price has a different timespan. The first three sections represent the initial purchase, first renewal, and second renewal, respectively.  The fourth section is the third renewal, at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/a6962b6c59fca2500367c1d792f2ec46/media-4311727%402x.png)

## See Also

- [static let freeTrial: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial.
- [static let payUpFront: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo)*