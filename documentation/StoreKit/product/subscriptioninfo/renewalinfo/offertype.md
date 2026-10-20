# offerType

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The subscription offer type for the next subscription period.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: offer.type)
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: offer.type)
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: offer.type)
- macOS 12.0+ - Deprecated in 15.0 (renamed: offer.type)
- tvOS 15.0+ - Deprecated in 18.0 (renamed: offer.type)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: offer.type)
- watchOS 8.0+ - Deprecated in 11.0 (renamed: offer.type)

> **Deprecated**: Use the offer property instead.

## Declaration

```swift
var offerType: Transaction.OfferType? { get }
```

#### Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Deprecated
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offertype)*