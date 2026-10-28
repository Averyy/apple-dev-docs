# price

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The decimal representation of the cost of the product, in local currency.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let price: Decimal
```

## Discussion

Use this property to perform arithmetic calculations with the price of the product. For a localized string representation of the price to display to customers, use the [`displayPrice`](./displayprice.md) property instead.

## See Also

### Displaying a product description and price
- [let displayName: String](./displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](./description.md)
  The localized description of the product.
- [let displayPrice: String](./displayprice.md)
  The localized string representation of the product price, suitable for display.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](./priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](./subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](./subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/price)*