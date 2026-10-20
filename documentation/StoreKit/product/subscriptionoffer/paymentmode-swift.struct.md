# Product.SubscriptionOffer.PaymentMode

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The payment modes for subscription offers that apply to a transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct PaymentMode
```

## Mentions

- [Testing win-back offers in Xcode](../../testing-win-back-offers-in-xcode.md)

#### Overview

A payment mode describes how a subscription offer charges its discounted price — whether it charges one time, charges multiple times, or charges nothing because it’s a free trial.

## Topics

### Getting the payment modes
- [static let freeTrial: Product.SubscriptionOffer.PaymentMode](./paymentmode-swift.struct/freetrial.md)
  A payment mode of a product discount that indicates a free trial offer.
- [static let payAsYouGo: Product.SubscriptionOffer.PaymentMode](./paymentmode-swift.struct/payasyougo.md)
  A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [static let payUpFront: Product.SubscriptionOffer.PaymentMode](./paymentmode-swift.struct/payupfront.md)
  A payment mode of a product discount that applies the discount up front.
### Getting a localized description
- [var localizedDescription: String](./paymentmode-swift.struct/localizeddescription.md)
  The localized text that describes the payment mode.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting price information
- [let displayPrice: String](./displayprice.md)
  The localized string representation of the discounted price of the subscription offer.
- [let price: Decimal](./price.md)
  The decimal representation of the discounted price of the subscription offer.
- [let paymentMode: Product.SubscriptionOffer.PaymentMode](./paymentmode-swift.property.md)
  The offer’s payment mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct)*