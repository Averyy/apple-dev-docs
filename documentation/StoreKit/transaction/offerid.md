# offerID

**Framework**: StoreKit  
**Kind**: property

A string that identifies an offer applied to the current subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var offerID: String? { get }
```

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

This value is `nil` if there isn’t an offer, or if the offer type is [`introductory`](transaction/offertype-swift.struct/introductory.md).

If the offer type is [`promotional`](transaction/offertype-swift.struct/promotional.md), this value contains the promotional offer identifier you set up in App Store Connect. For more information about promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev16dfca448).

If the offer type is [`code`](transaction/offertype-swift.struct/code.md), this value contains the reference name of the offer code you set up in App Store Connect. For more information about offer codes, see [`Set up offer codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

- [var currencyCode: String?](transaction/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](transaction/environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerPaymentModeStringRepresentation: String?](transaction/offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](transaction/offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](transaction/reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](transaction/storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offerid)*