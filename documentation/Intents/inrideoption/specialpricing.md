# specialPricing

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-visible string describing any special pricing considerations that apply to this ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var specialPricing: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * specialPricing;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * specialPricing;
```

#### Discussion

Use this property when you need to communicate special pricing conditions to the user. For example, you might set the value of this property to “Sale” when you want to offer discounted rides. The value in the [`priceRange`](./pricerange.md) and [`fareLineItems`](./farelineitems.md) properties should account for any special pricing you offer. Set this property to `nil` if special pricing does not apply.

## See Also

### Specifying Pricing Information
- [var priceRange: INPriceRange?](./pricerange.md)
  The range of prices for this ride option.
- [var specialPricingBadgeImage: INImage?](./specialpricingbadgeimage.md)
  A template image for Maps to display when special prices apply.
- [var usesMeteredFare: Bool?](./usesmeteredfare-1sig1.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.
- [var fareLineItems: [INRideFareLineItem]?](./farelineitems.md)
  An array of price-related items that break down the costs of the ride.
- [usesMeteredFare](./usesmeteredfare-25g1c.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/specialpricing)*