# offerID

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies an offer applied to the current subscription.

**Availability**:
- iOS 15.0+ - Deprecated in 17.2 (renamed: offer.id)
- iPadOS 15.0+ - Deprecated in 17.2 (renamed: offer.id)
- Mac Catalyst 15.0+ - Deprecated in 17.2 (renamed: offer.id)
- macOS 12.0+ - Deprecated in 14.2 (renamed: offer.id)
- tvOS 15.0+ - Deprecated in 17.2 (renamed: offer.id)
- visionOS 1.0+ - Deprecated in 1.1 (renamed: offer.id)
- watchOS 8.0+ - Deprecated in 10.2 (renamed: offer.id)

> **Deprecated**: Use [`offer`](./offer-swift.property.md) instead.

## Declaration

```swift
var offerID: String? { get }
```

## Mentions

- [Supporting subscription offer codes in your app](../supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

This value is `nil` if there isn’t an offer, or if the offer type is [`introductory`](./offertype-swift.struct/introductory.md).

If the offer type is [`promotional`](./offertype-swift.struct/promotional.md), this value contains the promotional offer identifier you set up in App Store Connect. For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

If the offer type is [`code`](./offertype-swift.struct/code.md), this value contains the reference name of the offer code you set up in App Store Connect. For more information about offer codes, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

### Deprecated
- [var currencyCode: String?](./currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](./environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerPaymentModeStringRepresentation: String?](./offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](./offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](./reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](./storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offerid)*