# subscriptionPeriodFormatStyle

**Framework**: StoreKit  
**Kind**: property

The format style for the date components related to a subscription’s duration.

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
var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle { get }
```

#### Discussion

Use this format style to format text that describes a subscription period, including its length and unit, such as “1 week”, “2 months”, and so on. Use this style with the [`formatted(_:referenceDate:)`](product/subscriptionperiod/formatted(_:referencedate:)-3t7wd.md) method on [`Product.SubscriptionPeriod`](product/subscriptionperiod.md) to format the subscription period for the App Store locale.

> **Note**:  When using [`subscriptionPeriodFormatStyle`](product/subscriptionperiodformatstyle.md) on systems earlier than iOS 16, macOS 13, tvOS 16, and watchOS 9, the property may return a format style with a sentinel locale identifier of `“xx_XX”` in uncommon cases, including if the server has an error, or while testing your app using StoreKit Testing in Xcode. For StoreKit testing, use a later OS version.

## See Also

- [let displayName: String](product/displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](product/description.md)
  The localized description of the product.
- [let displayPrice: String](product/displayprice.md)
  The localized string representation of the product price, suitable for display.
- [let price: Decimal](product/price.md)
  The decimal representation of the cost of the product, in local currency.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](product/priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](product/subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiodformatstyle)*