# SKProductDiscount

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

The details of an introductory offer or a promotional offer for an auto-renewable subscription.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.

## Declaration

```swift
class SKProductDiscount
```

```objc
@interface SKProductDiscount : NSObject
```

## Mentions

- [Implementing promotional offers in your app](./implementing-promotional-offers-in-your-app.md)

#### Overview

You set up introductory and promotional offers in App Store Connect. [`SKProductDiscount`](./skproductdiscount.md) contains the offer information as retrieved from the App Store.

For more information about setting up offers, see [Set an introductory offer for an auto-renewable subscription](https://help.apple.com/app-store-connect/#/deve1d49254f) and [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

## Topics

### Identifying the Discount
- [var identifier: String?](./skproductdiscount/identifier.md)
  A string used to uniquely identify a discount offer for a product.
- [var type: SKProductDiscount.Type](./skproductdiscount/type-swift.property.md)
  The type of discount offer.
- [SKProductDiscount.Type](./skproductdiscount/type-swift.enum.md)
  Values representing the types of discount offers an app can present.
### Getting Price and Payment Mode
- [var price: NSDecimalNumber](./skproductdiscount/price.md)
  The discount price of the product in the local currency.
- [var priceLocale: Locale](./skproductdiscount/pricelocale.md)
  The locale used to format the discount price of the product.
- [var paymentMode: SKProductDiscount.PaymentMode](./skproductdiscount/paymentmode-swift.property.md)
  The payment mode for this product discount.
- [SKProductDiscount.PaymentMode](./skproductdiscount/paymentmode-swift.enum.md)
  Values representing the payment modes for a product discount.
### Getting the Discount Duration
- [var numberOfPeriods: Int](./skproductdiscount/numberofperiods.md)
  An integer that indicates the number of periods the product discount is available.
- [var subscriptionPeriod: SKProductSubscriptionPeriod](./skproductdiscount/subscriptionperiod.md)
  An object that defines the period for the product discount.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Pricing Information
- [var price: NSDecimalNumber](./skproduct/price.md)
  The cost of the product in the local currency.
- [var priceLocale: Locale](./skproduct/pricelocale.md)
  The locale used to format the price of the product.
- [var introductoryPrice: SKProductDiscount?](./skproduct/introductoryprice.md)
  The object containing introductory price information for the product.
- [var discounts: [SKProductDiscount]](./skproduct/discounts.md)
  An array of subscription offers available for the auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount)*