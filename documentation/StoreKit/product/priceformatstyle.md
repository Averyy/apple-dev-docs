# priceFormatStyle

**Framework**: Storekit  
**Kind**: property

The format style for the numbers in the price of the product.

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
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var priceFormatStyle: Decimal.FormatStyle.Currency { get }
```

#### Discussion

The [`priceFormatStyle`](product/priceformatstyle.md) value is a localized number suitable for display. Use this value for localizing numbers derived from the [`price`](product/price.md) property, such as to calculate the price of two products as `$(`price * 2`)`.

To display the [`price`](product/price.md) directly, rather than making calculations, use the [`displayPrice`](product/displayprice.md) string instead.

> **Note**:  When using [`priceFormatStyle`](product/priceformatstyle.md) on systems earlier than iOS 16, macOS 13, tvOS 16, and watchOS 9, the property may return a format style with a sentinel locale identifier of `“xx_XX”` in uncommon cases, including if the server has an error, or while testing your app using StoreKit Testing in Xcode. For StoreKit testing, use a later OS version.

## See Also

- [let displayName: String](product/displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](product/description.md)
  The localized description of the product.
- [let displayPrice: String](product/displayprice.md)
  The localized string representation of the product price, suitable for display.
- [let price: Decimal](product/price.md)
  The decimal representation of the cost of the product, in local currency.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](product/subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](product/subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/priceformatstyle)*