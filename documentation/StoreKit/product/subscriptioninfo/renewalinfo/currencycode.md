# currencyCode

**Framework**: StoreKit  
**Kind**: property

The three-letter ISO 4217 currency code for the price of the product.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
var currencyCode: String? { get }
```

#### Discussion

Use [`currencyCode`](product/subscriptioninfo/renewalinfo/currencycode.md) to access the currency of the price on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9. Otherwise, use [`currency`](product/subscriptioninfo/renewalinfo/currency.md).

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [`currencyCode`](transaction/currencycode.md) to infer the storefront. Use the [`storefront`](transaction/storefront.md) value in the transaction instead.

For more information on how you set prices, see [`Set a price for an in-app purchase`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [var environmentStringRepresentation: String](product/subscriptioninfo/renewalinfo/environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](product/subscriptioninfo/renewalinfo/offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](product/subscriptioninfo/renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var offerPaymentModeStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/currencycode)*