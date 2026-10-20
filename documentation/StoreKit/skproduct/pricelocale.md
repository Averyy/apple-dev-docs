# priceLocale

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The locale used to format the price of the product.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.displayPrice.

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

### Getting Pricing Information
- [var price: NSDecimalNumber](./price.md)
  The cost of the product in the local currency.
- [var introductoryPrice: SKProductDiscount?](./introductoryprice.md)
  The object containing introductory price information for the product.
- [var discounts: [SKProductDiscount]](./discounts.md)
  An array of subscription offers available for the auto-renewable subscription.
- [class SKProductDiscount](../skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/pricelocale)*