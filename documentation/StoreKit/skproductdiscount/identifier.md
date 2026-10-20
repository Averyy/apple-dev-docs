# identifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string used to uniquely identify a discount offer for a product.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.id.

## Declaration

```swift
var identifier: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * identifier;
```

## Mentions

- [Generating a signature for promotional offers](../generating-a-signature-for-promotional-offers.md)
- [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md)

#### Discussion

You set up offers and their identifiers in App Store Connect.

## See Also

### Identifying the Discount
- [var type: SKProductDiscount.Type](./type-swift.property.md)
  The type of discount offer.
- [SKProductDiscount.Type](./type-swift.enum.md)
  Values representing the types of discount offers an app can present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/identifier)*