# price

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The discount price of the product in the local currency.

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
var price: NSDecimalNumber { get }
```

```objc
@property (nonatomic, readonly) NSDecimalNumber * price;
```

## Discussion

Use the [`priceLocale`](./pricelocale.md) to format the price.

## See Also

### Getting Price and Payment Mode
- [var priceLocale: Locale](./pricelocale.md)
  The locale used to format the discount price of the product.
- [var paymentMode: SKProductDiscount.PaymentMode](./paymentmode-swift.property.md)
  The payment mode for this product discount.
- [SKProductDiscount.PaymentMode](./paymentmode-swift.enum.md)
  Values representing the payment modes for a product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/price)*