# priceTiers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The price tiers of the transaction’s seats, with the number of seats bought at each price.

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
let priceTiers: [Transaction.MultiSeatInfo.PriceTier]
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

Each tier gives a per-seat price and the number of seats that the customer bought at that price. For example, 8 seats against tiers of 5 seats at $9.99 and more seats at $7.99 use two tiers: 5 seats at $9.99 and 3 seats at $7.99.

To get the amount the transaction charged for its seats, add up each tier’s price multiplied by its quantity. Don’t multiply the transaction’s [`price`](../price.md) by its [`purchasedQuantity`](../purchasedquantity.md). For a multiseat subscription, the price is the average price per seat.

The array isn’t in a guaranteed order. To list the tiers in the order that seats fill them, sort them by price, highest first.

For more information, see [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md).

## See Also

### Getting the price tiers
- [Transaction.MultiSeatInfo.PriceTier](./pricetier.md)
  A per-seat price and the number of seats that the customer bought at that price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/pricetiers)*