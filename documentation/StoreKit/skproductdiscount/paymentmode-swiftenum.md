# SKProductDiscount.PaymentMode

**Framework**: StoreKit  
**Kind**: enum

Values representing the payment modes for a product discount.

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
enum PaymentMode
```

## Mentions

- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md)

#### Overview

The payment mode indicates if the discount price is charged one time, multiple times, or if the discount is a free trial.

The payment mode may determine the wording you choose to phrase the offer in your app’s UI.

## Topics

### Discount Price Payment Modes
- [SKProductDiscount.PaymentMode.payAsYouGo](skproductdiscount/paymentmode-swift.enum/payasyougo.md)
  A constant that indicates a product discount that applies over a single billing period or multiple billing periods.
- [SKProductDiscount.PaymentMode.payUpFront](skproductdiscount/paymentmode-swift.enum/payupfront.md)
  A constant that indicates that the system applies the product discount up front.
- [SKProductDiscount.PaymentMode.freeTrial](skproductdiscount/paymentmode-swift.enum/freetrial.md)
  A constant that indicates that the payment mode is a free trial.
### Initializers
- [init?(rawValue: UInt)](skproductdiscount/paymentmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var price: NSDecimalNumber](skproductdiscount/price.md)
  The discount price of the product in the local currency.
- [var priceLocale: Locale](skproductdiscount/pricelocale.md)
  The locale used to format the discount price of the product.
- [var paymentMode: SKProductDiscount.PaymentMode](skproductdiscount/paymentmode-swift.property.md)
  The payment mode for this product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum)*