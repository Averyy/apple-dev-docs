# SKProductDiscount.PaymentMode.payAsYouGo

**Framework**: StoreKit  
**Kind**: case

A constant that indicates a product discount that applies over a single billing period or multiple billing periods.

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
case payAsYouGo
```

## Mentions

- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md)

#### Discussion

With a pay as you go payment mode, users pay the discounted price at each billing period during the discount period.

![Example of a subscription timeline with a pay as you go payment mode. The  introductory price is billed three times.](https://docs-assets.developer.apple.com/published/cdf7424c589eb68fe7962e3c551ebba1/media-2942132%402x.png)

## See Also

- [SKProductDiscount.PaymentMode.payUpFront](skproductdiscount/paymentmode-swift.enum/payupfront.md)
  A constant that indicates that the system applies the product discount up front.
- [SKProductDiscount.PaymentMode.freeTrial](skproductdiscount/paymentmode-swift.enum/freetrial.md)
  A constant that indicates that the payment mode is a free trial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum/payasyougo)*