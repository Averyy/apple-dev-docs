# SKProductDiscount.PaymentMode.freeTrial

**Framework**: StoreKit  
**Kind**: case

A constant that indicates that the payment mode is a free trial.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case freeTrial
```

## Mentions

- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md)

#### Discussion

With a free trial payment mode, the price is 0, so users pay nothing during the discount period.

![Example of a subscription timeline starting with a free trial. After the free introductory period, the subscription renews at regular price. ](https://docs-assets.developer.apple.com/published/0ee556ad1cee3517fb03233a341235b3/media-2942195%402x.png)

## See Also

- [SKProductDiscount.PaymentMode.payAsYouGo](skproductdiscount/paymentmode-swift.enum/payasyougo.md)
  A constant that indicates a product discount that applies over a single billing period or multiple billing periods.
- [SKProductDiscount.PaymentMode.payUpFront](skproductdiscount/paymentmode-swift.enum/payupfront.md)
  A constant that indicates that the system applies the product discount up front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/freetrial)*