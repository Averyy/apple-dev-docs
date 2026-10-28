# offerID

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies an offer that applies to the next subscription period.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: offer.id)
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: offer.id)
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: offer.id)
- macOS 12.0+ - Deprecated in 15.0 (renamed: offer.id)
- tvOS 15.0+ - Deprecated in 18.0 (renamed: offer.id)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: offer.id)
- watchOS 8.0+ - Deprecated in 11.0 (renamed: offer.id)

> **Deprecated**: Use the offer property instead.

## Declaration

```swift
var offerID: String? { get }
```

## Mentions

- [Supporting offer codes in your app](../../../supporting-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](../../../supporting-subscription-offer-codes-in-your-app.md)

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is [`introductory`](../../../transaction/offertype-swift.struct/introductory.md).

If the offer type is [`promotional`](../../../transaction/offertype-swift.struct/promotional.md), this value contains the promotional offer identifier you set up in App Store Connect. For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

If the offer type is [`code`](../../../transaction/offertype-swift.struct/code.md), this value contains the reference name of the offer code you set up in App Store Connect. For more information about offer codes, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

### Deprecated
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerType: Transaction.OfferType?](./offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](./offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerid)*