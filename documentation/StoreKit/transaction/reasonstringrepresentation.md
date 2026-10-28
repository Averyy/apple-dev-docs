# reasonStringRepresentation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The string representation of the transaction reason.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: Use [`reason`](./reason-swift.property.md) instead.

## Declaration

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
var reasonStringRepresentation: String { get }
```

## Discussion

For more information, see [`reason`](./reason-swift.property.md).

## See Also

### Deprecated
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](./offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var storefrontCountryCode: String](./storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/reasonstringrepresentation)*