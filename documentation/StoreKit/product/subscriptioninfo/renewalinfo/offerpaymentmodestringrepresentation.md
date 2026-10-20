# offerPaymentModeStringRepresentation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: offer.paymentMode.rawValue)
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: offer.paymentMode.rawValue)
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: offer.paymentMode.rawValue)
- macOS 12.0+ - Deprecated in 15.0 (renamed: offer.paymentMode.rawValue)
- tvOS 15.0+ - Deprecated in 18.0 (renamed: offer.paymentMode.rawValue)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: offer.paymentMode.rawValue)
- watchOS 8.0+ - Deprecated in 11.0 (renamed: offer.paymentMode.rawValue)

> **Deprecated**: Use the offer property instead.

## Declaration

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

### Deprecated
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](./offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](./offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation)*