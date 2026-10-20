# SKProductDiscount.Type

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values representing the types of discount offers an app can present.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.OfferType.

## Declaration

```swift
enum `Type`
```

```c
enum SKProductDiscountType : NSUInteger;
```

## Topics

### Types of Offers
- [SKProductDiscount.Type.introductory](./type-swift.enum/introductory.md)
  A constant indicating the discount type is an introductory offer.
- [SKProductDiscount.Type.subscription](./type-swift.enum/subscription.md)
  A constant indicating the discount type is a promotional offer.
### Initializers
- [init?(rawValue: UInt)](./type-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the Discount
- [var identifier: String?](./identifier.md)
  A string used to uniquely identify a discount offer for a product.
- [var type: SKProductDiscount.Type](./type-swift.property.md)
  The type of discount offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/type-swift.enum)*