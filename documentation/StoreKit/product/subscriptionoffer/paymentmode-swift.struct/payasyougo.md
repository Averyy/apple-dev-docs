# payAsYouGo

**Framework**: StoreKit  
**Kind**: property

A payment mode of a product discount that applies over a single billing period or multiple billing periods.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let payAsYouGo: Product.SubscriptionOffer.PaymentMode
```

#### Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each billing period for the duration of the discount.

![A timeline titled Pay As You Go that’s divided into four sections. The first three sections, labeled Introductory price, each have an equal timespan, and the fourth section, labeled Regular price has a different timespan. The first three sections represent the initial purchase, first renewal, and second renewal, respectively.  The fourth section is the third renewal, at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/a6962b6c59fca2500367c1d792f2ec46/media-4311775%402x.png)

## See Also

- [static let freeTrial: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial offer.
- [static let payUpFront: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/payasyougo)*