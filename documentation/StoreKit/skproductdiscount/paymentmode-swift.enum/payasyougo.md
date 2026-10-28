# SKProductDiscount.PaymentMode.payAsYouGo

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A constant that indicates a product discount that applies over a single billing period or multiple billing periods.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.PaymentMode.

## Declaration

```swift
case payAsYouGo
```

```c
SKProductDiscountPaymentModePayAsYouGo
```

## Mentions

- [Implementing introductory offers in your app](../../implementing-introductory-offers-in-your-app.md)

## Discussion

With a pay as you go payment mode, users pay the discounted price at each billing period during the discount period.

![Example of a subscription timeline with a pay as you go payment mode. The  introductory price is billed three times.](https://developer.apple.com/tutorials/images/com.apple.storekit/media-2942132@2x.png)

## See Also

### Discount Price Payment Modes
- [SKProductDiscount.PaymentMode.payUpFront](./payupfront.md)
  A constant that indicates that the system applies the product discount up front.
- [SKProductDiscount.PaymentMode.freeTrial](./freetrial.md)
  A constant that indicates that the payment mode is a free trial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payasyougo)*