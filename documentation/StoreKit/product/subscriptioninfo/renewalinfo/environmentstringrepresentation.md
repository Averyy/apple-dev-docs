# environmentStringRepresentation

**Framework**: StoreKit  
**Kind**: property

The string representation of the server environment that signs the renewal information for an auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var environmentStringRepresentation: String { get }
```

## See Also

- [var offerID: String?](product/subscriptioninfo/renewalinfo/offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](product/subscriptioninfo/renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](product/subscriptioninfo/renewalinfo/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/environmentstringrepresentation)*