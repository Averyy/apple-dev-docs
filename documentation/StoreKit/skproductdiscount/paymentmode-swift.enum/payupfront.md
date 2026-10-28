# SKProductDiscount.PaymentMode.payUpFront

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A constant that indicates that the system applies the product discount up front.

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
case payUpFront
```

```c
SKProductDiscountPaymentModePayUpFront
```

## Mentions

- [Implementing introductory offers in your app](../../implementing-introductory-offers-in-your-app.md)

## Discussion

With a pay up front payment mode, users pay the discounted price one time, and receive the product for duration of the discount period.

![Example of a subscription timeline with a pay up front payment mode. The introductory price is billed one time.](https://developer.apple.com/tutorials/images/com.apple.storekit/media-2942133@2x.png)

## See Also

### Discount Price Payment Modes
- [SKProductDiscount.PaymentMode.payAsYouGo](./payasyougo.md)
  A constant that indicates a product discount that applies over a single billing period or multiple billing periods.
- [SKProductDiscount.PaymentMode.freeTrial](./freetrial.md)
  A constant that indicates that the payment mode is a free trial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payupfront)*