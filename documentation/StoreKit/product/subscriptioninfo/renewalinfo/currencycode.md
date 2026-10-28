# currencyCode

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The three-letter ISO 4217 currency code for the price of the product.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0 (renamed: currency.identifier)
- iPadOS 15.0+ - Deprecated in 16.0 (renamed: currency.identifier)
- Mac Catalyst 15.0+ - Deprecated in 16.0 (renamed: currency.identifier)
- macOS 12.0+ - Deprecated in 13.0 (renamed: currency.identifier)
- tvOS 15.0+ - Deprecated in 16.0 (renamed: currency.identifier)
- watchOS 8.0+ - Deprecated in 9.0 (renamed: currency.identifier)

> **Deprecated**: Use [`currency`](./currency.md) instead. To get the currency code as a string, use the [`identifier`](../../../../Foundation/locale/currency-swift.struct/identifier.md) property of [`currency`](./currency.md).

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
var currencyCode: String? { get }
```

## Discussion

Use [`currencyCode`](./currencycode.md) to access the currency of the price on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9. Otherwise, use [`currency`](./currency.md).

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [`currencyCode`](../../../transaction/currencycode.md) to infer the storefront. Use the [`storefront`](../../../transaction/storefront.md) value in the transaction instead.

For more information on how you set prices, see [Set a price for an Apple In-App Purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

### Deprecated
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](./offertype.md)
  The subscription offer type for the next subscription period.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/currencycode)*