# introductoryPrice

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The object containing introductory price information for the product.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.subscription.introductionaryOffer.

## Declaration

```swift
var introductoryPrice: SKProductDiscount? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKProductDiscount * introductoryPrice;
```

## Mentions

- [Implementing introductory offers in your app](../implementing-introductory-offers-in-your-app.md)

## Discussion

If you’ve set up introductory prices in App Store Connect, the introductory price property will be populated. This property is `nil` if the product has no introductory price.

Before displaying UI that offers the introductory price, you must first determine if the user is eligible to receive it. See [Implementing introductory offers in your app](../implementing-introductory-offers-in-your-app.md) for information on determining eligibility and displaying introductory prices.

## See Also

### Getting Pricing Information
- [var price: NSDecimalNumber](./price.md)
  The cost of the product in the local currency.
- [var priceLocale: Locale](./pricelocale.md)
  The locale used to format the price of the product.
- [var discounts: [SKProductDiscount]](./discounts.md)
  An array of subscription offers available for the auto-renewable subscription.
- [class SKProductDiscount](../skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/introductoryprice)*