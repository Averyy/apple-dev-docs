# specialPricingBadgeImage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A template image for Maps to display when special prices apply.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var specialPricingBadgeImage: INImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INImage * specialPricingBadgeImage;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INImage * specialPricingBadgeImage;
```

#### Discussion

When offering special pricing, use this property to specify an image for Maps to display next to the pricing information. The width and height of the image must both be 12 points and the image must be a template image—that is, an image whose alpha channel defines the shape of the image. Set this property to `nil` if special pricing does not apply.

## See Also

### Specifying Pricing Information
- [var priceRange: INPriceRange?](./pricerange.md)
  The range of prices for this ride option.
- [var specialPricing: String?](./specialpricing.md)
  A user-visible string describing any special pricing considerations that apply to this ride.
- [var usesMeteredFare: Bool?](./usesmeteredfare-1sig1.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.
- [var fareLineItems: [INRideFareLineItem]?](./farelineitems.md)
  An array of price-related items that break down the costs of the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/specialpricingbadgeimage)*