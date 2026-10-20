# environmentStringRepresentation

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The string representation of the server environment that signs the renewal information for an auto-renewable subscription.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 12.0+ - Deprecated in 13.0
- tvOS 15.0+ - Deprecated in 16.0
- watchOS 8.0+ - Deprecated in 9.0

> **Deprecated**: Use the environment property instead.

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var environmentStringRepresentation: String { get }
```

## See Also

### Deprecated
- [var offerID: String?](./offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](./offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/environmentstringrepresentation)*