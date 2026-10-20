# offerPaymentModeStringRepresentation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The string representation of the payment mode for a subscription offer.

**Availability**:
- iOS 15.0+ - Deprecated in 17.2 (renamed: offer.paymentMode.rawValue)
- iPadOS 15.0+ - Deprecated in 17.2 (renamed: offer.paymentMode.rawValue)
- Mac Catalyst 15.0+ - Deprecated in 17.2 (renamed: offer.paymentMode.rawValue)
- macOS 12.0+ - Deprecated in 14.2 (renamed: offer.paymentMode.rawValue)
- tvOS 15.0+ - Deprecated in 17.2 (renamed: offer.paymentMode.rawValue)
- visionOS 1.0+ - Deprecated in 1.1 (renamed: offer.paymentMode.rawValue)
- watchOS 8.0+ - Deprecated in 10.2 (renamed: offer.paymentMode.rawValue)

> **Deprecated**: Use `paymentMode` instead.

## Declaration

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

### Deprecated
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerType: Transaction.OfferType?](./offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](./reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](./storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offerpaymentmodestringrepresentation)*