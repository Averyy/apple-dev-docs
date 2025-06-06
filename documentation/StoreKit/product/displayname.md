# displayName

**Framework**: Storekit  
**Kind**: property

The localized display name of the product, if it exists.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let displayName: String
```

#### Discussion

The storefront of the device determines the language of the display name, not the preferred language set on the device. For more information, see [`Storefront`](storefront.md).

> **Note**:  When you create a new product in App Store Connect or in a StoreKit configuration file, you can test it before you add a product localization. The [`displayName`](product/displayname.md) value is an empty string until you add a localization. For more information on localizations, see [`Add and remove localizations`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information#add-and-remove-localizations).

## See Also

- [let description: String](product/description.md)
  The localized description of the product.
- [let displayPrice: String](product/displayprice.md)
  The localized string representation of the product price, suitable for display.
- [let price: Decimal](product/price.md)
  The decimal representation of the cost of the product, in local currency.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](product/priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](product/subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](product/subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/displayname)*