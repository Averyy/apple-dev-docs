# Transaction.AdvancedCommerceInfo.SeatPriceTier

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A per-seat price and the number of seats it covers, as your Advanced Commerce API request defines them.

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
struct SeatPriceTier
```

## Overview

These tiers describe the prices you set for an item’s seats. The tiers in [`priceTiers`](../multiseatinfo-swift.struct/pricetiers.md) record the seats that the customer bought at each price instead.

## Topics

### Getting the price and seats
- [let price: Decimal](./seatpricetier/price.md)
  The per-seat price of the seats in this tier.
- [let maximumSeatQuantity: Int?](./seatpricetier/maximumseatquantity.md)
  The maximum number of seats in this price tier.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Structures
- [Transaction.AdvancedCommerceInfo.Item](./item.md)
  The developer-defined product that was purchased.
- [Transaction.AdvancedCommerceInfo.Offer](./offer.md)
  Information about the offer that was redeemed as part of the purchase.
- [Transaction.AdvancedCommerceInfo.Refund](./refund.md)
  Information about refunds that were issued as part of this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/seatpricetier)*