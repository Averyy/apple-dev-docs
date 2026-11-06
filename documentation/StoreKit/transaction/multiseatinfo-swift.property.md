# multiSeatInfo

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The seat information for a multiseat subscription transaction.

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
let multiSeatInfo: Transaction.MultiSeatInfo?
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)
- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

This value is `nil` if the transaction isn’t for a multiseat subscription.

With Apple-hosted invitations, each group member has their own transaction, and it contains the same seat information as the group purchaser’s, including the number of seats and the price tiers.

For more information, see [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Getting multiseat information
- [Transaction.MultiSeatInfo](./multiseatinfo-swift.struct.md)
  The invitation model, price tiers, and revoked seats of a multiseat subscription transaction.
- [let additionalTransactionReason: Transaction.AdditionalTransactionReason?](./additionaltransactionreason-swift.property.md)
  The reason that more than one transaction represents the subscription period.
- [Transaction.AdditionalTransactionReason](./additionaltransactionreason-swift.struct.md)
  Reasons that more than one transaction represents a single subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.property)*