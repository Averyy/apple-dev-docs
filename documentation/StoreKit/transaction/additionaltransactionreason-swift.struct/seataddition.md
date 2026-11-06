# seatAddition

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A reason that indicates the group purchaser added seats to a multiseat subscription partway through the period.

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
static let seatAddition: Transaction.AdditionalTransactionReason
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)

## Discussion

Both the period’s original transaction and the transaction for the added seats have this reason. The raw value is `SEAT_ADDITION`, the same value that the App Store Server API uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/additionaltransactionreason-swift.struct/seataddition)*