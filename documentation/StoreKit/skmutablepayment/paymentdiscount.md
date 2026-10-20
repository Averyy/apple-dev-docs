# paymentDiscount

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The details of the discount offer to apply to the payment.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
@NSCopying
var paymentDiscount: SKPaymentDiscount? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) SKPaymentDiscount * paymentDiscount;
```

## Mentions

- [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment/paymentdiscount)*