# discounts

**Framework**: StoreKit  
**Kind**: property

An array of subscription offers available for the auto-renewable subscription.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var discounts: [SKProductDiscount] { get }
```

## Mentions

- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)

#### Discussion

The [`discounts`](skproduct/discounts.md) array contains all of the introductory offers and promotional offers that you set up in App Store Connect for this subscription ([`productIdentifier`](skproduct/productidentifier.md)).  It’s up to the logic in your app to decide which offer to present to the user.

For more information about offers, see [`Implementing promotional offers in your app`](implementing-promotional-offers-in-your-app.md), and [`Implementing introductory offers in your app`](implementing-introductory-offers-in-your-app.md).

## See Also

- [var price: NSDecimalNumber](skproduct/price.md)
  The cost of the product in the local currency.
- [var priceLocale: Locale](skproduct/pricelocale.md)
  The locale used to format the price of the product.
- [var introductoryPrice: SKProductDiscount?](skproduct/introductoryprice.md)
  The object containing introductory price information for the product.
- [class SKProductDiscount](skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/discounts)*