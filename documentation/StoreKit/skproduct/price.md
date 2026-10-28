# price

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The cost of the product in the local currency.

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
var price: NSDecimalNumber { get }
```

```objc
@property (nonatomic, readonly) NSDecimalNumber * price;
```

## Discussion

Your app can format the price using a number formatter, as shown in the following sample code:

**Swift**:

```swift
let numberFormatter = NumberFormatter()
numberFormatter.numberStyle = .currency
numberFormatter.locale = product.priceLocale
let formattedString = numberFormatter.string(from: product.price)
```

**Objective-C**:

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setFormatterBehavior:NSNumberFormatterBehavior10_4];
[numberFormatter setNumberStyle:NSNumberFormatterCurrencyStyle];
[numberFormatter setLocale:product.priceLocale];
NSString *formattedString = [numberFormatter stringFromNumber:product.price];
```

## See Also

### Getting Pricing Information
- [var priceLocale: Locale](./pricelocale.md)
  The locale used to format the price of the product.
- [var introductoryPrice: SKProductDiscount?](./introductoryprice.md)
  The object containing introductory price information for the product.
- [var discounts: [SKProductDiscount]](./discounts.md)
  An array of subscription offers available for the auto-renewable subscription.
- [class SKProductDiscount](../skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/price)*