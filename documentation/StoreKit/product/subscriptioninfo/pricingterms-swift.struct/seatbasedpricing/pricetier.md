# Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A per-seat price that applies to a range of seats.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct PriceTier
```

## Topics

### Getting the seat range
- [let minimumSeats: Int](./pricetier/minimumseats.md)
  The seat count at which this tier’s range starts.
- [let maximumSeats: Int?](./pricetier/maximumseats.md)
  The upper limit of this tier’s seat range.
### Getting the price
- [let billingInfo: Product.SubscriptionInfo.BillingInfo](./pricetier/billinginfo.md)
  The price of one seat in this tier, and the period between renewals.

## Relationships

### Conforms To
- [Equatable](../../../../../Swift/equatable.md)
- [Hashable](../../../../../Swift/hashable.md)
- [Sendable](../../../../../Swift/sendable.md)
- [SendableMetatype](../../../../../Swift/sendablemetatype.md)

## See Also

### Getting the price tiers
- [let priceTiers: [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier]](./pricetiers.md)
  The price tiers of the subscription, in ascending order of seat count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetier)*