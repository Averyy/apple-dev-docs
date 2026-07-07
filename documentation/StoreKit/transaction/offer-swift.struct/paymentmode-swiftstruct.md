# Transaction.Offer.PaymentMode

**Framework**: StoreKit  
**Kind**: struct

The payment modes for offers that apply to a transaction.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
struct PaymentMode
```

#### Overview

If your app supports offers and the customer redeems an offer, the transaction contains the information in the [`offer`](transaction/offer-swift.property.md) parameter. The payment modes include the subscription payment modes as in the [`Product.SubscriptionOffer.PaymentMode`](product/subscriptionoffer/paymentmode-swift.struct.md) structure, and the [`oneTime`](transaction/offer-swift.struct/paymentmode-swift.struct/onetime.md) mode that applies to consumables, non-consumables, and non-renewing subscriptions.

The following images describe payment modes for auto-renewable subscriptions.

![A timeline titled “Free Trial” that is divided into three sections. The first section, which has a different timespan than the remaining sections, starts with the initial purchase and is the free trial period. The second section is labeled “first renewal”, and is at the regular price. The third section is labeled  “second renewal”, and is also at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/31535a5905cc81be4d4fa37a8089ea5f/media-4311732%402x.png)

![A timeline titled “Pay As You Go” that is divided into four sections. The first three sections, labeled “Introductory price” each have equal timespan, and the fourth section, labeled “Regular price” has a different timespan. The first three sections represent the initial purchase, first renewal, and second renewal, respectively.  The fourth section is the third renewal, at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/a6962b6c59fca2500367c1d792f2ec46/media-4311730%402x.png)

![A timeline titled “Pay Up Front” that is divided into three sections. The first section, labeled “Introductory price” has a different timespan than the following sections, labelled “Regular price”. The timeline starts with the initial purchase at the introductory price, followed by the first renewal and second renewals, both at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.](https://docs-assets.developer.apple.com/published/2067b05f759a211be51d6b062b2aa00c/media-4311731%402x.png)

For more information about payment modes, see [`In-app purchase and subscriptions pricing and availability`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-and-subscriptions-pricing-and-availability).

## Topics

### Getting payment modes
- [static let freeTrial: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial.
- [static let payAsYouGo: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [static let payUpFront: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.
- [static var oneTime: Transaction.Offer.PaymentMode](transaction/offer-swift.struct/paymentmode-swift.struct/onetime.md)
  A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let id: String?](transaction/offer-swift.struct/id.md)
  A string that identifies an offer that applies to the transaction.
- [let type: Transaction.OfferType](transaction/offer-swift.struct/type.md)
  The type of offer that applies to the transaction.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of offers that apply to a transaction.
- [let paymentMode: Transaction.Offer.PaymentMode?](transaction/offer-swift.struct/paymentmode-swift.property.md)
  The payment mode for a subscription offer on an auto-renewable subscription that applies to the transaction.
- [let period: Product.SubscriptionPeriod?](transaction/offer-swift.struct/period.md)
  The duration of the offer applied to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct)*