# SKProductDiscount.PaymentMode

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values representing the payment modes for a product discount.

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
enum PaymentMode
```

```c
enum SKProductDiscountPaymentMode : NSUInteger;
```

## Mentions

- [Implementing introductory offers in your app](../implementing-introductory-offers-in-your-app.md)

#### Overview

The payment mode indicates if the discount price is charged one time, multiple times, or if the discount is a free trial.

The payment mode may determine the wording you choose to phrase the offer in your app’s UI.

## Topics

### Discount Price Payment Modes
- [SKProductDiscount.PaymentMode.payAsYouGo](./paymentmode-swift.enum/payasyougo.md)
  A constant that indicates a product discount that applies over a single billing period or multiple billing periods.
- [SKProductDiscount.PaymentMode.payUpFront](./paymentmode-swift.enum/payupfront.md)
  A constant that indicates that the system applies the product discount up front.
- [SKProductDiscount.PaymentMode.freeTrial](./paymentmode-swift.enum/freetrial.md)
  A constant that indicates that the payment mode is a free trial.
### Initializers
- [init?(rawValue: UInt)](./paymentmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Price and Payment Mode
- [var price: NSDecimalNumber](./price.md)
  The discount price of the product in the local currency.
- [var priceLocale: Locale](./pricelocale.md)
  The locale used to format the discount price of the product.
- [var paymentMode: SKProductDiscount.PaymentMode](./paymentmode-swift.property.md)
  The payment mode for this product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum)*