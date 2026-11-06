# additionalTransactionReason

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The reason that more than one transaction represents the subscription period.

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
let additionalTransactionReason: Transaction.AdditionalTransactionReason?
```

## Discussion

This value is `nil` if one transaction represents the whole period. When it isn’t `nil`, evaluate every transaction in the period together to get the number of seats in the period.

For example, when the group purchaser adds seats partway through a period, the purchase creates a second transaction for the added seats, and both transactions have a reason of [`seatAddition`](./additionaltransactionreason-swift.struct/seataddition.md). The subscription’s seats for the period are the seats on the period’s transactions that aren’t revoked. Adding seats doesn’t set [`isUpgraded`](./isupgraded.md). At the next renewal, one transaction covers all the seats again.

For more information, see [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md).

## See Also

### Getting multiseat information
- [let multiSeatInfo: Transaction.MultiSeatInfo?](./multiseatinfo-swift.property.md)
  The seat information for a multiseat subscription transaction.
- [Transaction.MultiSeatInfo](./multiseatinfo-swift.struct.md)
  The invitation model, price tiers, and revoked seats of a multiseat subscription transaction.
- [Transaction.AdditionalTransactionReason](./additionaltransactionreason-swift.struct.md)
  Reasons that more than one transaction represents a single subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/additionaltransactionreason-swift.property)*