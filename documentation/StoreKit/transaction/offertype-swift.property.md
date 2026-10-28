# offerType

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The subscription offer type for the current subscription period.

**Availability**:
- iOS 15.0+ - Deprecated in 17.2 (renamed: offer.type)
- iPadOS 15.0+ - Deprecated in 17.2 (renamed: offer.type)
- Mac Catalyst 15.0+ - Deprecated in 17.2 (renamed: offer.type)
- macOS 12.0+ - Deprecated in 14.2 (renamed: offer.type)
- tvOS 15.0+ - Deprecated in 17.2 (renamed: offer.type)
- visionOS 1.0+ - Deprecated in 1.1 (renamed: offer.type)
- watchOS 8.0+ - Deprecated in 10.2 (renamed: offer.type)

> **Deprecated**: Use [`offer`](./offer-swift.property.md) instead.

## Declaration

```swift
var offerType: Transaction.OfferType? { get }
```

## Mentions

- [Supporting subscription offer codes in your app](../supporting-subscription-offer-codes-in-your-app.md)
- [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md)

## Discussion

If this value is `nil`, there’s no offer applied.

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
- [var reasonStringRepresentation: String](./reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](./storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offertype-swift.property)*