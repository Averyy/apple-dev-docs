# price

**Framework**: StoreKit  
**Kind**: property

The discount price of the product in the local currency.

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
var price: NSDecimalNumber { get }
```

#### Discussion

Use the [`priceLocale`](skproductdiscount/pricelocale.md) to format the price.

## See Also

- [var priceLocale: Locale](skproductdiscount/pricelocale.md)
  The locale used to format the discount price of the product.
- [var paymentMode: SKProductDiscount.PaymentMode](skproductdiscount/paymentmode-swift.property.md)
  The payment mode for this product discount.
- [SKProductDiscount.PaymentMode](skproductdiscount/paymentmode-swift.enum.md)
  Values representing the payment modes for a product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/price)*