# offerPeriodStringRepresentation

**Framework**: StoreKit  
**Kind**: property

The string representation of the subscription offer period applied to the next billing period.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var offerPeriodStringRepresentation: String? { get }
```

#### Discussion

This value is present only for subscriptions that include an offer.

> ❗ **Important**:  In rare cases, the property might return a sentinel `nil` value. One possible reason is using StoreKit Testing in Xcode; try testing on a device with a newer OS. Another reason could be a critical server error.

## See Also

- [var environmentStringRepresentation: String](product/subscriptioninfo/renewalinfo/environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](product/subscriptioninfo/renewalinfo/offerid.md)
  A string that identifies an offer applied to the next subscription period.
- [var offerType: Transaction.OfferType?](product/subscriptioninfo/renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](product/subscriptioninfo/renewalinfo/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation)*