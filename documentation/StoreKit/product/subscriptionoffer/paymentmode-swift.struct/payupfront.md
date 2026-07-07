# payUpFront

**Framework**: StoreKit  
**Kind**: property

A payment mode of a product discount that applies the discount up front.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let payUpFront: Product.SubscriptionOffer.PaymentMode
```

#### Discussion

With a Pay Up Front payment mode, subscribers pay a one-time discounted price for a specific duration.

![A timeline titled Pay Up Front that’s divided into three sections. The first section, labeled Introductory price has a longer timespan than the following sections which are both labeled Regular price. The timeline starts with the initial purchase at the introductory price, followed by the first and second renewals, both at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/2067b05f759a211be51d6b062b2aa00c/media-4311773%402x.png)

## See Also

- [static let freeTrial: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial offer.
- [static let payAsYouGo: Product.SubscriptionOffer.PaymentMode](product/subscriptionoffer/paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/payupfront)*