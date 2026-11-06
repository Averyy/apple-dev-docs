# renewalPriceTiers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The price tiers of the seats at the next renewal, with the number of seats at each price.

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
let renewalPriceTiers: [Transaction.MultiSeatInfo.PriceTier]
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../../../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

Each element has the same type as a transaction’s price tiers, [`Transaction.MultiSeatInfo.PriceTier`](../../../../transaction/multiseatinfo-swift.struct/pricetier.md). To get the amount of the next renewal, add up each tier’s price multiplied by its quantity. The [`renewalPrice`](../renewalprice.md) value is the average price per seat.

The array isn’t in a guaranteed order.

For more information, see [Managing the life cycle of multiseat subscriptions](../../../../managing-the-life-cycle-of-multiseat-subscriptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/multiseatinfo-swift.struct/renewalpricetiers)*