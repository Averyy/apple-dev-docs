# Transaction.MultiSeatInfo.PriceTier

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A per-seat price and the number of seats that the customer bought at that price.

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

## Overview

A transaction’s price tiers record the seats that the customer bought at each price. The tiers of a product’s seat-based pricing terms, [`Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier`](../../product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetier.md), give a seat range for each price instead.

## Topics

### Getting the price and seats
- [let price: Decimal](./pricetier/price.md)
  The per-seat price of the seats in this tier.
- [let quantity: Int](./pricetier/quantity.md)
  The number of seats that the customer bought at this tier’s price.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the price tiers
- [let priceTiers: [Transaction.MultiSeatInfo.PriceTier]](./pricetiers.md)
  The price tiers of the transaction’s seats, with the number of seats bought at each price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/pricetier)*