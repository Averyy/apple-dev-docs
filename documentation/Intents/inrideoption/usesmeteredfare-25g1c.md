# usesMeteredFare

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the price uses a metered fare instead of a fixed price.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * usesMeteredFare;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * usesMeteredFare;
```

#### Discussion

The [`NSNumber`](../../Foundation/nsnumber.md) object in this property contains a Boolean value indicating whether the ride uses a metered fare instead of a fixed price. When set to [`true`](../../Swift/true.md), any information in the [`priceRange`](./pricerange.md) property isn’t shown to the user.

## See Also

### Specifying Pricing Information
- [var priceRange: INPriceRange?](./pricerange.md)
  The range of prices for this ride option.
- [var specialPricing: String?](./specialpricing.md)
  A user-visible string describing any special pricing considerations that apply to this ride.
- [var specialPricingBadgeImage: INImage?](./specialpricingbadgeimage.md)
  A template image for Maps to display when special prices apply.
- [var fareLineItems: [INRideFareLineItem]?](./farelineitems.md)
  An array of price-related items that break down the costs of the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/usesmeteredfare-25g1c)*