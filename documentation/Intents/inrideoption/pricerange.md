# priceRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of prices for this ride option.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var priceRange: INPriceRange? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INPriceRange * priceRange;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INPriceRange * priceRange;
```

## Mentions

- [Generating a List of Ride Options](../../SiriKit/generating-a-list-of-ride-options.md)

#### Discussion

Use this property to specify the approximate cost of the ride. Price ranges should reflect the actual price you plan to charge and should include any special pricing that currently applies. If the ride option also includes separate line items, display those items separately.

If the [`usesMeteredFare`](./usesmeteredfare-25g1c.md) property is [`true`](../../Swift/true.md), the information in this property is not displayed.

## See Also

### Specifying Pricing Information
- [var specialPricing: String?](./specialpricing.md)
  A user-visible string describing any special pricing considerations that apply to this ride.
- [var specialPricingBadgeImage: INImage?](./specialpricingbadgeimage.md)
  A template image for Maps to display when special prices apply.
- [var usesMeteredFare: Bool?](./usesmeteredfare-1sig1.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.
- [var fareLineItems: [INRideFareLineItem]?](./farelineitems.md)
  An array of price-related items that break down the costs of the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/pricerange)*