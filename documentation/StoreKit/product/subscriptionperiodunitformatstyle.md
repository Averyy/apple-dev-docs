# subscriptionPeriodUnitFormatStyle

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The format style for subscription period units, such as week, month, or year.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle { get }
```

## See Also

### Displaying a product description and price
- [let displayName: String](./displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](./description.md)
  The localized description of the product.
- [let displayPrice: String](./displayprice.md)
  The localized string representation of the product price, suitable for display.
- [let price: Decimal](./price.md)
  The decimal representation of the cost of the product, in local currency.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](./priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](./subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiodunitformatstyle)*