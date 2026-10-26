# fareLineItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of price-related items that break down the costs of the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var fareLineItems: [INRideFareLineItem]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INRideFareLineItem *> * fareLineItems;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INRideFareLineItem *> * fareLineItems;
```

#### Discussion

When the cost of a ride has multiple components, use [`INRideFareLineItem`](../inridefarelineitem.md) objects to break down the individual costs of the ride. You can use line items to specify fixed charges, per-mile charges, special surcharges, or any other charges that you designate. The system displays the fare line items to the user as part of the pricing information.

## See Also

### Specifying Pricing Information
- [var priceRange: INPriceRange?](./pricerange.md)
  The range of prices for this ride option.
- [var specialPricing: String?](./specialpricing.md)
  A user-visible string describing any special pricing considerations that apply to this ride.
- [var specialPricingBadgeImage: INImage?](./specialpricingbadgeimage.md)
  A template image for Maps to display when special prices apply.
- [var usesMeteredFare: Bool?](./usesmeteredfare-1sig1.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.
- [usesMeteredFare](./usesmeteredfare-25g1c.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/farelineitems)*