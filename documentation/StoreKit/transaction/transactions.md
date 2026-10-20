# Transaction.Transactions

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of transactions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Transactions
```

#### Overview

You don’t create a [`Transaction.Transactions`](./transactions.md) sequence directly. Use methods such as [`all`](./all.md), [`updates`](./updates.md), or [`currentEntitlements`](./currententitlements.md) to get transactions.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring transaction-related changes
- [static var updates: Transaction.Transactions](./updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/transactions)*