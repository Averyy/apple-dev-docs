# price

**Framework**: StoreKit  
**Kind**: property

The cost of the product in the local currency.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var price: NSDecimalNumber { get }
```

#### Discussion

Your app can format the price using a number formatter, as shown in the following sample code:

## See Also

- [var priceLocale: Locale](skproduct/pricelocale.md)
  The locale used to format the price of the product.
- [var introductoryPrice: SKProductDiscount?](skproduct/introductoryprice.md)
  The object containing introductory price information for the product.
- [var discounts: [SKProductDiscount]](skproduct/discounts.md)
  An array of subscription offers available for the auto-renewable subscription.
- [class SKProductDiscount](skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/price)*