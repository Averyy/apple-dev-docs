# currencyCode

**Framework**: StoreKit  
**Kind**: property

The three-letter ISO 4217 currency code for the price of the product.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
var currencyCode: String? { get }
```

#### Discussion

The [`currencyCode`](transaction/currencycode.md) property contains an ISO 4217 alpha-3 string that represents the currency of the price of the product. Use [`currencyCode`](product/subscriptioninfo/renewalinfo/currencycode.md) to access the currency of the price on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9. Otherwise, use [`currency`](product/subscriptioninfo/renewalinfo/currency.md).

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [`currencyCode`](transaction/currencycode.md) to infer the storefront. Use the [`storefront`](transaction/storefront.md) value in the transaction instead.

For more information on how you set prices, see [`Set a price for an in-app purchase`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [var environmentStringRepresentation: String](transaction/environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](transaction/offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerPaymentModeStringRepresentation: String?](transaction/offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](transaction/offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](transaction/reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](transaction/storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currencycode)*