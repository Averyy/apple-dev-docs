# freeTrial

**Framework**: StoreKit  
**Kind**: property

A payment mode of a product discount that indicates a free trial offer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let freeTrial: Product.SubscriptionOffer.PaymentMode
```

#### Discussion

With a Free trial payment mode, customers pay nothing during the discount period.

![A timeline titled Free Trial that’s divided into three sections. The first section, which has a different timespan than the remaining sections, starts with the initial purchase and is the free trial period. The second section is labeled first renewal, and is at the regular price. The third section is labeled  second renewal, and is also at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/31535a5905cc81be4d4fa37a8089ea5f/media-4311774%402x.png)

## See Also

- [static let payAsYouGo: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [static let payUpFront: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/freetrial)*