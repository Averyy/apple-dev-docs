# offerPaymentModeStringRepresentation

**Framework**: StoreKit  
**Kind**: property

The string representation of the payment mode for a subscription offer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

- [var currencyCode: String?](transaction/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](transaction/environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](transaction/offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerType: Transaction.OfferType?](transaction/offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](transaction/reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](transaction/storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offerpaymentmodestringrepresentation)*