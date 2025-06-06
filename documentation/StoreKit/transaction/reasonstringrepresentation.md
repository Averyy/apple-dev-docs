# reasonStringRepresentation

**Framework**: StoreKit  
**Kind**: property

The string representation of the transaction reason.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
var reasonStringRepresentation: String { get }
```

#### Discussion

For more information, see [`reason`](transaction/reason-swift.property.md).

## See Also

- [var currencyCode: String?](transaction/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](transaction/environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](transaction/offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerPaymentModeStringRepresentation: String?](transaction/offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](transaction/offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var storefrontCountryCode: String](transaction/storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/reasonstringrepresentation)*