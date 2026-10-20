# environmentStringRepresentation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string representation of the server environment.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 12.0+ - Deprecated in 13.0
- tvOS 15.0+ - Deprecated in 16.0
- watchOS 8.0+ - Deprecated in 9.0

> **Deprecated**: Use [`environment`](./environment.md) instead.

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var environmentStringRepresentation: String { get }
```

## See Also

### Deprecated
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](./offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](./reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](./storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/environmentstringrepresentation)*