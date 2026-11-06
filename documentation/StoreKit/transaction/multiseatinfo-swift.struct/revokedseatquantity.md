# revokedSeatQuantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of seats from this transaction that the App Store revoked.

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
let revokedSeatQuantity: Int?
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)

## Discussion

This value is `nil` if the App Store hasn’t revoked any seats from the transaction. The App Store revokes seats when it refunds some of them, for example. Refunds apply per transaction: when more than one transaction represents a period, as [`additionalTransactionReason`](../additionaltransactionreason-swift.property.md) indicates, a refund that covers seats from several of those transactions updates each of them.

The transaction’s [`revocationDate`](../revocationdate.md) and [`revocationReason`](../revocationreason-swift.property.md) appear only when the App Store revokes every seat on the transaction. A refund for some of the seats doesn’t change the transactions of the remaining group members.

For more information, see [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/revokedseatquantity)*