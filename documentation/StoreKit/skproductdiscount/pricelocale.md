# priceLocale

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The locale used to format the discount price of the product.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.displayPrice.

## Declaration

```swift
var priceLocale: Locale { get }
```

```objc
@property (nonatomic, readonly) NSLocale * priceLocale;
```

#### Discussion

Use the locale to format the [`price`](./price.md).

## See Also

### Getting Price and Payment Mode
- [var price: NSDecimalNumber](./price.md)
  The discount price of the product in the local currency.
- [var paymentMode: SKProductDiscount.PaymentMode](./paymentmode-swift.property.md)
  The payment mode for this product discount.
- [SKProductDiscount.PaymentMode](./paymentmode-swift.enum.md)
  Values representing the payment modes for a product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/pricelocale)*