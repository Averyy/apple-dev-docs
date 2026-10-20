# SKProductDiscount.PaymentMode.freeTrial

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A constant that indicates that the payment mode is a free trial.

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
case freeTrial
```

```c
SKProductDiscountPaymentModeFreeTrial
```

## Mentions

- [Implementing introductory offers in your app](../../implementing-introductory-offers-in-your-app.md)

#### Discussion

With a free trial payment mode, the price is 0, so users pay nothing during the discount period.

![Example of a subscription timeline starting with a free trial. After the free introductory period, the subscription renews at regular price. ](https://developer.apple.com/tutorials/images/com.apple.storekit/media-2942195@2x.png)

## See Also

### Discount Price Payment Modes
- [SKProductDiscount.PaymentMode.payAsYouGo](./payasyougo.md)
  A constant that indicates a product discount that applies over a single billing period or multiple billing periods.
- [SKProductDiscount.PaymentMode.payUpFront](./payupfront.md)
  A constant that indicates that the system applies the product discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/freetrial)*