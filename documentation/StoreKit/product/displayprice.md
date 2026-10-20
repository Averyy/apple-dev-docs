# displayPrice

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The localized string representation of the product price, suitable for display.

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
let displayPrice: String
```

#### Discussion

Use this string to display the price, formatted for the locale. The storefront that the user’s device is connected to determines the locale. For more information, see [`Storefront`](../storefront.md).

To perform arithmetic calculations with the price, use the [`price`](./price.md) property instead.

## See Also

### Displaying a product description and price
- [let displayName: String](./displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](./description.md)
  The localized description of the product.
- [let price: Decimal](./price.md)
  The decimal representation of the cost of the product, in local currency.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](./priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](./subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](./subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/displayprice)*