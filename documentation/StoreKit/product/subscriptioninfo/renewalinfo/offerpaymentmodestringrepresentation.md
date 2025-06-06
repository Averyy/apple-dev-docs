# offerPaymentModeStringRepresentation

**Framework**: StoreKit  
**Kind**: property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

- [var environmentStringRepresentation: String](product/subscriptioninfo/renewalinfo/environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](product/subscriptioninfo/renewalinfo/offerid.md)
  A string that identifies an offer applied to the next subscription period.
- [var offerType: Transaction.OfferType?](product/subscriptioninfo/renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](product/subscriptioninfo/renewalinfo/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPeriodStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation)*