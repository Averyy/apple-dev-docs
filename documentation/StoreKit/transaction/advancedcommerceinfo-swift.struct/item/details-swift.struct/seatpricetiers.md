# seatPriceTiers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The per-seat price tiers for the item’s seats.

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
let seatPriceTiers: [Transaction.AdvancedCommerceInfo.SeatPriceTier]
```

## Discussion

In a transaction, these are the tiers from your Advanced Commerce API request for the purchase. In renewal information, they’re the tiers at which the item’s seats renew.

To get the number of seats that the customer bought at each price, use the price tiers in [`multiSeatInfo`](../../../multiseatinfo-swift.property.md).

## See Also

### Instance Properties
- [let description: String](./description.md)
  The description of the item.
- [let displayName: String](./displayname.md)
  The display name of the item.
- [let offer: Transaction.AdvancedCommerceInfo.Offer?](./offer.md)
  The offer applied to the purchase of this item, if any.
- [let price: Decimal](./price.md)
  The price of the item.
- [let sku: String](./sku.md)
  Unique identifier for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/item/details-swift.struct/seatpricetiers)*